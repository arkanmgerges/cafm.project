"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List, Union

from elasticsearch_dsl import Document, Q

from src.application.lookup.model_data.BaseLookupModel import BaseLookupModel
from src.application.lookup.model_data.LookupModelAttributeData import LookupModelAttributeData
from src.port_adapter.repository.es_model.model.EsModel import EsModel
from src.port_adapter.repository.es_model.model.EsModelAttributeData import EsModelAttributeData
from src.resource.common.Util import Util
from src.resource.logging.decorator import debugLogger


class BaseLookupRepository:
    @debugLogger
    def lookup(self, *args, **kwargs):
        resultFrom = kwargs["resultFrom"] if "resultFrom" in kwargs else 0
        resultSize = kwargs["resultSize"] if "resultSize" in kwargs else 0
        orders = kwargs["orders"] if "orders" in kwargs else []
        filters = kwargs["filters"] if "filters" in kwargs else []
        esModel: Union[Document, EsModel] = kwargs["esModel"] if "esModel" in kwargs else None
        lookupModel: BaseLookupModel = kwargs["lookupModel"] if "lookupModel" in kwargs else None

        esSearch = esModel.search()
        """
        Pagination
        """
        esSearch = esSearch[resultFrom : resultFrom + resultSize]
        """
        Filtering, Querying
        """
        esSearch = self._constructFiltering(
            filters=filters, esModel=esModel, esSearch=esSearch, lookupModel=lookupModel
        )

        """
        Sorting
        """
        esSearch = self._constructSorting(orders=orders, esModel=esModel, esSearch=esSearch)
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

    def _constructFiltering(self, filters, esModel, esSearch, lookupModel):
        for filterItem in filters:
            filterKey: str = filterItem["key"]
            filterValue = filterItem["value"]
            if filterKey != "_all":
                attributeData = esModel.attributeDataBySnakeCaseAttributeName(
                    instance=None, snakeCaseAttributeName=filterKey
                )
                esSearch = self._constructEsSearch(
                    attributeDataResultList=[
                        {"key": filterKey, "dataType": attributeData.dataType, "attribute": attributeData}
                    ],
                    filterValue=filterValue,
                    esSearch=esSearch,
                )
            else:  # If the filter is '_all', then filter on all keys
                # We need to add them into a list, so we can then OR-ing them
                attributeDataResultList: List[dict] = []
                for modelKey, lookupModelAttributeData in lookupModel.attributes().items():
                    modelKey = Util.camelCaseToLowerSnakeCase(modelKey)
                    if lookupModelAttributeData.isClass:
                        resultList = self._parseLookupModelAttributes(modelKey, lookupModelAttributeData)
                        for item in resultList:
                            attributeDataResultList.append(
                                {
                                    "key": item["key"],
                                    "dataType": item["dataType"],
                                    "attribute": esModel.attributeDataBySnakeCaseAttributeName(
                                        snakeCaseAttributeName=item["key"]
                                    ),
                                }
                            )
                    else:
                        attributeDataResultList.append(
                            {
                                "key": modelKey,
                                "dataType": lookupModelAttributeData.dataType,
                                "attribute": esModel.attributeDataBySnakeCaseAttributeName(
                                    snakeCaseAttributeName=modelKey
                                ),
                            }
                        )
                esSearch = self._constructEsSearch(
                    attributeDataResultList=attributeDataResultList, filterValue=filterValue, esSearch=esSearch
                )
        return esSearch

    def _constructSorting(self, orders, esModel, esSearch):
        sortList = []
        for order in orders:
            attributeData = esModel.attributeDataBySnakeCaseAttributeName(
                instance=None, snakeCaseAttributeName=order["orderBy"]
            )
            # If it is a nested field then we need to use 'path' key
            if attributeData.attributeRepoName.find(".") != -1:
                sortList.append(
                    {
                        attributeData.attributeRepoName: {
                            "order": order["direction"],
                            "nested": {"path": attributeData.attributeRepoName},
                        }
                    }
                )
            else:  # Otherwise if it is not a nested field, then use direct ordering
                sortList.append({attributeData.attributeRepoName: {"order": order["direction"]}})
        esSearch = esSearch.sort(*sortList)
        return esSearch

    def _parseLookupModelAttributes(self, lookupModelKey: str, lookupModelAttributeData: LookupModelAttributeData):
        result = []
        if lookupModelAttributeData.isClass:
            for (
                lookupModelAttributeName,
                lookupModelAttributeDataItem,
            ) in lookupModelAttributeData.dataType.attributes().items():
                innerResult = self._parseLookupModelAttributes(
                    f"{lookupModelKey}.{lookupModelAttributeName}", lookupModelAttributeDataItem
                )
                result = result + innerResult
        else:
            return [{"key": lookupModelKey, "dataType": lookupModelAttributeData.dataType}]
        return result

    @debugLogger
    def _filterModelKeyByModelKeyAndLookupModelAttributeData(
        self, modelKey: str, lookupAttributeData: LookupModelAttributeData
    ):
        if lookupAttributeData.isClass:
            return self._filterModelKeyByModelKeyAndLookupModelAttributeData(f"{modelKey}.")
        else:
            return modelKey

    @debugLogger
    def _constructEsSearch(self, attributeDataResultList: List[dict], filterValue, esSearch):
        queryList = []
        for attributeDataResult in attributeDataResultList:
            canAddAttributeDataToQuery = True
            # Make the query type to be 'wildcard'
            fieldQueryType = "wildcard"
            # If the data type is 'int' then we need to use 'term' query
            if attributeDataResult["dataType"] is int:
                fieldQueryType = "term"
                if isinstance(filterValue, str):
                    filterValue = filterValue.replace("*", "")
                    try:
                        filterValue = int(filterValue)
                    except:
                        canAddAttributeDataToQuery = False
            # Do not add a query for the current attribute if it is not suitable to be queried
            if canAddAttributeDataToQuery:
                filterKey = attributeDataResult["key"]
                # If it is a nested field, then we need to use 'path' in order to query it
                if filterKey.find(".") != -1:
                    queryList.append(
                        Q(
                            "nested",
                            path=attributeDataResult["attribute"].attributeRepoName,
                            query=Q(fieldQueryType, **{filterKey: filterValue}),
                        )
                    )
                else:
                    queryList.append(Q(fieldQueryType, **{filterKey: filterValue}))
        return esSearch.query(Q("bool", should=queryList))

    @debugLogger
    def _constructDomainModelObjectFromEsObject(self, lookupModel, esObject, esModel: Union[Document, EsModel]):
        if esObject is None:
            return None
        lookupModelAttributes = lookupModel.attributes()
        kwargs = {}
        lookupModelAttributeData: LookupModelAttributeData
        for lookupModelAttributeKey, lookupModelAttributeData in lookupModelAttributes.items():
            snakeCaseLookupModelAttributeKey = Util.camelCaseToLowerSnakeCase(lookupModelAttributeKey)
            esAttributeData: EsModelAttributeData = esModel.attributeDataBySnakeCaseAttributeName(
                esObject, snakeCaseLookupModelAttributeKey
            )
            if lookupModelAttributeData.isClass:
                if lookupModelAttributeData.isArray:
                    kwargs[lookupModelAttributeKey] = []
                    if type(esAttributeData.attributeRepoValue) is list and esObject is not None:
                        kwargs[lookupModelAttributeKey] = [
                            self._constructDomainModelObjectFromEsObject(
                                lookupModel=lookupModelAttributeData.dataType,
                                esObject=currentEsObject,
                                esModel=esAttributeData.dataType,
                            )
                            for currentEsObject in esAttributeData.attributeRepoValue
                        ]
                else:
                    kwargs[lookupModelAttributeKey] = None
                    if esObject is not None:
                        kwargs[lookupModelAttributeKey] = self._constructDomainModelObjectFromEsObject(
                            lookupModel=lookupModelAttributeData.dataType,
                            esObject=esAttributeData.attributeRepoValue,
                            esModel=esAttributeData.dataType,
                        )
            else:
                kwargs[lookupModelAttributeKey] = (
                    esAttributeData.attributeRepoValue if esAttributeData is not None else None
                )
        return lookupModel(**kwargs)
