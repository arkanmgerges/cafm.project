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
from src.application.DailyCheckProcedureApplicationService import DailyCheckProcedureApplicationService
from src.application.DailyCheckProcedureOperationApplicationService import \
    DailyCheckProcedureOperationApplicationService
from src.application.DailyCheckProcedureOperationParameterApplicationService import \
    DailyCheckProcedureOperationParameterApplicationService
from src.application.EquipmentApplicationService import EquipmentApplicationService
from src.application.EquipmentCategoryApplicationService import EquipmentCategoryApplicationService
from src.application.EquipmentCategoryGroupApplicationService import EquipmentCategoryGroupApplicationService
from src.application.EquipmentInputApplicationService import EquipmentInputApplicationService
from src.application.EquipmentModelApplicationService import EquipmentModelApplicationService
from src.application.EquipmentProjectCategoryApplicationService import EquipmentProjectCategoryApplicationService
from src.application.MaintenanceProcedureApplicationService import MaintenanceProcedureApplicationService
from src.application.MaintenanceProcedureOperationApplicationService import \
    MaintenanceProcedureOperationApplicationService
from src.application.MaintenanceProcedureOperationParameterApplicationService import \
    MaintenanceProcedureOperationParameterApplicationService
from src.application.ManufacturerApplicationService import ManufacturerApplicationService
from src.application.OrganizationApplicationService import OrganizationApplicationService
from src.application.PolicyApplicationService import PolicyApplicationService
from src.application.ProjectApplicationService import ProjectApplicationService
from src.application.RoleApplicationService import RoleApplicationService
from src.application.SubcontractorApplicationService import SubcontractorApplicationService
from src.application.UnitApplicationService import UnitApplicationService
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
from src.domain_model.project.daily_check.procedure.DailyCheckProcedureRepository import DailyCheckProcedureRepository
from src.domain_model.project.daily_check.procedure.DailyCheckProcedureService import DailyCheckProcedureService
from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperationRepository import \
    DailyCheckProcedureOperationRepository
from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperationService import \
    DailyCheckProcedureOperationService
from src.domain_model.project.daily_check.procedure.operation.parameter.DailyCheckProcedureOperationParameterRepository import \
    DailyCheckProcedureOperationParameterRepository
from src.domain_model.project.daily_check.procedure.operation.parameter.DailyCheckProcedureOperationParameterService import \
    DailyCheckProcedureOperationParameterService
from src.domain_model.project.equipment.EquipmentRepository import EquipmentRepository
from src.domain_model.project.equipment.EquipmentService import EquipmentService
from src.domain_model.project.equipment.category.EquipmentCategoryRepository import EquipmentCategoryRepository
from src.domain_model.project.equipment.category.EquipmentCategoryService import EquipmentCategoryService
from src.domain_model.project.equipment.category.group.EquipmentCategoryGroupRepository import \
    EquipmentCategoryGroupRepository
from src.domain_model.project.equipment.category.group.EquipmentCategoryGroupService import \
    EquipmentCategoryGroupService
from src.domain_model.project.equipment.input.EquipmentInputRepository import EquipmentInputRepository
from src.domain_model.project.equipment.input.EquipmentInputService import EquipmentInputService
from src.domain_model.project.equipment.model.EquipmentModelRepository import EquipmentModelRepository
from src.domain_model.project.equipment.model.EquipmentModelService import EquipmentModelService
from src.domain_model.project.equipment.project_category.EquipmentProjectCategoryRepository import \
    EquipmentProjectCategoryRepository
from src.domain_model.project.equipment.project_category.EquipmentProjectCategoryService import \
    EquipmentProjectCategoryService
from src.domain_model.project.maintenance.procedure.MaintenanceProcedureRepository import MaintenanceProcedureRepository
from src.domain_model.project.maintenance.procedure.MaintenanceProcedureService import MaintenanceProcedureService
from src.domain_model.project.maintenance.procedure.operation.MaintenanceProcedureOperationRepository import \
    MaintenanceProcedureOperationRepository
from src.domain_model.project.maintenance.procedure.operation.MaintenanceProcedureOperationService import \
    MaintenanceProcedureOperationService
