"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


from uuid import uuid4

from injector import ClassAssistedBuilder
from injector import Module, Injector, singleton, provider

class AppDi(Module):
    pass



class Builder:
    @classmethod
    def buildConsumer(cls, groupId: str = uuid4(), autoCommit: bool = False,
                      partitionEof: bool = True, autoOffsetReset: str = ConsumerOffsetReset.earliest.name) -> Consumer:
        builder = instance.get(ClassAssistedBuilder[KafkaConsumer])
        return builder.build(groupId=groupId, autoCommit=autoCommit, partitionEof=partitionEof,
                             autoOffsetReset=autoOffsetReset)


instance = Injector([AppDi])