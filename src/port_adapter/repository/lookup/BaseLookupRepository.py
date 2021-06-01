"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from datetime import datetime
from typing import List, Union

from elasticsearch_dsl import Document, Q, AttrList
from elasticsearch_dsl.utils import ObjectBase

from src.application.lookup.model_data.BaseLookupModel import BaseLookupModel
from src.application.lookup.model_data.LookupModelAttributeData import LookupModelAttributeData
from src.port_adapter.repository.es_model.model.EsModel import EsModel
from src.port_adapter.repository.es_model.model.EsModelAttributeData import EsModelAttributeData
from src.resource.common.DateTimeHelper import DateTimeHelper
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
        esSearch = self._constructFiltering2(
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


    def _constructFiltering2(self, filters, esModel, esSearch, lookupModel):
        for filterItem in filters:
            filterKey: str = filterItem["key"]
            if filterKey == "_all":
                filterItems = self._allAttributesFullPath(lookupModel=lookupModel, filterValue=filterItem["value"])
                esSearch = self._constructQuery(filters=filterItems, esModel=esModel, esSearch=esSearch)
            elif filterKey.find(".") != -1:
                # nested
                esSearch = self._constructQuery(filters=[filterItem], esModel=esModel, esSearch=esSearch)
            else: # root
                esSearch = self._constructQuery(filters=[filterItem], esModel=esModel, esSearch=esSearch)
        return esSearch

    def _allAttributesFullPath(self, lookupModel, filterValue):
        attributeDataResultList: List[dict] = []
        for modelKey, lookupModelAttributeData in lookupModel.attributes().items():
            modelKey = Util.camelCaseToLowerSnakeCase(modelKey)
            if lookupModelAttributeData.isClass:
                resultList = self._allAttributesFullPath(lookupModel=lookupModelAttributeData.dataType, filterValue=filterValue)
                for item in resultList:
                    attributeDataResultList.append(
                        {
                            "key": f'{modelKey}.{item["key"]}',
                            "value": item["value"],
                        }
                    )
            else:
                attributeDataResultList.append(
                    {
                        "key": modelKey,
                        "value": filterValue,
                    }
                )
        return attributeDataResultList

    def _constructQuery(self, filters, esModel, esSearch):
        queryList = []
        for filterItem in filters:
            filterKey: str = filterItem["key"]
            filterValue = filterItem["value"]
            fieldType = self._fieldType(filterKey=filterKey, esModel=esModel)
            fieldQueryType = "wildcard"
            if fieldType is int:
                fieldQueryType = "term"
                filterValue = filterValue.replace("*", "")
                try:
                    filterValue = int(filterValue)
                except:
                    filterValue = 0

            if fieldType is bool:
                fieldQueryType = "term"
                filterValue = filterValue.replace("*", "")
                try:
                    filterValue = bool(filterValue)
                except:
                    filterValue = False

            if fieldType is datetime:
                fieldQueryType = "term"
                filterValue = filterValue.replace("*", "")
                try:
                    x = datetime(filterValue)
                except:
                    filterValue = DateTimeHelper.utcNow()

            if fieldType is float:
                fieldQueryType = "term"
                filterValue = filterValue.replace("*", "")
                try:
                    filterValue = float(filterValue)
                except:
                    filterValue = DateTimeHelper.utcNow()

            if filterKey.find(".") != -1:  # nested
                queryList.append(
                    Q(
                        "nested",
                        path=filterKey[:filterKey.rfind(".")],
                        query=Q(fieldQueryType, **{filterKey: filterValue}),
                    )
                )
            else:  # root
                queryList.append(Q(fieldQueryType, **{filterKey: filterValue}))
        return esSearch.query(Q("bool", should=queryList))

    def _fieldType(self, filterKey, esModel):
        esModelAttributeData: EsModelAttributeData
        if filterKey.find(".") != -1:
            # nested
            classPartsAndAttribute = filterKey.split(".")  # country.id
            attribute = classPartsAndAttribute[-1:][0]  # Take the last part
            tmpEsModel = esModel
            for index in range(0, len(classPartsAndAttribute) - 1):
                esModelAttributeData = tmpEsModel.attributeDataBySnakeCaseAttributeName(snakeCaseAttributeName=classPartsAndAttribute[index])
                if esModelAttributeData is not None and esModelAttributeData.isClass:
                    tmpEsModel = esModelAttributeData.dataType
                else:
                    return str
            return tmpEsModel.attributeDataBySnakeCaseAttributeName(snakeCaseAttributeName=attribute).dataType
        else:  # root
            esModelAttributeData = esModel.attributeDataBySnakeCaseAttributeName(snakeCaseAttributeName=filterKey)
            return esModelAttributeData.dataType

    def _constructFiltering(self, filters, esModel, esSearch, lookupModel):
        for filterItem in filters:
            filterKey: str = filterItem["key"]
            filterValue = filterItem["value"]
            if filterKey != "_all":
                esModelAttributeData: EsModelAttributeData
                esModelAttributeData = esModel.attributeDataBySnakeCaseAttributeName(
                    instance=None, snakeCaseAttributeName=filterKey
                )
                esSearch = self._constructEsSearch(
                    attributeDataResultList=[{
                        "key": filterKey,
                        "dataType": esModelAttributeData.dataType,
                        "esModelAttributeData": esModelAttributeData
                    }],
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
                                    "esModelAttributeData": esModel.attributeDataBySnakeCaseAttributeName(
                                        snakeCaseAttributeName=item["key"]
                                    ),
                                }
                            )
                    else:
                        attributeDataResultList.append(
                            {
                                "key": modelKey,
                                "dataType": lookupModelAttributeData.dataType,
                                "esModelAttributeData": esModel.attributeDataBySnakeCaseAttributeName(
                                    snakeCaseAttributeName=modelKey
                                ),
                            }
                        )
                esSearch = self._constructEsSearch(
                    attributeDataResultList=attributeDataResultList, filterValue=filterValue, esSearch=esSearch
                )
        return esSearch

    @debugLogger
    def _constructEsSearch(self, attributeDataResultList: List[dict], filterValue, esSearch):
        queryList = []
        for attributeDataResult in attributeDataResultList:
            canAddAttributeDataToQuery = True
            # Make the query type to be 'wildcard'
            fieldQueryType = "wildcard"
            # if attributeDataResult["dataType"] is ObjectBase:
            #     queryList.append(self._constructEsSearch([attributeDataResult], filterValue, esSearch))
            #     canAddAttributeDataToQuery = False

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
                            path=attributeDataResult["esModelAttributeData"].attributeRepoName,
                            query=Q(fieldQueryType, **{filterKey: filterValue}),
                        )
                    )
                else:
                    queryList.append(Q(fieldQueryType, **{filterKey: filterValue}))
        return esSearch.query(Q("bool", should=queryList))

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
                    if type(esAttributeData.attributeRepoValue) is AttrList and esObject is not None:
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