from src.domain_model.project.maintenance.procedure.operation.parameter.MaintenanceProcedureOperationParameterRepository import \
    MaintenanceProcedureOperationParameterRepository
from src.domain_model.project.maintenance.procedure.operation.parameter.MaintenanceProcedureOperationParameterService import \
    MaintenanceProcedureOperationParameterService
from src.domain_model.project.unit.UnitRepository import UnitRepository
from src.domain_model.project.unit.UnitService import UnitService
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
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.application.StandardMaintenanceProcedureApplicationService import StandardMaintenanceProcedureApplicationService
from src.domain_model.standard_maintenance_procedure.StandardMaintenanceProcedureRepository import StandardMaintenanceProcedureRepository
from src.domain_model.standard_maintenance_procedure.StandardMaintenanceProcedureService import StandardMaintenanceProcedureService
from src.application.SubcontractorCategoryApplicationService import SubcontractorCategoryApplicationService
from src.domain_model.subcontractor.category.SubcontractorCategoryRepository import SubcontractorCategoryRepository
from src.domain_model.subcontractor.category.SubcontractorCategoryService import SubcontractorCategoryService
from src.application.StandardEquipmentCategoryApplicationService import StandardEquipmentCategoryApplicationService
from src.domain_model.project.standard_equipment.standard_category.StandardEquipmentCategoryRepository import StandardEquipmentCategoryRepository
from src.domain_model.project.standard_equipment.standard_category.StandardEquipmentCategoryService import StandardEquipmentCategoryService
from src.application.StandardEquipmentCategoryGroupApplicationService import StandardEquipmentCategoryGroupApplicationService
from src.domain_model.project.standard_equipment.standard_category.standard_group.StandardEquipmentCategoryGroupRepository import StandardEquipmentCategoryGroupRepository
from src.domain_model.project.standard_equipment.standard_category.standard_group.StandardEquipmentCategoryGroupService import StandardEquipmentCategoryGroupService
from src.application.StandardEquipmentApplicationService import StandardEquipmentApplicationService
from src.domain_model.project.standard_equipment.StandardEquipmentRepository import StandardEquipmentRepository
from src.domain_model.project.standard_equipment.StandardEquipmentService import StandardEquipmentService


DbBase = DeclarativeMeta


