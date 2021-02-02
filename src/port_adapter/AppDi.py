"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from uuid import uuid4

from injector import ClassAssistedBuilder
from injector import Module, Injector, singleton, provider
from sqlalchemy.ext.declarative.api import DeclarativeMeta, declarative_base

from src.application.BuildingApplicationService import BuildingApplicationService
from src.application.OrganizationApplicationService import OrganizationApplicationService
from src.application.PolicyApplicationService import PolicyApplicationService
from src.application.ProjectApplicationService import ProjectApplicationService
from src.application.RoleApplicationService import RoleApplicationService
from src.application.UserApplicationService import UserApplicationService
from src.application.UserLookupApplicationService import UserLookupApplicationService
from src.application.user_lookup.UserLookupRepository import UserLookupRepository
from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.organization.OrganizationService import OrganizationService
from src.domain_model.policy.PolicyRepository import PolicyRepository
from src.domain_model.policy.PolicyService import PolicyService
from src.domain_model.project.ProjectRepository import ProjectRepository
from src.domain_model.project.ProjectService import ProjectService
from src.domain_model.project.building.BuildingRepository import BuildingRepository
from src.domain_model.project.building.BuildingService import BuildingService
from src.domain_model.role.RoleRepository import RoleRepository
from src.domain_model.role.RoleService import RoleService
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

    @singleton
    @provider
    def provideOrganizationApplicationService(self) -> OrganizationApplicationService:
        return OrganizationApplicationService(repo=self.__injector__.get(OrganizationRepository),
                                              domainService=self.__injector__.get(OrganizationService))

    @singleton
    @provider
    def provideRoleApplicationService(self) -> RoleApplicationService:
        return RoleApplicationService(repo=self.__injector__.get(RoleRepository),
                                      domainService=self.__injector__.get(RoleService))

    @singleton
    @provider
    def providePolicyApplicationService(self) -> PolicyApplicationService:
        return PolicyApplicationService(repo=self.__injector__.get(PolicyRepository),
                                        policyService=self.__injector__.get(PolicyService),
                                        userRepo=self.__injector__.get(UserRepository),
                                        roleRepo=self.__injector__.get(RoleRepository),
                                        organizationRepo=self.__injector__.get(OrganizationRepository))

    @singleton
    @provider
    def provideUserLookupApplicationService(self) -> UserLookupApplicationService:
        return UserLookupApplicationService(repo=self.__injector__.get(UserLookupRepository))

    @singleton
    @provider
    def provideBuildingApplicationService(self) -> BuildingApplicationService:
        return BuildingApplicationService(repo=self.__injector__.get(BuildingRepository),
                                          buildingService=self.__injector__.get(BuildingService))
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

    @singleton
    @provider
    def provideOrganizationRepository(self) -> OrganizationRepository:
        from src.port_adapter.repository.organization.OrganizationRepositoryImpl import OrganizationRepositoryImpl
        return OrganizationRepositoryImpl()

    @singleton
    @provider
    def provideRoleRepository(self) -> RoleRepository:
        from src.port_adapter.repository.role.RoleRepositoryImpl import RoleRepositoryImpl
        return RoleRepositoryImpl()

    @singleton
    @provider
    def providePolicyRepository(self) -> PolicyRepository:
        from src.port_adapter.repository.policy.PolicyRepositoryImpl import PolicyRepositoryImpl
        return PolicyRepositoryImpl()

    @singleton
    @provider
    def provideUserLookupRepository(self) -> UserLookupRepository:
        from src.port_adapter.repository.application.user_lookup.UserLookupRepositoryImpl import \
            UserLookupRepositoryImpl
        return UserLookupRepositoryImpl()

    @singleton
    @provider
    def provideBuildingRepository(self) -> BuildingRepository:
        from src.port_adapter.repository.project.building.BuildingRepositoryImpl import BuildingRepositoryImpl
        return BuildingRepositoryImpl()
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

    @singleton
    @provider
    def provideOrganizationService(self) -> OrganizationService:
        return OrganizationService(organizationRepo=self.__injector__.get(OrganizationRepository))

    @singleton
    @provider
    def provideRoleService(self) -> RoleService:
        return RoleService(roleRepo=self.__injector__.get(RoleRepository))

    @singleton
    @provider
    def providePolicyService(self) -> PolicyService:
        return PolicyService(policyRepo=self.__injector__.get(PolicyRepository))

    @singleton
    @provider
    def provideBuildingService(self) -> BuildingService:
        return BuildingService(buildingRepo=self.__injector__.get(BuildingRepository))
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
