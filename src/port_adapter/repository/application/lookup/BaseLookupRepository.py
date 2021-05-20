"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from elasticsearch_dsl import Document, Q

from src.port_adapter.repository.es_model.model.AttributeData import AttributeData
from src.resource.common.Util import Util
from src.resource.logging.decorator import debugLogger


class BaseLookupRepository:
    @debugLogger
    def lookup(self, *args, **kwargs):
        resultFrom = kwargs["resultFrom"] if "resultFrom" in kwargs else 0
        resultSize = kwargs["resultSize"] if "resultSize" in kwargs else 0
        orders = kwargs["orders"] if "orders" in kwargs else []
        filters = kwargs["filters"] if "filters" in kwargs else []
        esModel: Document = kwargs["esModel"] if "esModel" in kwargs else None
        lookupModel = kwargs["lookupModel"] if "lookupModel" in kwargs else None

        esSearch = esModel.search()
        """
        Pagination
        """
        esSearch = esSearch[resultFrom : resultFrom + resultSize]
        """
        Filtering, Querying
        """
        for filterItem in filters:
            filterKey: str = filterItem["key"]
            filterValue = filterItem["value"]
            if filterKey != "_all":
                attributeData = esModel.attributeDataBySnakeCaseAttributeName(
                    instance=None, snakeCaseAttributeName=filterKey
                )
                esSearch = self._esSearchByAttributeDataListAndFilterValue(
                    attributeDataList=[attributeData], filterValue=filterValue, esSearch=esSearch
                )
            else:  # If the filter is '_all', then filter on all keys
                # We need to add them into a list, so we can then OR-ing them
                attributeDataList = []
                for attribute in lookupModel.attributes():
                    attributeDataList.append(
                        esModel.attributeDataBySnakeCaseAttributeName(
                            snakeCaseAttributeName=Util.camelCaseToLowerSnakeCase(attribute)
                        )
                    )
                esSearch = self._esSearchByAttributeDataListAndFilterValue(
                    attributeDataList=attributeDataList, filterValue=filterValue, esSearch=esSearch
                )

        """
        Sorting
        """
        sortList = []
        for order in orders:
            attributeData = esModel.attributeDataBySnakeCaseAttributeName(
                instance=None, snakeCaseAttributeName=order["orderBy"]
            )
            # If it is a nested field then we need to use 'path' key
            if attributeData.repoName.find(".") != -1:
                sortList.append(
                    {
                        attributeData.repoName: {
                            "order": order["direction"],
                            "nested": {"path": attributeData.repoName[: attributeData.repoName.rindex(".")]},
                        }
                    }
                )
            else:  # Otherwise if it is not a nested field, then use direct ordering
                sortList.append({attributeData.repoName: {"order": order["direction"]}})
        esSearch = esSearch.sort(*sortList)
        esResults = esSearch.execute()
        """
        Result aggregation
        """
        items = []
        for esResultItem in esResults:
            items.append(
                self._constructDomainModelObjectFromEsObject(
                    lookupModel=lookupModel, esObject=esResultItem, esModel=esModel
                )
            )

        return {"items": items, "totalItemCount": esResults.hits.total.value}

    def _esSearchByAttributeDataListAndFilterValue(self, attributeDataList: List[AttributeData], filterValue, esSearch):
        queryList = []
        for attributeData in attributeDataList:
            canAddAttributeDataToQuery = True
            # Make the query type to be 'wildcard'
            fieldQueryType = "wildcard"
            # If the data type is 'int' then we need to use 'term' query
            if attributeData.dataType == "int":
                fieldQueryType = "term"
                if isinstance(filterValue, str):
                    filterValue = filterValue.replace("*", "")
                    try:
                        filterValue = int(filterValue)
                    except:
                        canAddAttributeDataToQuery = False
            # Do not add a query for the current attribute if it is not suitable to be queried
            if canAddAttributeDataToQuery:
                # If it is a nested field, then we need to use 'path' in order to query it
                if attributeData.repoName.find(".") != -1:
                    queryList.append(
                        Q(
                            "nested",
                            path=attributeData.repoName[: attributeData.repoName.rindex(".")],
                            query=Q(fieldQueryType, **{attributeData.repoName: filterValue}),
                        )
                    )
                else:
                    queryList.append(Q(fieldQueryType, **{attributeData.repoName: filterValue}))
        return esSearch.query(Q("bool", should=queryList))

    def _constructDomainModelObjectFromEsObject(self, lookupModel, esObject, esModel: Document):
        domainModelAttributes = lookupModel.attributes()
        kwargs = {}
        for attribute in domainModelAttributes:
            attributeData: AttributeData = esModel.attributeDataBySnakeCaseAttributeName(
                esObject, Util.camelCaseToLowerSnakeCase(attribute)
            )
            kwargs[attribute] = attributeData.repoValue

        return lookupModel(**kwargs)