class AppDi(Module):
    """
    Dependency injection module of the app

    """

    # region Application service
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
    def provideEquipmentCategoryApplicationService(self) -> EquipmentCategoryApplicationService:
        return EquipmentCategoryApplicationService(repo=self.__injector__.get(EquipmentCategoryRepository),
                                                   equipmentCategoryService=self.__injector__.get(
                                                       EquipmentCategoryService))

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
                                               orgRepo=self.__injector__.get(OrganizationRepository),
                                               subcontractorCategoryRepo=self.__injector__.get(SubcontractorCategoryRepository),
                                               domainService=self.__injector__.get(SubcontractorService))

    @singleton
    @provider
    def provideEquipmentModelApplicationService(self) -> EquipmentModelApplicationService:
        return EquipmentModelApplicationService(repo=self.__injector__.get(EquipmentModelRepository),
                                                equipmentModelService=self.__injector__.get(EquipmentModelService))

    @singleton
    @provider
    def provideManufacturerApplicationService(self) -> ManufacturerApplicationService:
        return ManufacturerApplicationService(repo=self.__injector__.get(ManufacturerRepository),
                                              manufacturerService=self.__injector__.get(ManufacturerService))

    @singleton
    @provider
    def provideEquipmentProjectCategoryApplicationService(self) -> EquipmentProjectCategoryApplicationService:
        return EquipmentProjectCategoryApplicationService(
            repo=self.__injector__.get(EquipmentProjectCategoryRepository),
            groupRepo=self.__injector__.get(EquipmentCategoryGroupRepository),
            equipmentProjectCategoryService=self.__injector__.get(EquipmentProjectCategoryService))

    @singleton
    @provider
    def provideEquipmentCategoryApplicationService(self) -> EquipmentCategoryApplicationService:
        return EquipmentCategoryApplicationService(repo=self.__injector__.get(EquipmentCategoryRepository),
                                                   equipmentCategoryService=self.__injector__.get(
                                                       EquipmentCategoryService))

    @singleton
    @provider
    def provideUnitApplicationService(self) -> UnitApplicationService:
        return UnitApplicationService(repo=self.__injector__.get(UnitRepository),
                                      unitService=self.__injector__.get(UnitService))

    @singleton
    @provider
    def provideEquipmentInputApplicationService(self) -> EquipmentInputApplicationService:
        return EquipmentInputApplicationService(repo=self.__injector__.get(EquipmentInputRepository),
                                                equipmentInputService=self.__injector__.get(EquipmentInputService))

    @singleton
    @provider
    def provideEquipmentCategoryGroupApplicationService(self) -> EquipmentCategoryGroupApplicationService:
        return EquipmentCategoryGroupApplicationService(repo=self.__injector__.get(EquipmentCategoryGroupRepository),
                                                        equipmentCategoryGroupService=self.__injector__.get(
                                                            EquipmentCategoryGroupService),
                                                        equipmentCategoryRepo=self.__injector__.get(EquipmentCategoryRepository),)

    @singleton
    @provider
    def provideEquipmentApplicationService(self) -> EquipmentApplicationService:
        return EquipmentApplicationService(repo=self.__injector__.get(EquipmentRepository),
                                           equipmentService=self.__injector__.get(EquipmentService),
                                           projectRepo=self.__injector__.get(ProjectRepository),
                                           equipmentProjectCategoryRepo=self.__injector__.get(
                                               EquipmentProjectCategoryRepository),
                                           equipmentCategoryRepo=self.__injector__.get(EquipmentCategoryRepository),
                                           equipmentCategoryGroupRepo=self.__injector__.get(
                                               EquipmentCategoryGroupRepository),
                                           buildingRepo=self.__injector__.get(BuildingRepository),
                                           buildingLevelRepo=self.__injector__.get(BuildingLevelRepository),
                                           buildingLevelRoomRepo=self.__injector__.get(BuildingLevelRoomRepository),
                                           manufacturerRepo=self.__injector__.get(ManufacturerRepository),
                                           equipmentModelRepo=self.__injector__.get(EquipmentModelRepository), )

    @singleton
    @provider
    def provideEquipmentInputApplicationService(self) -> EquipmentInputApplicationService:
        return EquipmentInputApplicationService(repo=self.__injector__.get(EquipmentInputRepository),
                                                equipmentInputService=self.__injector__.get(EquipmentInputService), )

    @singleton
    @provider
    def provideMaintenanceProcedureApplicationService(self) -> MaintenanceProcedureApplicationService:
        return MaintenanceProcedureApplicationService(repo=self.__injector__.get(MaintenanceProcedureRepository),
                                                      maintenanceProcedureService=self.__injector__.get(
                                                          MaintenanceProcedureService),
                                                      equipmentRepo=self.__injector__.get(EquipmentRepository), )

    @singleton
    @provider
    def provideMaintenanceProcedureOperationApplicationService(self) -> MaintenanceProcedureOperationApplicationService:
        return MaintenanceProcedureOperationApplicationService(
            repo=self.__injector__.get(MaintenanceProcedureOperationRepository),
            maintenanceProcedureOperationService=self.__injector__.get(MaintenanceProcedureOperationService),
            maintenanceProcedureRepo=self.__injector__.get(MaintenanceProcedureRepository), )

    @singleton
    @provider
    def provideMaintenanceProcedureOperationParameterApplicationService(
            self) -> MaintenanceProcedureOperationParameterApplicationService:
        return MaintenanceProcedureOperationParameterApplicationService(
            repo=self.__injector__.get(MaintenanceProcedureOperationParameterRepository),
            maintenanceProcedureOperationParameterService=self.__injector__.get(
                MaintenanceProcedureOperationParameterService),
            maintenanceProcedureOperationRepo=self.__injector__.get(MaintenanceProcedureOperationRepository), )

    @singleton
    @provider
    def provideProjectApplicationService(self) -> ProjectApplicationService:
        return ProjectApplicationService(repo=self.__injector__.get(ProjectRepository),
                                         projectService=self.__injector__.get(ProjectService), )

    @singleton
    @provider
    def provideDailyCheckProcedureOperationApplicationService(self) -> DailyCheckProcedureOperationApplicationService:
        return DailyCheckProcedureOperationApplicationService(
            repo=self.__injector__.get(DailyCheckProcedureOperationRepository),
            dailyCheckProcedureOperationService=self.__injector__.get(DailyCheckProcedureOperationService),
            dailyCheckProcedureRepo=self.__injector__.get(DailyCheckProcedureRepository), )

    @singleton
    @provider
    def provideDailyCheckProcedureApplicationService(self) -> DailyCheckProcedureApplicationService:
        return DailyCheckProcedureApplicationService(repo=self.__injector__.get(DailyCheckProcedureRepository),
                                                     dailyCheckProcedureService=self.__injector__.get(
                                                         DailyCheckProcedureService),
                                                     equipmentRepo=self.__injector__.get(EquipmentRepository),
                                                     equipmentCategoryGroupRepo=self.__injector__.get(
                                                         EquipmentCategoryGroupRepository), )

    @singleton
    @provider
    def provideDailyCheckProcedureOperationParameterApplicationService(
            self) -> DailyCheckProcedureOperationParameterApplicationService:
        return DailyCheckProcedureOperationParameterApplicationService(
            repo=self.__injector__.get(DailyCheckProcedureOperationParameterRepository),
            dailyCheckProcedureOperationParameterService=self.__injector__.get(
                DailyCheckProcedureOperationParameterService), unitRepo=self.__injector__.get(UnitRepository),
            dailyCheckProcedureOperationRepo=self.__injector__.get(DailyCheckProcedureOperationRepository), )

    @singleton
    @provider
    def provideStandardMaintenanceProcedureApplicationService(self) -> StandardMaintenanceProcedureApplicationService:
        return StandardMaintenanceProcedureApplicationService(repo=self.__injector__.get(StandardMaintenanceProcedureRepository), standardMaintenanceProcedureService=self.__injector__.get(StandardMaintenanceProcedureService), orgRepo=self.__injector__.get(OrganizationRepository), standardEquipmentCategoryGroupRepo=self.__injector__.get(StandardEquipmentCategoryGroupRepository),)

    @singleton
    @provider
    def provideSubcontractorCategoryApplicationService(self) -> SubcontractorCategoryApplicationService:
        return SubcontractorCategoryApplicationService(repo=self.__injector__.get(SubcontractorCategoryRepository), subcontractorCategoryService=self.__injector__.get(SubcontractorCategoryService),)

    @singleton
    @provider
    def provideStandardEquipmentCategoryApplicationService(self) -> StandardEquipmentCategoryApplicationService:
        return StandardEquipmentCategoryApplicationService(repo=self.__injector__.get(StandardEquipmentCategoryRepository), standardEquipmentCategoryService=self.__injector__.get(StandardEquipmentCategoryService),)

    @singleton
    @provider
    def provideStandardEquipmentApplicationService(self) -> StandardEquipmentApplicationService:
        return StandardEquipmentApplicationService(repo=self.__injector__.get(StandardEquipmentRepository), standardEquipmentService=self.__injector__.get(StandardEquipmentService),standardEquipmentCategoryRepo=self.__injector__.get(StandardEquipmentCategoryRepository),standardEquipmentCategoryGroupRepo=self.__injector__.get(StandardEquipmentCategoryGroupRepository),manufacturerRepo=self.__injector__.get(ManufacturerRepository),equipmentModelRepo=self.__injector__.get(EquipmentModelRepository),)


    @singleton
    @provider
    def provideStandardEquipmentCategoryGroupApplicationService(self) -> StandardEquipmentCategoryGroupApplicationService:
        return StandardEquipmentCategoryGroupApplicationService(repo=self.__injector__.get(StandardEquipmentCategoryGroupRepository), standardEquipmentCategoryGroupService=self.__injector__.get(StandardEquipmentCategoryGroupService),standardEquipmentCategoryRepo=self.__injector__.get(StandardEquipmentCategoryRepository),)

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
        from src.port_adapter.repository.project.equipment.model.EquipmentModelRepositoryImpl import \
            EquipmentModelRepositoryImpl
        return EquipmentModelRepositoryImpl()

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
    def provideUnitRepository(self) -> UnitRepository:
        from src.port_adapter.repository.project.unit.UnitRepositoryImpl import UnitRepositoryImpl
        return UnitRepositoryImpl()

    @singleton
    @provider
    def provideEquipmentInputRepository(self) -> EquipmentInputRepository:
        from src.port_adapter.repository.project.equipment.input.EquipmentInputRepositoryImpl import \
            EquipmentInputRepositoryImpl
        return EquipmentInputRepositoryImpl()

    @singleton
    @provider
    def provideMaintenanceProcedureRepository(self) -> MaintenanceProcedureRepository:
        from src.port_adapter.repository.project.maintenance.procedure.MaintenanceProcedureRepositoryImpl import \
            MaintenanceProcedureRepositoryImpl
        return MaintenanceProcedureRepositoryImpl()

    @singleton
    @provider
    def provideMaintenanceProcedureOperationRepository(self) -> MaintenanceProcedureOperationRepository:
        from src.port_adapter.repository.project.maintenance.procedure.operation.MaintenanceProcedureOperationRepositoryImpl import \
            MaintenanceProcedureOperationRepositoryImpl
        return MaintenanceProcedureOperationRepositoryImpl()

    @singleton
    @provider
    def provideMaintenanceProcedureOperationParameterRepository(
            self) -> MaintenanceProcedureOperationParameterRepository:
        from src.port_adapter.repository.project.maintenance.procedure.operation.parameter.MaintenanceProcedureOperationParameterRepositoryImpl import \
            MaintenanceProcedureOperationParameterRepositoryImpl
        return MaintenanceProcedureOperationParameterRepositoryImpl()

    @singleton
    @provider
    def provideDailyCheckProcedureRepository(self) -> DailyCheckProcedureRepository:
        from src.port_adapter.repository.project.daily_check.procedure.DailyCheckProcedureRepositoryImpl import \
            DailyCheckProcedureRepositoryImpl
        return DailyCheckProcedureRepositoryImpl()

    @singleton
    @provider
    def provideDailyCheckProcedureOperationRepository(self) -> DailyCheckProcedureOperationRepository:
        from src.port_adapter.repository.project.daily_check.procedure.operation.DailyCheckProcedureOperationRepositoryImpl import \
            DailyCheckProcedureOperationRepositoryImpl
        return DailyCheckProcedureOperationRepositoryImpl()

    @singleton
    @provider
    def provideDailyCheckProcedureOperationParameterRepository(self) -> DailyCheckProcedureOperationParameterRepository:
        from src.port_adapter.repository.project.daily_check.procedure.operation.parameter.DailyCheckProcedureOperationParameterRepositoryImpl import \
            DailyCheckProcedureOperationParameterRepositoryImpl
        return DailyCheckProcedureOperationParameterRepositoryImpl()

    @singleton
    @provider
    def provideStandardMaintenanceProcedureRepository(self) -> StandardMaintenanceProcedureRepository:
        from src.port_adapter.repository.standard_maintenance_procedure.StandardMaintenanceProcedureRepositoryImpl import StandardMaintenanceProcedureRepositoryImpl
        return StandardMaintenanceProcedureRepositoryImpl()

    @singleton
    @provider
    def provideSubcontractorCategoryRepository(self) -> SubcontractorCategoryRepository:
        from src.port_adapter.repository.subcontractor.category.SubcontractorCategoryRepositoryImpl import SubcontractorCategoryRepositoryImpl
        return SubcontractorCategoryRepositoryImpl()

    @singleton
    @provider
    def provideStandardEquipmentCategoryRepository(self) -> StandardEquipmentCategoryRepository:
        from src.port_adapter.repository.project.standard_equipment.standard_category.StandardEquipmentCategoryRepositoryImpl import StandardEquipmentCategoryRepositoryImpl
        return StandardEquipmentCategoryRepositoryImpl()

    @singleton
    @provider
    def provideStandardEquipmentCategoryGroupRepository(self) -> StandardEquipmentCategoryGroupRepository:
        from src.port_adapter.repository.project.standard_equipment.standard_category.standard_group.StandardEquipmentCategoryGroupRepositoryImpl import StandardEquipmentCategoryGroupRepositoryImpl
        return StandardEquipmentCategoryGroupRepositoryImpl()

    @singleton
    @provider
    def provideStandardEquipmentRepository(self) -> StandardEquipmentRepository:
        from src.port_adapter.repository.project.standard_equipment.StandardEquipmentRepositoryImpl import StandardEquipmentRepositoryImpl
        return StandardEquipmentRepositoryImpl()


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
                                    buildingRepo=self.__injector__.get(BuildingRepository))

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

    @singleton
    @provider
    def provideUnitService(self) -> UnitService:
        return UnitService(repository=self.__injector__.get(UnitRepository))

    @singleton
    @provider
    def provideEquipmentInputService(self) -> EquipmentInputService:
        return EquipmentInputService(repository=self.__injector__.get(EquipmentInputRepository))

    @singleton
    @provider
    def provideMaintenanceProcedureService(self) -> MaintenanceProcedureService:
        return MaintenanceProcedureService(repository=self.__injector__.get(MaintenanceProcedureRepository))

    @singleton
    @provider
    def provideMaintenanceProcedureOperationService(self) -> MaintenanceProcedureOperationService:
        return MaintenanceProcedureOperationService(
            repository=self.__injector__.get(MaintenanceProcedureOperationRepository))

    @singleton
    @provider
    def provideMaintenanceProcedureOperationParameterService(self) -> MaintenanceProcedureOperationParameterService:
        return MaintenanceProcedureOperationParameterService(
            repository=self.__injector__.get(MaintenanceProcedureOperationParameterRepository))

    @singleton
    @provider
    def provideDailyCheckProcedureService(self) -> DailyCheckProcedureService:
        return DailyCheckProcedureService(repository=self.__injector__.get(DailyCheckProcedureRepository))

    @singleton
    @provider
    def provideDailyCheckProcedureOperationService(self) -> DailyCheckProcedureOperationService:
        return DailyCheckProcedureOperationService(
            repository=self.__injector__.get(DailyCheckProcedureOperationRepository))

    @singleton
    @provider
    def provideDailyCheckProcedureOperationParameterService(self) -> DailyCheckProcedureOperationParameterService:
        return DailyCheckProcedureOperationParameterService(
            repository=self.__injector__.get(DailyCheckProcedureOperationParameterRepository))

    @singleton
    @provider
    def provideStandardMaintenanceProcedureService(self) -> StandardMaintenanceProcedureService:
        return StandardMaintenanceProcedureService(repository=self.__injector__.get(StandardMaintenanceProcedureRepository))

    @singleton
    @provider
    def provideSubcontractorCategoryService(self) -> SubcontractorCategoryService:
        return SubcontractorCategoryService(repository=self.__injector__.get(SubcontractorCategoryRepository))

    @singleton
    @provider
    def provideStandardEquipmentCategoryService(self) -> StandardEquipmentCategoryService:
        return StandardEquipmentCategoryService(repository=self.__injector__.get(StandardEquipmentCategoryRepository))

    @singleton
    @provider
    def provideStandardEquipmentCategoryGroupService(self) -> StandardEquipmentCategoryGroupService:
        return StandardEquipmentCategoryGroupService(repository=self.__injector__.get(StandardEquipmentCategoryGroupRepository))

    @singleton
    @provider
    def provideStandardEquipmentService(self) -> StandardEquipmentService:
        return StandardEquipmentService(repository=self.__injector__.get(StandardEquipmentRepository))

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

    # region Resource
    @singleton
    @provider
    def provideOpenTelemetry(self) -> OpenTelemetry:
        return OpenTelemetry()
    # endregion


class Builder:
    @classmethod
    def buildConsumer(cls, groupId: str = uuid4(), autoCommit: bool = False,
                      partitionEof: bool = True, autoOffsetReset: str = ConsumerOffsetReset.earliest.name) -> Consumer:
        builder = instance.get(ClassAssistedBuilder[KafkaConsumer])
        return builder.build(groupId=groupId, autoCommit=autoCommit, partitionEof=partitionEof,
                             autoOffsetReset=autoOffsetReset)


instance = Injector([AppDi])
