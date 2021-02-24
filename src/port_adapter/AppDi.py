"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from uuid import uuid4

from injector import ClassAssistedBuilder
from injector import Module, Injector, singleton, provider
from sqlalchemy.ext.declarative.api import DeclarativeMeta, declarative_base

from src.application.BuildingApplicationService import BuildingApplicationService
from src.application.BuildingLevelApplicationService import BuildingLevelApplicationService
from src.application.BuildingLevelRoomApplicationService import BuildingLevelRoomApplicationService
from src.application.EquipmentApplicationService import EquipmentApplicationService
from src.application.EquipmentCategoryApplicationService import EquipmentCategoryApplicationService
from src.application.EquipmentCategoryGroupApplicationService import EquipmentCategoryGroupApplicationService
from src.application.EquipmentProjectCategoryApplicationService import EquipmentProjectCategoryApplicationService
from src.application.ManufacturerApplicationService import ManufacturerApplicationService
from src.application.OrganizationApplicationService import OrganizationApplicationService
from src.application.PolicyApplicationService import PolicyApplicationService
from src.application.ProjectApplicationService import ProjectApplicationService
from src.application.RoleApplicationService import RoleApplicationService
from src.application.SubcontractorApplicationService import SubcontractorApplicationService
from src.application.UserApplicationService import UserApplicationService
from src.application.UserLookupApplicationService import UserLookupApplicationService
from src.application.user_lookup.UserLookupRepository import UserLookupRepository
from src.domain_model.manufacturer.ManufacturerRepository import ManufacturerRepository
from src.domain_model.manufacturer.ManufacturerService import ManufacturerService
from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.organization.OrganizationService import OrganizationService
from src.domain_model.policy.PolicyRepository import PolicyRepository
from src.domain_model.policy.PolicyService import PolicyService
from src.domain_model.project.ProjectRepository import ProjectRepository
from src.domain_model.project.ProjectService import ProjectService
from src.domain_model.project.building.BuildingRepository import BuildingRepository
from src.domain_model.project.building.BuildingService import BuildingService
from src.domain_model.project.building.level.BuildingLevelRepository import BuildingLevelRepository
from src.domain_model.project.building.level.BuildingLevelService import BuildingLevelService
from src.domain_model.project.building.level.room.BuildingLevelRoomRepository import BuildingLevelRoomRepository
from src.domain_model.project.building.level.room.BuildingLevelRoomService import BuildingLevelRoomService
from src.domain_model.project.equipment.EquipmentRepository import EquipmentRepository
from src.domain_model.project.equipment.EquipmentService import EquipmentService
from src.domain_model.project.equipment.category.EquipmentCategoryRepository import EquipmentCategoryRepository
from src.domain_model.project.equipment.category.EquipmentCategoryService import EquipmentCategoryService
from src.domain_model.project.equipment.category.group.EquipmentCategoryGroupRepository import \
    EquipmentCategoryGroupRepository
from src.domain_model.project.equipment.category.group.EquipmentCategoryGroupService import \
    EquipmentCategoryGroupService
from src.domain_model.project.equipment.model.EquipmentModelRepository import EquipmentModelRepository
from src.domain_model.project.equipment.model.EquipmentModelService import EquipmentModelService
from src.domain_model.project.equipment.project_category.EquipmentProjectCategoryRepository import \
    EquipmentProjectCategoryRepository
from src.domain_model.project.equipment.project_category.EquipmentProjectCategoryService import \
    EquipmentProjectCategoryService
from src.domain_model.role.RoleRepository import RoleRepository
from src.domain_model.role.RoleService import RoleService
from src.domain_model.subcontractor.SubcontractorRepository import SubcontractorRepository
from src.domain_model.subcontractor.SubcontractorService import SubcontractorService
from src.domain_model.user.UserRepository import UserRepository
from src.domain_model.user.UserService import UserService
from src.port_adapter.messaging.common.Consumer import Consumer
from src.port_adapter.messaging.common.ConsumerOffsetReset import ConsumerOffsetReset
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.TransactionalProducer import TransactionalProducer
from src.port_adapter.messaging.common.kafka.KafkaConsumer import KafkaConsumer
from src.port_adapter.messaging.common.kafka.KafkaProducer import KafkaProducer

