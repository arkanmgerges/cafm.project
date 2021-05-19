"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from elasticsearch_dsl import Document, Q

from src.port_adapter.repository.es_model.model.AttributeData import AttributeData
from src.resource.common.Util import Util
from src.resource.logging.decorator import debugLogger


class BaseLookupRepository:
    @debugLogger
    def lookup(self, *args, **kwargs):
        resultFrom = kwargs['resultFrom'] if 'resultFrom' in kwargs else 0
        resultSize = kwargs['resultSize'] if 'resultSize' in kwargs else 0
        orders = kwargs['orders'] if 'orders' in kwargs else []
        filters = kwargs['filters'] if 'filters' in kwargs else []
        esModel: Document = kwargs['esModel'] if 'esModel' in kwargs else None
        lookupModel = kwargs['lookupModel'] if 'lookupModel' in kwargs else None

        s = esModel.search()
        s = s[resultFrom: resultFrom + resultSize]
        for filterItem in filters:
            filterKey: str = filterItem['key']
            filterValue = filterItem['value']
            attributeData = esModel.attributeDataBySnakeCaseAttributeName(instance=None,
                                                                                  snakeCaseAttributeName=filterKey)
            fieldQueryType = 'wildcard'
            if attributeData.dataType == 'int':
                fieldQueryType = 'term'
            q = Q(fieldQueryType, **{attributeData.repoName: filterValue})
            if attributeData.repoName.find('.') != -1:
                s = s.query('nested', path=attributeData.repoName[:attributeData.repoName.rindex('.')], query=q)
            else:
                s = s.query(q)
        sortList = []
        for order in orders:
            attributeData = esModel.attributeDataBySnakeCaseAttributeName(instance=None,
                                                                                  snakeCaseAttributeName=order[
                                                                                      'orderBy'])
            if attributeData.repoName.find('.') != -1:
                sortList.append({
                    attributeData.repoName: {
                        "order": order['direction'],
                        "nested": {
                            "path": attributeData.repoName[:attributeData.repoName.rindex('.')]
                        }
                    }
                })
            else:
                sortList.append({attributeData.repoName: {"order": order['direction']}})
        s = s.sort(*sortList)
        esResults = s.execute()
        items = []

        for esResultItem in esResults:
            items.append(self._constructDomainModelObjectFromEsObject(lookupModel=lookupModel, esObject=esResultItem, esModel=esModel))

        return {'items': items, 'totalItemCount': esResults.hits.total.value}

    def _constructDomainModelObjectFromEsObject(self, lookupModel, esObject, esModel: Document):
        domainModelAttributes = lookupModel.attributes()
        kwargs = {}
        for attribute in domainModelAttributes:
            attributeData: AttributeData = esModel.attributeDataBySnakeCaseAttributeName(
                esObject, Util.camelCaseToLowerSnakeCase(attribute))
            kwargs[attribute] = attributeData.repoValue

        return lookupModel(**kwargs)