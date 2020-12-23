"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from uuid import uuid4

from injector import ClassAssistedBuilder
from injector import Module, Injector, singleton, provider
from sqlalchemy.ext.declarative.api import DeclarativeMeta, declarative_base

from src.application.ProjectApplicationService import ProjectApplicationService
from src.application.UserApplicationService import UserApplicationService
from src.domain_model.project.ProjectRepository import ProjectRepository
from src.domain_model.project.ProjectService import ProjectService
from src.domain_model.user.UserRepository import UserRepository
from src.domain_model.user.UserService import UserService
from src.port_adapter.messaging.common.Consumer import Consumer
from src.port_adapter.messaging.common.ConsumerOffsetReset import ConsumerOffsetReset
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.TransactionalProducer import TransactionalProducer
from src.port_adapter.messaging.common.kafka.KafkaConsumer import KafkaConsumer
from src.port_adapter.messaging.common.kafka.KafkaProducer import KafkaProducer

DbBase = DeclarativeMeta


class AppDi(Module):
    """
    Dependency injection module of the app

    """

    # region Application service
    @singleton
    @provider
    def provideProjectApplicationService(self) -> ProjectApplicationService:
        return ProjectApplicationService(repo=self.__injector__.get(ProjectRepository),
                                         projectService=self.__injector__.get(ProjectService))
 
    @singleton
    @provider
    def provideUserApplicationService(self) -> UserApplicationService:
        return UserApplicationService(repo=self.__injector__.get(UserRepository),
                                      userService=self.__injector__.get(UserService))

    # endregion

    # region Repository
    @singleton
    @provider
    def provideProjectRepository(self) -> ProjectRepository:
        from src.port_adapter.repository.project.ProjectRepositoryImpl import ProjectRepositoryImpl
        return ProjectRepositoryImpl()

    @singleton
    @provider
    def provideUserRepository(self) -> UserRepository:
        from src.port_adapter.repository.user.UserRepositoryImpl import UserRepositoryImpl
        return UserRepositoryImpl()
    # endregion

    # region Domain service
    @singleton
    @provider
    def provideProjectService(self) -> ProjectService:
        return ProjectService(projectRepo=self.__injector__.get(ProjectRepository))

    @singleton
    @provider
    def provideUserService(self) -> UserService:
        return UserService(userRepo=self.__injector__.get(UserRepository))
    # endregion

    # region Messaging
    @singleton
    @provider
    def provideSimpleProducer(self) -> SimpleProducer:
        return KafkaProducer.simpleProducer()

    @singleton
    @provider
    def provideTransactionalProducer(self) -> TransactionalProducer:
        return KafkaProducer.transactionalProducer()

    @singleton
    @provider
    def provideConsumer(self, groupId: str = uuid4(), autoCommit: bool = False,
                        partitionEof: bool = True,
                        autoOffsetReset: str = ConsumerOffsetReset.earliest.name) -> Consumer:
        return KafkaConsumer(groupId=groupId, autoCommit=autoCommit, partitionEof=partitionEof,
                             autoOffsetReset=autoOffsetReset)

    # endregion

    # region db
    @singleton
    @provider
    def provideDbBase(self) -> DbBase:
        return declarative_base()
    # endregion


class Builder:
    @classmethod
    def buildConsumer(cls, groupId: str = uuid4(), autoCommit: bool = False,
                      partitionEof: bool = True, autoOffsetReset: str = ConsumerOffsetReset.earliest.name) -> Consumer:
        builder = instance.get(ClassAssistedBuilder[KafkaConsumer])
        return builder.build(groupId=groupId, autoCommit=autoCommit, partitionEof=partitionEof,
                             autoOffsetReset=autoOffsetReset)


instance = Injector([AppDi])