from src.application.EquipmentModelApplicationService import EquipmentModelApplicationService
from src.domain_model.project.equipment.model.EquipmentModelRepository import EquipmentModelRepository
from src.domain_model.project.equipment.model.EquipmentModelService import EquipmentModelService

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

    @singleton
    @provider
    def provideBuildingLevelApplicationService(self) -> BuildingLevelApplicationService:
        return BuildingLevelApplicationService(repo=self.__injector__.get(BuildingLevelRepository),
                                               buildingLevelService=self.__injector__.get(BuildingLevelService),
                                               buildingRepo=self.__injector__.get(BuildingRepository))

    @singleton
    @provider
    def provideBuildingLevelRoomApplicationService(self) -> BuildingLevelRoomApplicationService:
        return BuildingLevelRoomApplicationService(repo=self.__injector__.get(BuildingLevelRoomRepository),
                                                   buildingLevelRoomService=self.__injector__.get(
                                                       BuildingLevelRoomService),
                                                   buildingLevelRepository=self.__injector__.get(
                                                       BuildingLevelRepository))

    @singleton
    @provider
    def provideEquipmentApplicationService(self) -> EquipmentApplicationService:
        return EquipmentApplicationService(repo=self.__injector__.get(EquipmentRepository),
                                           equipmentService=self.__injector__.get(
                                               EquipmentService))

    @singleton
    @provider
    def provideEquipmentCategoryApplicationService(self) -> EquipmentCategoryApplicationService:
        return EquipmentCategoryApplicationService(repo=self.__injector__.get(EquipmentCategoryRepository),
                                                   equipmentCategoryService=self.__injector__.get(
                                                       EquipmentCategoryService))

    @singleton
    @provider
    def provideEquipmentCategoryGroupApplicationService(self) -> EquipmentCategoryGroupApplicationService:
        return EquipmentCategoryGroupApplicationService(repo=self.__injector__.get(EquipmentCategoryGroupRepository),
                                                        equipmentCategoryGroupService=self.__injector__.get(
                                                            EquipmentCategoryGroupService))

    @singleton
    @provider
    def provideEquipmentProjectCategoryApplicationService(self) -> EquipmentProjectCategoryApplicationService:
        return EquipmentProjectCategoryApplicationService(
            repo=self.__injector__.get(EquipmentProjectCategoryRepository),
            equipmentProjectCategoryService=self.__injector__.get(
                EquipmentProjectCategoryService))

    @singleton
    @provider
    def provideManufacturerApplicationService(self) -> ManufacturerApplicationService:
        return ManufacturerApplicationService(repo=self.__injector__.get(ManufacturerRepository),
                                              manufacturerService=self.__injector__.get(
                                                  ManufacturerService))

    @singleton
    @provider
    def provideSubcontractorApplicationService(self) -> SubcontractorApplicationService:
        return SubcontractorApplicationService(repo=self.__injector__.get(SubcontractorRepository),
                                               domainService=self.__injector__.get(SubcontractorService))

    @singleton
    @provider
    def provideEquipmentModelApplicationService(self) -> EquipmentModelApplicationService:
        return EquipmentModelApplicationService(repo=self.__injector__.get(EquipmentModelRepository), equipmentModelService=self.__injector__.get(EquipmentModelService))

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

    @singleton
    @provider
    def provideBuildingLevelRepository(self) -> BuildingLevelRepository:
        from src.port_adapter.repository.project.building.level.BuildingLevelRepositoryImpl import \
            BuildingLevelRepositoryImpl
        return BuildingLevelRepositoryImpl()

    @singleton
    @provider
    def provideBuildingLevelRoomRepository(self) -> BuildingLevelRoomRepository:
        from src.port_adapter.repository.project.building.level.room.BuildingLevelRoomRepositoryImpl import \
            BuildingLevelRoomRepositoryImpl
        return BuildingLevelRoomRepositoryImpl()

    @singleton
    @provider
    def provideEquipmentProjectCategoryRepository(self) -> EquipmentProjectCategoryRepository:
        from src.port_adapter.repository.project.equipment.project_category.EquipmentProjectCategoryRepositoryImpl import \
            EquipmentProjectCategoryRepositoryImpl
        return EquipmentProjectCategoryRepositoryImpl()

    @singleton
    @provider
    def provideEquipmentCategoryRepository(self) -> EquipmentCategoryRepository:
        from src.port_adapter.repository.project.equipment.category.EquipmentCategoryRepositoryImpl import \
            EquipmentCategoryRepositoryImpl
        return EquipmentCategoryRepositoryImpl()

    @singleton
    @provider
    def provideEquipmentCategoryGroupRepository(self) -> EquipmentCategoryGroupRepository:
        from src.port_adapter.repository.project.equipment.category.group.EquipmentCategoryGroupRepositoryImpl import \
            EquipmentCategoryGroupRepositoryImpl
        return EquipmentCategoryGroupRepositoryImpl()

    @singleton
    @provider
    def provideEquipmentModelRepository(self) -> EquipmentModelRepository:
        from src.port_adapter.repository.project.equipment.model.EquipmentModelRepositoryImpl import \
            EquipmentModelRepositoryImpl
        return EquipmentModelRepositoryImpl()

    @singleton
    @provider
    def provideManufacturerRepository(self) -> ManufacturerRepository:
        from src.port_adapter.repository.manufacturer.ManufacturerRepositoryImpl import ManufacturerRepositoryImpl
        return ManufacturerRepositoryImpl()

    @singleton
    @provider
    def provideEquipmentRepository(self) -> EquipmentRepository:
        from src.port_adapter.repository.project.equipment.EquipmentRepositoryImpl import EquipmentRepositoryImpl
        return EquipmentRepositoryImpl()

    @singleton
    @provider
    def provideSubcontractorRepository(self) -> SubcontractorRepository:
        from src.port_adapter.repository.subcontractor.SubcontractorRepositoryImpl import SubcontractorRepositoryImpl
        return SubcontractorRepositoryImpl()

    @singleton
    @provider
    def provideEquipmentModelRepository(self) -> EquipmentModelRepository:
        from src.port_adapter.repository.project.equipment.model.EquipmentModelRepositoryImpl import EquipmentModelRepositoryImpl
        return EquipmentModelRepositoryImpl()

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

    @singleton
    @provider
    def provideBuildingLevelService(self) -> BuildingLevelService:
        return BuildingLevelService(buildingLevelRepo=self.__injector__.get(BuildingLevelRepository),
                                    buildingRepo=self.__injector__.get(BuildingLevelRepository))

    @singleton
    @provider
    def provideBuildingLevelRoomService(self) -> BuildingLevelRoomService:
        return BuildingLevelRoomService(buildingLevelRoomRepo=self.__injector__.get(BuildingLevelRoomRepository),
                                        buildingLevelRepo=self.__injector__.get(BuildingLevelRepository))

    @singleton
    @provider
    def provideBuildingLevelRoomService(self) -> BuildingLevelRoomService:
        return BuildingLevelRoomService(buildingLevelRoomRepo=self.__injector__.get(BuildingLevelRoomRepository),
                                        buildingLevelRepo=self.__injector__.get(BuildingLevelRepository))

    @singleton
    @provider
    def provideEquipmentService(self) -> EquipmentService:
        return EquipmentService(repository=self.__injector__.get(EquipmentRepository))

    @singleton
    @provider
    def provideEquipmentCategoryService(self) -> EquipmentCategoryService:
        return EquipmentCategoryService(repository=self.__injector__.get(EquipmentCategoryRepository))

    @singleton
    @provider
    def provideEquipmentCategoryGroupService(self) -> EquipmentCategoryGroupService:
        return EquipmentCategoryGroupService(repository=self.__injector__.get(EquipmentCategoryGroupRepository))

    @singleton
    @provider
    def provideEquipmentModelService(self) -> EquipmentModelService:
        return EquipmentModelService(repository=self.__injector__.get(EquipmentModelRepository))

    @singleton
    @provider
    def provideEquipmentProjectCategoryService(self) -> EquipmentProjectCategoryService:
        return EquipmentProjectCategoryService(repository=self.__injector__.get(EquipmentProjectCategoryRepository))

    @singleton
    @provider
    def provideManufacturerService(self) -> ManufacturerService:
        return ManufacturerService(repository=self.__injector__.get(ManufacturerRepository))

    @singleton
    @provider
    def provideSubcontractorService(self) -> SubcontractorService:
        return SubcontractorService(subcontractorRepo=self.__injector__.get(SubcontractorRepository))

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
