"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from uuid import uuid4

from injector import ClassAssistedBuilder
from injector import Module, Injector, singleton, provider
from sqlalchemy.ext.declarative.api import DeclarativeMeta, declarative_base

from src.application.BuildingApplicationService import BuildingApplicationService
from src.application.BuildingLevelApplicationService import (
    BuildingLevelApplicationService,
)
from src.application.BuildingLevelRoomApplicationService import (
    BuildingLevelRoomApplicationService,
)
from src.application.CityApplicationService import CityApplicationService
from src.application.CountryApplicationService import CountryApplicationService
from src.application.DailyCheckProcedureApplicationService import (
    DailyCheckProcedureApplicationService,
)
from src.application.DailyCheckProcedureOperationApplicationService import (
    DailyCheckProcedureOperationApplicationService,
)
from src.application.DailyCheckProcedureOperationParameterApplicationService import (
    DailyCheckProcedureOperationParameterApplicationService,
)
from src.application.EquipmentApplicationService import EquipmentApplicationService
from src.application.EquipmentCategoryGroupApplicationService import (
    EquipmentCategoryGroupApplicationService,
)
from src.application.EquipmentInputApplicationService import (
    EquipmentInputApplicationService,
)
from src.application.EquipmentModelApplicationService import (
    EquipmentModelApplicationService,
)
from src.application.EquipmentProjectCategoryApplicationService import (
    EquipmentProjectCategoryApplicationService,
)
from src.application.MaintenanceProcedureApplicationService import (
    MaintenanceProcedureApplicationService,
)
from src.application.MaintenanceProcedureOperationApplicationService import (
    MaintenanceProcedureOperationApplicationService,
)
from src.application.MaintenanceProcedureOperationParameterApplicationService import (
    MaintenanceProcedureOperationParameterApplicationService,
)
from src.application.ManufacturerApplicationService import (
    ManufacturerApplicationService,
)
from src.application.OrganizationApplicationService import (
    OrganizationApplicationService,
)
from src.application.PolicyApplicationService import PolicyApplicationService
from src.application.ProjectApplicationService import ProjectApplicationService
from src.application.RoleApplicationService import RoleApplicationService
from src.application.StandardEquipmentApplicationService import (
    StandardEquipmentApplicationService,
)
from src.application.StandardEquipmentCategoryApplicationService import (
    StandardEquipmentCategoryApplicationService,
)
from src.application.StandardEquipmentCategoryGroupApplicationService import (
    StandardEquipmentCategoryGroupApplicationService,
)
from src.application.StandardMaintenanceProcedureApplicationService import (
    StandardMaintenanceProcedureApplicationService,
)
from src.application.SubcontractorApplicationService import (
    SubcontractorApplicationService,
)
from src.application.SubcontractorCategoryApplicationService import (
    SubcontractorCategoryApplicationService,
)
from src.application.UnitApplicationService import UnitApplicationService
from src.application.UserApplicationService import UserApplicationService
from src.application.UserLookupApplicationService import UserLookupApplicationService
from src.application.lifecycle.BaseDbContainer import BaseDbContainer
from src.application.lookup.daily_check_procedure.DailyCheckProcedureApplicationService import \
    DailyCheckProcedureApplicationService as Lookup__DailyCheckProcedure__DailyCheckProcedureApplicationService
from src.application.lookup.daily_check_procedure.DailyCheckProcedureOperationApplicationService import \
    DailyCheckProcedureOperationApplicationService as Lookup__DailyCheckProcedureOperation__DailyCheckProcedureOperationApplicationService
from src.application.lookup.daily_check_procedure.DailyCheckProcedureOperationParameterApplicationService import \
    DailyCheckProcedureOperationParameterApplicationService as Lookup__DailyCheckProcedureOperationParameter__DailyCheckProcedureOperationParameterApplicationService
from src.application.lookup.daily_check_procedure.DailyCheckProcedureOperationParameterRepository import \
    DailyCheckProcedureOperationParameterRepository as Lookup__DailyCheckProcedureOperationParameter__DailyCheckProcedureOperationParameterRepository
from src.application.lookup.daily_check_procedure.DailyCheckProcedureOperationRepository import \
    DailyCheckProcedureOperationRepository as Lookup__DailyCheckProcedureOperation__DailyCheckProcedureOperationRepository
from src.application.lookup.daily_check_procedure.DailyCheckProcedureRepository import \
    DailyCheckProcedureRepository as Lookup__DailyCheckProcedure__DailyCheckProcedureRepository
from src.application.lookup.daily_check_procedure.EquipmentCategoryGroupApplicationService import \
    EquipmentCategoryGroupApplicationService as Lookup__EquipmentCategoryGroup__EquipmentCategoryGroupApplicationService
from src.application.lookup.daily_check_procedure.EquipmentCategoryGroupRepository import \
    EquipmentCategoryGroupRepository as Lookup__EquipmentCategoryGroup__EquipmentCategoryGroupRepository
from src.application.lookup.daily_check_procedure.UnitApplicationService import \
    UnitApplicationService as Lookup__Unit__UnitApplicationService
from src.application.lookup.daily_check_procedure.UnitRepository import UnitRepository as Lookup__Unit__UnitRepository
from src.application.lookup.equipment.BuildingApplicationService import \
    BuildingApplicationService as Lookup__Equipment__BuildingApplicationService
from src.application.lookup.equipment.BuildingLevelApplicationService import \
    BuildingLevelApplicationService as Lookup__Equipment__BuildingLevelApplicationService
from src.application.lookup.equipment.BuildingLevelRepository import \
    BuildingLevelRepository as Lookup__Equipment__BuildingLevelRepository
from src.application.lookup.equipment.BuildingLevelRoomApplicationService import \
    BuildingLevelRoomApplicationService as Lookup__Equipment__BuildingLevelRoomApplicationService
from src.application.lookup.equipment.BuildingLevelRoomRepository import \
    BuildingLevelRoomRepository as Lookup__Equipment__BuildingLevelRoomRepository
from src.application.lookup.equipment.BuildingRepository import \
    BuildingRepository as Lookup__Equipment__BuildingRepository
from src.application.lookup.equipment.EquipmentCategoryGroupApplicationService import \
    EquipmentCategoryGroupApplicationService as Lookup__Equipment__EquipmentCategoryGroupApplicationService
from src.application.lookup.equipment.EquipmentCategoryGroupRepository import \
    EquipmentCategoryGroupRepository as Lookup__Equipment__EquipmentCategoryGroupRepository
from src.application.lookup.equipment.EquipmentLookupApplicationService import (
    EquipmentLookupApplicationService as Lookup__Equipment__EquipmentLookupApplicationService,
)
from src.application.lookup.equipment.EquipmentLookupRepository import (
    EquipmentLookupRepository as Lookup__Equipment__EquipmentLookupRepository,
)
from src.application.lookup.equipment.EquipmentModelApplicationService import \
    EquipmentModelApplicationService as Lookup__Equipment__EquipmentModelApplicationService
from src.application.lookup.equipment.EquipmentModelRepository import \
    EquipmentModelRepository as Lookup__Equipment__EquipmentModelRepository
from src.application.lookup.equipment.EquipmentProjectCategoryApplicationService import \
    EquipmentProjectCategoryApplicationService as Lookup__Equipment__EquipmentProjectCategoryApplicationService
from src.application.lookup.equipment.EquipmentProjectCategoryRepository import \
    EquipmentProjectCategoryRepository as Lookup__Equipment__EquipmentProjectCategoryRepository
from src.application.lookup.equipment.MaintenanceProcedureApplicationService import (
    MaintenanceProcedureApplicationService as Lookup__Equipment__MaintenanceProcedureApplicationService,
)
from src.application.lookup.equipment.MaintenanceProcedureOperationApplicationService import (
    MaintenanceProcedureOperationApplicationService as Lookup__Equipment__MaintenanceProcedureOperationApplicationService,
)
from src.application.lookup.equipment.MaintenanceProcedureOperationParameterApplicationService import (
    MaintenanceProcedureOperationParameterApplicationService as Lookup__Equipment__MaintenanceProcedureOperationParameterApplicationService,
)
from src.application.lookup.equipment.MaintenanceProcedureOperationParameterRepository import (
    MaintenanceProcedureOperationParameterRepository as Lookup__Equipment__MaintenanceProcedureOperationParameterRepository,
)
from src.application.lookup.equipment.MaintenanceProcedureOperationRepository import (
    MaintenanceProcedureOperationRepository as Lookup__Equipment__MaintenanceProcedureOperationRepository,
)
from src.application.lookup.equipment.MaintenanceProcedureRepository import (
    MaintenanceProcedureRepository as Lookup__Equipment__MaintenanceProcedureRepository,
)
from src.application.lookup.equipment.ManufacturerApplicationService import \
    ManufacturerApplicationService as Lookup__Equipment__ManufacturerApplicationService
from src.application.lookup.equipment.ManufacturerRepository import \
    ManufacturerRepository as Lookup__Equipment__ManufacturerRepository
from src.application.lookup.equipment.ProjectApplicationService import \
    ProjectApplicationService as Lookup__Equipment__ProjectApplicationService
from src.application.lookup.equipment.ProjectRepository import ProjectRepository as Lookup__Equipment__ProjectRepository
from src.application.lookup.equipment.UnitApplicationService import \
    UnitApplicationService as Lookup__Equipment__UnitApplicationService
from src.application.lookup.equipment.UnitRepository import UnitRepository as Lookup__Equipment__UnitRepository
from src.application.lookup.subcontractor.SubcontractorCategoryApplicationService import (
    SubcontractorCategoryApplicationService as Lookup__Equipment__SubcontractorCategoryApplicationService,
)
from src.application.lookup.subcontractor.SubcontractorCategoryRepository import (
    SubcontractorCategoryRepository as Lookup__Equipment__SubcontractorCategoryRepository,
)
from src.application.lookup.subcontractor.SubcontractorLookupApplicationService import (
    SubcontractorLookupApplicationService as Lookup__Equipment__SubcontractorLookupApplicationService,
)
from src.application.lookup.subcontractor.SubcontractorLookupRepository import (
    SubcontractorLookupRepository as Lookup__Equipment__SubcontractorLookupRepository,
)
from src.application.lookup.user.UserLookupRepository import UserLookupRepository
from src.domain_model.city.CityRepository import CityRepository
from src.domain_model.country.CountryRepository import CountryRepository
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
from src.domain_model.project.building.level.BuildingLevelRepository import (
    BuildingLevelRepository,
)
from src.domain_model.project.building.level.BuildingLevelService import (
    BuildingLevelService,
)
from src.domain_model.project.building.level.room.BuildingLevelRoomRepository import (
    BuildingLevelRoomRepository,
)
from src.domain_model.project.building.level.room.BuildingLevelRoomService import (
    BuildingLevelRoomService,
)
from src.domain_model.project.daily_check.procedure.DailyCheckProcedureRepository import (
    DailyCheckProcedureRepository,
)
from src.domain_model.project.daily_check.procedure.DailyCheckProcedureService import (
    DailyCheckProcedureService,
)
from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperationRepository import (
    DailyCheckProcedureOperationRepository,
)
from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperationService import (
    DailyCheckProcedureOperationService,
)
from src.domain_model.project.daily_check.procedure.operation.parameter.DailyCheckProcedureOperationParameterRepository import (
    DailyCheckProcedureOperationParameterRepository,
)
from src.domain_model.project.daily_check.procedure.operation.parameter.DailyCheckProcedureOperationParameterService import (
    DailyCheckProcedureOperationParameterService,
)
from src.domain_model.project.equipment.EquipmentRepository import EquipmentRepository
from src.domain_model.project.equipment.EquipmentService import EquipmentService
from src.domain_model.project.equipment.category.group.EquipmentCategoryGroupRepository import (
    EquipmentCategoryGroupRepository,
)
from src.domain_model.project.equipment.category.group.EquipmentCategoryGroupService import (
    EquipmentCategoryGroupService,
)
from src.domain_model.project.equipment.input.EquipmentInputRepository import (
    EquipmentInputRepository,
)
from src.domain_model.project.equipment.input.EquipmentInputService import (
    EquipmentInputService,
)
from src.domain_model.project.equipment.model.EquipmentModelRepository import (
    EquipmentModelRepository,
)
from src.domain_model.project.equipment.model.EquipmentModelService import (
    EquipmentModelService,
)
from src.domain_model.project.equipment.project_category.EquipmentProjectCategoryRepository import (
    EquipmentProjectCategoryRepository,
)
from src.domain_model.project.equipment.project_category.EquipmentProjectCategoryService import (
    EquipmentProjectCategoryService,
)
from src.domain_model.project.maintenance.procedure.MaintenanceProcedureRepository import (
    MaintenanceProcedureRepository,
)
from src.domain_model.project.maintenance.procedure.MaintenanceProcedureService import (
    MaintenanceProcedureService,
)
from src.domain_model.project.maintenance.procedure.operation.MaintenanceProcedureOperationRepository import (
    MaintenanceProcedureOperationRepository,
)
from src.domain_model.project.maintenance.procedure.operation.MaintenanceProcedureOperationService import (
    MaintenanceProcedureOperationService,
)
from src.domain_model.project.maintenance.procedure.operation.parameter.MaintenanceProcedureOperationParameterRepository import (
    MaintenanceProcedureOperationParameterRepository,
)
from src.domain_model.project.maintenance.procedure.operation.parameter.MaintenanceProcedureOperationParameterService import (
    MaintenanceProcedureOperationParameterService,
)
from src.domain_model.project.standard_equipment.StandardEquipmentRepository import (
    StandardEquipmentRepository,
)
from src.domain_model.project.standard_equipment.StandardEquipmentService import (
    StandardEquipmentService,
)
from src.domain_model.project.standard_equipment.standard_category.StandardEquipmentCategoryRepository import (
    StandardEquipmentCategoryRepository,
)
from src.domain_model.project.standard_equipment.standard_category.StandardEquipmentCategoryService import (
    StandardEquipmentCategoryService,
)
from src.domain_model.project.standard_equipment.standard_category.standard_group.StandardEquipmentCategoryGroupRepository import (
    StandardEquipmentCategoryGroupRepository,
)
from src.domain_model.project.standard_equipment.standard_category.standard_group.StandardEquipmentCategoryGroupService import (
    StandardEquipmentCategoryGroupService,
)
from src.domain_model.project.unit.UnitRepository import UnitRepository
from src.domain_model.project.unit.UnitService import UnitService
from src.domain_model.role.RoleRepository import RoleRepository
from src.domain_model.role.RoleService import RoleService
from src.domain_model.standard_maintenance_procedure.StandardMaintenanceProcedureRepository import (
    StandardMaintenanceProcedureRepository,
)
from src.domain_model.standard_maintenance_procedure.StandardMaintenanceProcedureService import (
    StandardMaintenanceProcedureService,
)
from src.domain_model.subcontractor.SubcontractorRepository import (
    SubcontractorRepository,
)
from src.domain_model.subcontractor.SubcontractorService import SubcontractorService
from src.domain_model.subcontractor.category.SubcontractorCategoryRepository import (
    SubcontractorCategoryRepository,
)
from src.domain_model.subcontractor.category.SubcontractorCategoryService import (
    SubcontractorCategoryService,
)
from src.domain_model.user.UserRepository import UserRepository
from src.domain_model.user.UserService import UserService
from src.port_adapter.messaging.common.Consumer import Consumer
from src.port_adapter.messaging.common.ConsumerOffsetReset import ConsumerOffsetReset
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.TransactionalProducer import (
    TransactionalProducer,
)
from src.port_adapter.messaging.common.kafka.KafkaConsumer import KafkaConsumer
from src.port_adapter.messaging.common.kafka.KafkaProducer import KafkaProducer
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

DbBase = DeclarativeMeta


class AppDi(Module):
    """
    Dependency injection module of the app

    """

    # region Application service
    @singleton
    @provider
    def provideUserApplicationService(self) -> UserApplicationService:
        return UserApplicationService(
            repo=self.__injector__.get(UserRepository),
            userService=self.__injector__.get(UserService),
        )

    @singleton
    @provider
    def provideOrganizationApplicationService(self) -> OrganizationApplicationService:
        return OrganizationApplicationService(
            repo=self.__injector__.get(OrganizationRepository),
            domainService=self.__injector__.get(OrganizationService),
        )

    @singleton
    @provider
    def provideRoleApplicationService(self) -> RoleApplicationService:
        return RoleApplicationService(
            repo=self.__injector__.get(RoleRepository),
            roleService=self.__injector__.get(RoleService),
        )

    @singleton
    @provider
    def providePolicyApplicationService(self) -> PolicyApplicationService:
        return PolicyApplicationService(
            repo=self.__injector__.get(PolicyRepository),
            policyService=self.__injector__.get(PolicyService),
            userRepo=self.__injector__.get(UserRepository),
            roleRepo=self.__injector__.get(RoleRepository),
            organizationRepo=self.__injector__.get(OrganizationRepository),
            projectRepo=self.__injector__.get(ProjectRepository),
        )

    @singleton
    @provider
    def provideUserLookupApplicationService(self) -> UserLookupApplicationService:
        return UserLookupApplicationService(repo=self.__injector__.get(UserLookupRepository))

    @singleton
    @provider
    def provideBuildingApplicationService(self) -> BuildingApplicationService:
        return BuildingApplicationService(
            repo=self.__injector__.get(BuildingRepository),
            buildingService=self.__injector__.get(BuildingService),
        )

    @singleton
    @provider
    def provideBuildingLevelApplicationService(self) -> BuildingLevelApplicationService:
        return BuildingLevelApplicationService(
            repo=self.__injector__.get(BuildingLevelRepository),
            buildingLevelService=self.__injector__.get(BuildingLevelService),
            buildingRepo=self.__injector__.get(BuildingRepository),
        )

    @singleton
    @provider
    def provideBuildingLevelRoomApplicationService(
        self,
    ) -> BuildingLevelRoomApplicationService:
        return BuildingLevelRoomApplicationService(
            repo=self.__injector__.get(BuildingLevelRoomRepository),
            buildingLevelRoomService=self.__injector__.get(BuildingLevelRoomService),
            buildingLevelRepository=self.__injector__.get(BuildingLevelRepository),
        )

    @singleton
    @provider
    def provideManufacturerApplicationService(self) -> ManufacturerApplicationService:
        return ManufacturerApplicationService(
            repo=self.__injector__.get(ManufacturerRepository),
            manufacturerService=self.__injector__.get(ManufacturerService),
        )

    @singleton
    @provider
    def provideSubcontractorApplicationService(self) -> SubcontractorApplicationService:
        return SubcontractorApplicationService(
            repo=self.__injector__.get(SubcontractorRepository),
            orgRepo=self.__injector__.get(OrganizationRepository),
            subcontractorService=self.__injector__.get(SubcontractorService),
            subcontractorCategoryRepo=self.__injector__.get(SubcontractorCategoryRepository),
        )

    @singleton
    @provider
    def provideEquipmentModelApplicationService(
        self,
    ) -> EquipmentModelApplicationService:
        return EquipmentModelApplicationService(
            repo=self.__injector__.get(EquipmentModelRepository),
            equipmentModelService=self.__injector__.get(EquipmentModelService),
        )

    @singleton
    @provider
    def provideManufacturerApplicationService(self) -> ManufacturerApplicationService:
        return ManufacturerApplicationService(
            repo=self.__injector__.get(ManufacturerRepository),
            manufacturerService=self.__injector__.get(ManufacturerService),
        )

    @singleton
    @provider
    def provideEquipmentProjectCategoryApplicationService(
        self,
    ) -> EquipmentProjectCategoryApplicationService:
        return EquipmentProjectCategoryApplicationService(
            repo=self.__injector__.get(EquipmentProjectCategoryRepository),
            groupRepo=self.__injector__.get(EquipmentCategoryGroupRepository),
            equipmentProjectCategoryService=self.__injector__.get(EquipmentProjectCategoryService),
        )

    @singleton
    @provider
    def provideUnitApplicationService(self) -> UnitApplicationService:
        return UnitApplicationService(
            repo=self.__injector__.get(UnitRepository),
            unitService=self.__injector__.get(UnitService),
        )

    @singleton
    @provider
    def provideEquipmentInputApplicationService(
        self,
    ) -> EquipmentInputApplicationService:
        return EquipmentInputApplicationService(
            repo=self.__injector__.get(EquipmentInputRepository),
            equipmentInputService=self.__injector__.get(EquipmentInputService),
        )

    @singleton
    @provider
    def provideEquipmentCategoryGroupApplicationService(
        self,
    ) -> EquipmentCategoryGroupApplicationService:
        return EquipmentCategoryGroupApplicationService(
            repo=self.__injector__.get(EquipmentCategoryGroupRepository),
            equipmentCategoryGroupService=self.__injector__.get(EquipmentCategoryGroupService),
        )

    @singleton
    @provider
    def provideEquipmentApplicationService(self) -> EquipmentApplicationService:
        return EquipmentApplicationService(
            repo=self.__injector__.get(EquipmentRepository),
            equipmentService=self.__injector__.get(EquipmentService),
            projectRepo=self.__injector__.get(ProjectRepository),
            equipmentProjectCategoryRepo=self.__injector__.get(EquipmentProjectCategoryRepository),
            equipmentCategoryGroupRepo=self.__injector__.get(EquipmentCategoryGroupRepository),
            buildingRepo=self.__injector__.get(BuildingRepository),
            buildingLevelRepo=self.__injector__.get(BuildingLevelRepository),
            buildingLevelRoomRepo=self.__injector__.get(BuildingLevelRoomRepository),
            manufacturerRepo=self.__injector__.get(ManufacturerRepository),
            equipmentModelRepo=self.__injector__.get(EquipmentModelRepository),
        )

    @singleton
    @provider
    def provideEquipmentInputApplicationService(
        self,
    ) -> EquipmentInputApplicationService:
        return EquipmentInputApplicationService(
            repo=self.__injector__.get(EquipmentInputRepository),
            equipmentInputService=self.__injector__.get(EquipmentInputService),
        )

    @singleton
    @provider
    def provideMaintenanceProcedureApplicationService(
        self,
    ) -> MaintenanceProcedureApplicationService:
        return MaintenanceProcedureApplicationService(
            repo=self.__injector__.get(MaintenanceProcedureRepository),
            maintenanceProcedureService=self.__injector__.get(MaintenanceProcedureService),
            equipmentRepo=self.__injector__.get(EquipmentRepository),
        )

    @singleton
    @provider
    def provideMaintenanceProcedureOperationApplicationService(
        self,
    ) -> MaintenanceProcedureOperationApplicationService:
        return MaintenanceProcedureOperationApplicationService(
            repo=self.__injector__.get(MaintenanceProcedureOperationRepository),
            maintenanceProcedureOperationService=self.__injector__.get(MaintenanceProcedureOperationService),
            maintenanceProcedureRepo=self.__injector__.get(MaintenanceProcedureRepository),
        )

    @singleton
    @provider
    def provideMaintenanceProcedureOperationParameterApplicationService(
        self,
    ) -> MaintenanceProcedureOperationParameterApplicationService:
        return MaintenanceProcedureOperationParameterApplicationService(
            repo=self.__injector__.get(MaintenanceProcedureOperationParameterRepository),
            maintenanceProcedureOperationParameterService=self.__injector__.get(
                MaintenanceProcedureOperationParameterService
            ),
            maintenanceProcedureOperationRepo=self.__injector__.get(MaintenanceProcedureOperationRepository),
        )

    @singleton
    @provider
    def provideProjectApplicationService(self) -> ProjectApplicationService:
        return ProjectApplicationService(
            repo=self.__injector__.get(ProjectRepository),
            projectService=self.__injector__.get(ProjectService),
        )

    @singleton
    @provider
    def provideDailyCheckProcedureOperationApplicationService(
        self,
    ) -> DailyCheckProcedureOperationApplicationService:
        return DailyCheckProcedureOperationApplicationService(
            repo=self.__injector__.get(DailyCheckProcedureOperationRepository),
            dailyCheckProcedureOperationService=self.__injector__.get(DailyCheckProcedureOperationService),
            dailyCheckProcedureRepo=self.__injector__.get(DailyCheckProcedureRepository),
        )

    @singleton
    @provider
    def provideDailyCheckProcedureApplicationService(
        self,
    ) -> DailyCheckProcedureApplicationService:
        return DailyCheckProcedureApplicationService(
            repo=self.__injector__.get(DailyCheckProcedureRepository),
            dailyCheckProcedureService=self.__injector__.get(DailyCheckProcedureService),
            equipmentRepo=self.__injector__.get(EquipmentRepository),
            equipmentCategoryGroupRepo=self.__injector__.get(EquipmentCategoryGroupRepository),
        )

    @singleton
    @provider
    def provideDailyCheckProcedureOperationParameterApplicationService(
        self,
    ) -> DailyCheckProcedureOperationParameterApplicationService:
        return DailyCheckProcedureOperationParameterApplicationService(
            repo=self.__injector__.get(DailyCheckProcedureOperationParameterRepository),
            dailyCheckProcedureOperationParameterService=self.__injector__.get(
                DailyCheckProcedureOperationParameterService
            ),
            unitRepo=self.__injector__.get(UnitRepository),
            dailyCheckProcedureOperationRepo=self.__injector__.get(DailyCheckProcedureOperationRepository),
        )

    @singleton
    @provider
    def provideStandardMaintenanceProcedureApplicationService(
        self,
    ) -> StandardMaintenanceProcedureApplicationService:
        return StandardMaintenanceProcedureApplicationService(
            repo=self.__injector__.get(StandardMaintenanceProcedureRepository),
            standardMaintenanceProcedureService=self.__injector__.get(StandardMaintenanceProcedureService),
            orgRepo=self.__injector__.get(OrganizationRepository),
            standardEquipmentCategoryGroupRepo=self.__injector__.get(StandardEquipmentCategoryGroupRepository),
        )

    @singleton
    @provider
    def provideSubcontractorCategoryApplicationService(
        self,
    ) -> SubcontractorCategoryApplicationService:
        return SubcontractorCategoryApplicationService(
            repo=self.__injector__.get(SubcontractorCategoryRepository),
            subcontractorCategoryService=self.__injector__.get(SubcontractorCategoryService),
        )

    @singleton
    @provider
    def provideStandardEquipmentCategoryApplicationService(
        self,
    ) -> StandardEquipmentCategoryApplicationService:
        return StandardEquipmentCategoryApplicationService(
            repo=self.__injector__.get(StandardEquipmentCategoryRepository),
            standardEquipmentCategoryService=self.__injector__.get(StandardEquipmentCategoryService),
        )

    @singleton
    @provider
    def provideStandardEquipmentApplicationService(
        self,
    ) -> StandardEquipmentApplicationService:
        return StandardEquipmentApplicationService(
            repo=self.__injector__.get(StandardEquipmentRepository),
            standardEquipmentService=self.__injector__.get(StandardEquipmentService),
            standardEquipmentCategoryRepo=self.__injector__.get(StandardEquipmentCategoryRepository),
            standardEquipmentCategoryGroupRepo=self.__injector__.get(StandardEquipmentCategoryGroupRepository),
            manufacturerRepo=self.__injector__.get(ManufacturerRepository),
            equipmentModelRepo=self.__injector__.get(EquipmentModelRepository),
        )

    @singleton
    @provider
    def provideStandardEquipmentCategoryGroupApplicationService(
        self,
    ) -> StandardEquipmentCategoryGroupApplicationService:
        return StandardEquipmentCategoryGroupApplicationService(
            repo=self.__injector__.get(StandardEquipmentCategoryGroupRepository),
            standardEquipmentCategoryGroupService=self.__injector__.get(StandardEquipmentCategoryGroupService),
            standardEquipmentCategoryRepo=self.__injector__.get(StandardEquipmentCategoryRepository),
        )

    @singleton
    @provider
    def provideLookup__Equipment__SubcontractorLookupApplicationService(
        self,
    ) -> Lookup__Equipment__SubcontractorLookupApplicationService:
        return Lookup__Equipment__SubcontractorLookupApplicationService(
            repo=self.__injector__.get(Lookup__Equipment__SubcontractorLookupRepository),
        )

    @singleton
    @provider
    def provideCountryApplicationService(self) -> CountryApplicationService:
        return CountryApplicationService(repo=self.__injector__.get(CountryRepository))

    @singleton
    @provider
    def provideCityApplicationService(self) -> CityApplicationService:
        return CityApplicationService(repo=self.__injector__.get(CityRepository))

    @singleton
    @provider
    def provideLookup__Equipment__SubcontractorCategoryLookupApplicationService(
        self,
    ) -> Lookup__Equipment__SubcontractorCategoryApplicationService:
        return Lookup__Equipment__SubcontractorCategoryApplicationService(
            repo=self.__injector__.get(Lookup__Equipment__SubcontractorCategoryRepository),
        )

    @singleton
    @provider
    def provideLookup__Equipment__EquipmentProjectCategoryApplicationService(
        self,
    ) -> Lookup__Equipment__EquipmentProjectCategoryApplicationService:
        return Lookup__Equipment__EquipmentProjectCategoryApplicationService(
            repo=self.__injector__.get(Lookup__Equipment__EquipmentProjectCategoryRepository),
        )

    @singleton
    @provider
    def provideLookup__Equipment__EquipmentCategoryGroupApplicationService(
        self,
    ) -> Lookup__Equipment__EquipmentCategoryGroupApplicationService:
        return Lookup__Equipment__EquipmentCategoryGroupApplicationService(
            repo=self.__injector__.get(Lookup__Equipment__EquipmentCategoryGroupRepository)
        )

    @singleton
    @provider
    def provideLookup__Equipment__BuildingApplicationService(self) -> Lookup__Equipment__BuildingApplicationService:
        return Lookup__Equipment__BuildingApplicationService(repo=self.__injector__.get(Lookup__Equipment__BuildingRepository))

    @singleton
    @provider
    def provideLookup__Equipment__BuildingLevelApplicationService(self) -> Lookup__Equipment__BuildingLevelApplicationService:
        return Lookup__Equipment__BuildingLevelApplicationService(repo=self.__injector__.get(Lookup__Equipment__BuildingLevelRepository))

    @singleton
    @provider
    def provideLookup__Equipment__BuildingLevelRoomApplicationService(self) -> Lookup__Equipment__BuildingLevelRoomApplicationService:
        return Lookup__Equipment__BuildingLevelRoomApplicationService(
            repo=self.__injector__.get(Lookup__Equipment__BuildingLevelRoomRepository)
        )

    @singleton
    @provider
    def provideLookup__Equipment__ManufacturerApplicationService(self) -> Lookup__Equipment__ManufacturerApplicationService:
        return Lookup__Equipment__ManufacturerApplicationService(repo=self.__injector__.get(Lookup__Equipment__ManufacturerRepository))

    @singleton
    @provider
    def provideLookup__Equipment__EquipmentModelApplicationService(self) -> Lookup__Equipment__EquipmentModelApplicationService:
        return Lookup__Equipment__EquipmentModelApplicationService(repo=self.__injector__.get(Lookup__Equipment__EquipmentModelRepository))

    @singleton
    @provider
    def provideLookup__Equipment__UnitApplicationService(self) -> Lookup__Equipment__UnitApplicationService:
        return Lookup__Equipment__UnitApplicationService(repo=self.__injector__.get(Lookup__Equipment__UnitRepository))

    @singleton
    @provider
    def provideLookup__Equipment__ProjectApplicationService(self) -> Lookup__Equipment__ProjectApplicationService:
        return Lookup__Equipment__ProjectApplicationService(repo=self.__injector__.get(Lookup__Equipment__ProjectRepository))

    @singleton
    @provider
    def provideLookup__Equipment__MaintenanceProcedureOperationParameterApplicationService(
        self,
    ) -> Lookup__Equipment__MaintenanceProcedureOperationParameterApplicationService:
        return Lookup__Equipment__MaintenanceProcedureOperationParameterApplicationService(
            repo=self.__injector__.get(Lookup__Equipment__MaintenanceProcedureOperationParameterRepository)
        )

    @singleton
    @provider
    def provideLookup__Equipment__MaintenanceProcedureOperationApplicationService(
        self,
    ) -> Lookup__Equipment__MaintenanceProcedureOperationApplicationService:
        return Lookup__Equipment__MaintenanceProcedureOperationApplicationService(
            repo=self.__injector__.get(Lookup__Equipment__MaintenanceProcedureOperationRepository)
        )

    @singleton
    @provider
    def provideLookup__Equipment__MaintenanceProcedureApplicationService(self) -> Lookup__Equipment__MaintenanceProcedureApplicationService:
        return Lookup__Equipment__MaintenanceProcedureApplicationService(
            repo=self.__injector__.get(Lookup__Equipment__MaintenanceProcedureRepository)
        )

    @singleton
    @provider
    def provideLookup__Equipment__EquipmentLookupApplicationService(self) -> Lookup__Equipment__EquipmentLookupApplicationService:
        return Lookup__Equipment__EquipmentLookupApplicationService(repo=self.__injector__.get(Lookup__Equipment__EquipmentLookupRepository))

    @singleton
    @provider
    def provideLookup__Equipment__EquipmentProjectCategoryApplicationService(self) -> Lookup__Equipment__EquipmentProjectCategoryApplicationService:
        return Lookup__Equipment__EquipmentProjectCategoryApplicationService(repo=self.__injector__.get(Lookup__Equipment__EquipmentProjectCategoryRepository))

    @singleton
    @provider
    def provideLookup__Equipment__EquipmentCategoryGroupApplicationService(self) -> Lookup__Equipment__EquipmentCategoryGroupApplicationService:
        return Lookup__Equipment__EquipmentCategoryGroupApplicationService(repo=self.__injector__.get(Lookup__Equipment__EquipmentCategoryGroupRepository))

    @singleton
    @provider
    def provideLookup__Equipment__BuildingLevelRoomApplicationService(self) -> Lookup__Equipment__BuildingLevelRoomApplicationService:
        return Lookup__Equipment__BuildingLevelRoomApplicationService(repo=self.__injector__.get(Lookup__Equipment__BuildingLevelRoomRepository))

    @singleton
    @provider
    def provideLookup__Unit__UnitApplicationService(self) -> Lookup__Unit__UnitApplicationService:
        return Lookup__Unit__UnitApplicationService(repo=self.__injector__.get(Lookup__Unit__UnitRepository))

    @singleton
    @provider
    def provideLookup__DailyCheckProcedureOperationParameter__DailyCheckProcedureOperationParameterApplicationService(self) -> Lookup__DailyCheckProcedureOperationParameter__DailyCheckProcedureOperationParameterApplicationService:
        return Lookup__DailyCheckProcedureOperationParameter__DailyCheckProcedureOperationParameterApplicationService(repo=self.__injector__.get(Lookup__DailyCheckProcedureOperationParameter__DailyCheckProcedureOperationParameterRepository))

    @singleton
    @provider
    def provideLookup__DailyCheckProcedureOperation__DailyCheckProcedureOperationApplicationService(self) -> Lookup__DailyCheckProcedureOperation__DailyCheckProcedureOperationApplicationService:
        return Lookup__DailyCheckProcedureOperation__DailyCheckProcedureOperationApplicationService(repo=self.__injector__.get(Lookup__DailyCheckProcedureOperation__DailyCheckProcedureOperationRepository))

    @singleton
    @provider
    def provideLookup__EquipmentCategoryGroup__EquipmentCategoryGroupApplicationService(self) -> Lookup__EquipmentCategoryGroup__EquipmentCategoryGroupApplicationService:
        return Lookup__EquipmentCategoryGroup__EquipmentCategoryGroupApplicationService(repo=self.__injector__.get(Lookup__EquipmentCategoryGroup__EquipmentCategoryGroupRepository))

    @singleton
    @provider
    def provideLookup__DailyCheckProcedure__DailyCheckProcedureApplicationService(self) -> Lookup__DailyCheckProcedure__DailyCheckProcedureApplicationService:
        return Lookup__DailyCheckProcedure__DailyCheckProcedureApplicationService(repo=self.__injector__.get(Lookup__DailyCheckProcedure__DailyCheckProcedureRepository))

    # endregion

    # region Repository
    @singleton
    @provider
    def provideProjectRepository(self) -> ProjectRepository:
        from src.port_adapter.repository.project.ProjectRepositoryImpl import (
            ProjectRepositoryImpl,
        )

        return ProjectRepositoryImpl()

    @singleton
    @provider
    def provideUserRepository(self) -> UserRepository:
        from src.port_adapter.repository.user.UserRepositoryImpl import (
            UserRepositoryImpl,
        )

        return UserRepositoryImpl()

    @singleton
    @provider
    def provideOrganizationRepository(self) -> OrganizationRepository:
        from src.port_adapter.repository.organization.OrganizationRepositoryImpl import (
            OrganizationRepositoryImpl,
        )

        return OrganizationRepositoryImpl()

    @singleton
    @provider
    def provideRoleRepository(self) -> RoleRepository:
        from src.port_adapter.repository.role.RoleRepositoryImpl import (
            RoleRepositoryImpl,
        )

        return RoleRepositoryImpl()

    @singleton
    @provider
    def providePolicyRepository(self) -> PolicyRepository:
        from src.port_adapter.repository.policy.PolicyRepositoryImpl import (
            PolicyRepositoryImpl,
        )

        return PolicyRepositoryImpl()

    @singleton
    @provider
    def provideUserLookupRepository(self) -> UserLookupRepository:
        from src.port_adapter.repository.lookup.user.UserLookupRepositoryImpl import (
            UserLookupRepositoryImpl,
        )

        return UserLookupRepositoryImpl()

    @singleton
    @provider
    def provideBuildingRepository(self) -> BuildingRepository:
        from src.port_adapter.repository.project.building.BuildingRepositoryImpl import (
            BuildingRepositoryImpl,
        )

        return BuildingRepositoryImpl()

    @singleton
    @provider
    def provideBuildingLevelRepository(self) -> BuildingLevelRepository:
        from src.port_adapter.repository.project.building.level.BuildingLevelRepositoryImpl import (
            BuildingLevelRepositoryImpl,
        )

        return BuildingLevelRepositoryImpl()

    @singleton
    @provider
    def provideBuildingLevelRoomRepository(self) -> BuildingLevelRoomRepository:
        from src.port_adapter.repository.project.building.level.room.BuildingLevelRoomRepositoryImpl import (
            BuildingLevelRoomRepositoryImpl,
        )

        return BuildingLevelRoomRepositoryImpl()

    @singleton
    @provider
    def provideEquipmentProjectCategoryRepository(
        self,
    ) -> EquipmentProjectCategoryRepository:
        from src.port_adapter.repository.project.equipment.project_category.EquipmentProjectCategoryRepositoryImpl import (
            EquipmentProjectCategoryRepositoryImpl,
        )

        return EquipmentProjectCategoryRepositoryImpl()


    @singleton
    @provider
    def provideEquipmentCategoryGroupRepository(
        self,
    ) -> EquipmentCategoryGroupRepository:
        from src.port_adapter.repository.project.equipment.category.group.EquipmentCategoryGroupRepositoryImpl import (
            EquipmentCategoryGroupRepositoryImpl,
        )

        return EquipmentCategoryGroupRepositoryImpl()

    @singleton
    @provider
    def provideEquipmentModelRepository(self) -> EquipmentModelRepository:
        from src.port_adapter.repository.project.equipment.model.EquipmentModelRepositoryImpl import (
            EquipmentModelRepositoryImpl,
        )

        return EquipmentModelRepositoryImpl()

    @singleton
    @provider
    def provideManufacturerRepository(self) -> ManufacturerRepository:
        from src.port_adapter.repository.manufacturer.ManufacturerRepositoryImpl import (
            ManufacturerRepositoryImpl,
        )

        return ManufacturerRepositoryImpl()

    @singleton
    @provider
    def provideEquipmentRepository(self) -> EquipmentRepository:
        from src.port_adapter.repository.project.equipment.EquipmentRepositoryImpl import (
            EquipmentRepositoryImpl,
        )

        return EquipmentRepositoryImpl()

    @singleton
    @provider
    def provideSubcontractorRepository(self) -> SubcontractorRepository:
        from src.port_adapter.repository.subcontractor.SubcontractorRepositoryImpl import (
            SubcontractorRepositoryImpl,
        )

        return SubcontractorRepositoryImpl()

    @singleton
    @provider
    def provideEquipmentModelRepository(self) -> EquipmentModelRepository:
        from src.port_adapter.repository.project.equipment.model.EquipmentModelRepositoryImpl import (
            EquipmentModelRepositoryImpl,
        )

        return EquipmentModelRepositoryImpl()

    @singleton
    @provider
    def provideEquipmentProjectCategoryRepository(
        self,
    ) -> EquipmentProjectCategoryRepository:
        from src.port_adapter.repository.project.equipment.project_category.EquipmentProjectCategoryRepositoryImpl import (
            EquipmentProjectCategoryRepositoryImpl,
        )

        return EquipmentProjectCategoryRepositoryImpl()

    @singleton
    @provider
    def provideEquipmentCategoryGroupRepository(
        self,
    ) -> EquipmentCategoryGroupRepository:
        from src.port_adapter.repository.project.equipment.category.group.EquipmentCategoryGroupRepositoryImpl import (
            EquipmentCategoryGroupRepositoryImpl,
        )

        return EquipmentCategoryGroupRepositoryImpl()

    @singleton
    @provider
    def provideUnitRepository(self) -> UnitRepository:
        from src.port_adapter.repository.project.unit.UnitRepositoryImpl import (
            UnitRepositoryImpl,
        )

        return UnitRepositoryImpl()

    @singleton
    @provider
    def provideEquipmentInputRepository(self) -> EquipmentInputRepository:
        from src.port_adapter.repository.project.equipment.input.EquipmentInputRepositoryImpl import (
            EquipmentInputRepositoryImpl,
        )

        return EquipmentInputRepositoryImpl()

    @singleton
    @provider
    def provideMaintenanceProcedureRepository(self) -> MaintenanceProcedureRepository:
        from src.port_adapter.repository.project.maintenance.procedure.MaintenanceProcedureRepositoryImpl import (
            MaintenanceProcedureRepositoryImpl,
        )

        return MaintenanceProcedureRepositoryImpl()

    @singleton
    @provider
    def provideMaintenanceProcedureOperationRepository(
        self,
    ) -> MaintenanceProcedureOperationRepository:
        from src.port_adapter.repository.project.maintenance.procedure.operation.MaintenanceProcedureOperationRepositoryImpl import (
            MaintenanceProcedureOperationRepositoryImpl,
        )

        return MaintenanceProcedureOperationRepositoryImpl()

    @singleton
    @provider
    def provideMaintenanceProcedureOperationParameterRepository(
        self,
    ) -> MaintenanceProcedureOperationParameterRepository:
        from src.port_adapter.repository.project.maintenance.procedure.operation.parameter.MaintenanceProcedureOperationParameterRepositoryImpl import (
            MaintenanceProcedureOperationParameterRepositoryImpl,
        )

        return MaintenanceProcedureOperationParameterRepositoryImpl()

    @singleton
    @provider
    def provideDailyCheckProcedureRepository(self) -> DailyCheckProcedureRepository:
        from src.port_adapter.repository.project.daily_check.procedure.DailyCheckProcedureRepositoryImpl import (
            DailyCheckProcedureRepositoryImpl,
        )

        return DailyCheckProcedureRepositoryImpl()

    @singleton
    @provider
    def provideDailyCheckProcedureOperationRepository(
        self,
    ) -> DailyCheckProcedureOperationRepository:
        from src.port_adapter.repository.project.daily_check.procedure.operation.DailyCheckProcedureOperationRepositoryImpl import (
            DailyCheckProcedureOperationRepositoryImpl,
        )

        return DailyCheckProcedureOperationRepositoryImpl()

    @singleton
    @provider
    def provideDailyCheckProcedureOperationParameterRepository(
        self,
    ) -> DailyCheckProcedureOperationParameterRepository:
        from src.port_adapter.repository.project.daily_check.procedure.operation.parameter.DailyCheckProcedureOperationParameterRepositoryImpl import (
            DailyCheckProcedureOperationParameterRepositoryImpl,
        )

        return DailyCheckProcedureOperationParameterRepositoryImpl()

    @singleton
    @provider
    def provideStandardMaintenanceProcedureRepository(
        self,
    ) -> StandardMaintenanceProcedureRepository:
        from src.port_adapter.repository.standard_maintenance_procedure.StandardMaintenanceProcedureRepositoryImpl import (
            StandardMaintenanceProcedureRepositoryImpl,
        )

        return StandardMaintenanceProcedureRepositoryImpl()

    @singleton
    @provider
    def provideSubcontractorCategoryRepository(self) -> SubcontractorCategoryRepository:
        from src.port_adapter.repository.subcontractor.category.SubcontractorCategoryRepositoryImpl import (
            SubcontractorCategoryRepositoryImpl,
        )

        return SubcontractorCategoryRepositoryImpl()

    @singleton
    @provider
    def provideStandardEquipmentCategoryRepository(
        self,
    ) -> StandardEquipmentCategoryRepository:
        from src.port_adapter.repository.project.standard_equipment.standard_category.StandardEquipmentCategoryRepositoryImpl import (
            StandardEquipmentCategoryRepositoryImpl,
        )

        return StandardEquipmentCategoryRepositoryImpl()

    @singleton
    @provider
    def provideStandardEquipmentCategoryGroupRepository(
        self,
    ) -> StandardEquipmentCategoryGroupRepository:
        from src.port_adapter.repository.project.standard_equipment.standard_category.standard_group.StandardEquipmentCategoryGroupRepositoryImpl import (
            StandardEquipmentCategoryGroupRepositoryImpl,
        )

        return StandardEquipmentCategoryGroupRepositoryImpl()

    @singleton
    @provider
    def provideStandardEquipmentRepository(self) -> StandardEquipmentRepository:
        from src.port_adapter.repository.project.standard_equipment.StandardEquipmentRepositoryImpl import (
            StandardEquipmentRepositoryImpl,
        )

        return StandardEquipmentRepositoryImpl()

    @singleton
    @provider
    def provideLookup__Equipment__SubcontractorLookupRepository(self) -> Lookup__Equipment__SubcontractorLookupRepository:
        from src.port_adapter.repository.lookup.subcontractor.SubcontractorLookupRepositoryImpl import (
            SubcontractorLookupRepositoryImpl,
        )

        return SubcontractorLookupRepositoryImpl()

    @singleton
    @provider
    def provideCountryRepository(self) -> CountryRepository:
        from src.port_adapter.repository.country.CountryRepositoryImpl import (
            CountryRepositoryImpl,
        )

        return CountryRepositoryImpl()

    @singleton
    @provider
    def provideCityRepository(self) -> CityRepository:
        from src.port_adapter.repository.city.CityRepositoryImpl import (
            CityRepositoryImpl,
        )

        return CityRepositoryImpl()

    @singleton
    @provider
    def provideLookup__Equipment__SubcontractorCategoryLookupRepository(
        self,
    ) -> Lookup__Equipment__SubcontractorCategoryRepository:
        from src.port_adapter.repository.lookup.subcontractor.SubcontractorCategoryRepositoryImpl import (
            SubcontractorCategoryRepositoryImpl,
        )

        return SubcontractorCategoryRepositoryImpl()

    @singleton
    @provider
    def provideLookup__Equipment__EquipmentProjectCategoryRepository(self) -> Lookup__Equipment__EquipmentProjectCategoryRepository:
        from src.port_adapter.repository.lookup.equipment.EquipmentProjectCategoryRepositoryImpl import (
            EquipmentProjectCategoryRepositoryImpl,
        )

        return EquipmentProjectCategoryRepositoryImpl()


    @singleton
    @provider
    def provideLookup__Equipment__EquipmentCategoryGroupRepository(self) -> Lookup__Equipment__EquipmentCategoryGroupRepository:
        from src.port_adapter.repository.lookup.equipment.EquipmentCategoryGroupRepositoryImpl import (
            EquipmentCategoryGroupRepositoryImpl,
        )

        return EquipmentCategoryGroupRepositoryImpl()

    @singleton
    @provider
    def provideLookup__Equipment__BuildingRepository(self) -> Lookup__Equipment__BuildingRepository:
        from src.port_adapter.repository.lookup.equipment.BuildingRepositoryImpl import BuildingRepositoryImpl

        return BuildingRepositoryImpl()

    @singleton
    @provider
    def provideLookup__Equipment__BuildingLevelRepository(self) -> Lookup__Equipment__BuildingLevelRepository:
        from src.port_adapter.repository.lookup.equipment.BuildingLevelRepositoryImpl import BuildingLevelRepositoryImpl

        return BuildingLevelRepositoryImpl()

    @singleton
    @provider
    def provideLookup__Equipment__BuildingLevelRoomRepository(self) -> Lookup__Equipment__BuildingLevelRoomRepository:
        from src.port_adapter.repository.lookup.equipment.BuildingLevelRoomRepositoryImpl import (
            BuildingLevelRoomRepositoryImpl,
        )

        return BuildingLevelRoomRepositoryImpl()

    @singleton
    @provider
    def provideLookup__Equipment__ManufacturerRepository(self) -> Lookup__Equipment__ManufacturerRepository:
        from src.port_adapter.repository.lookup.equipment.ManufacturerRepositoryImpl import ManufacturerRepositoryImpl

        return ManufacturerRepositoryImpl()

    @singleton
    @provider
    def provideLookup__Equipment__EquipmentModelRepository(self) -> Lookup__Equipment__EquipmentModelRepository:
        from src.port_adapter.repository.lookup.equipment.EquipmentModelRepositoryImpl import (
            EquipmentModelRepositoryImpl,
        )

        return EquipmentModelRepositoryImpl()

    @singleton
    @provider
    def provideLookup__Equipment__UnitRepository(self) -> Lookup__Equipment__UnitRepository:
        from src.port_adapter.repository.lookup.equipment.UnitRepositoryImpl import UnitRepositoryImpl

        return UnitRepositoryImpl()

    @singleton
    @provider
    def provideLookup__Equipment__ProjectRepository(self) -> Lookup__Equipment__ProjectRepository:
        from src.port_adapter.repository.lookup.equipment.ProjectRepositoryImpl import ProjectRepositoryImpl

        return ProjectRepositoryImpl()

    @singleton
    @provider
    def provideLookup__Equipment__MaintenanceProcedureOperationParameterRepository(
        self,
    ) -> Lookup__Equipment__MaintenanceProcedureOperationParameterRepository:
        from src.port_adapter.repository.lookup.equipment.MaintenanceProcedureOperationParameterRepositoryImpl import (
            MaintenanceProcedureOperationParameterRepositoryImpl,
        )

        return MaintenanceProcedureOperationParameterRepositoryImpl()

    @singleton
    @provider
    def provideLookup__Equipment__MaintenanceProcedureOperationRepository(self) -> Lookup__Equipment__MaintenanceProcedureOperationRepository:
        from src.port_adapter.repository.lookup.equipment.MaintenanceProcedureOperationRepositoryImpl import (
            MaintenanceProcedureOperationRepositoryImpl,
        )

        return MaintenanceProcedureOperationRepositoryImpl()

    @singleton
    @provider
    def provideLookup__Equipment__MaintenanceProcedureRepository(self) -> Lookup__Equipment__MaintenanceProcedureRepository:
        from src.port_adapter.repository.lookup.equipment.MaintenanceProcedureRepositoryImpl import (
            MaintenanceProcedureRepositoryImpl,
        )

        return MaintenanceProcedureRepositoryImpl()

    @singleton
    @provider
    def provideLookup__Equipment__EquipmentLookupRepository(self) -> Lookup__Equipment__EquipmentLookupRepository:
        from src.port_adapter.repository.lookup.equipment.EquipmentLookupRepositoryImpl import (
            EquipmentLookupRepositoryImpl,
        )

        return EquipmentLookupRepositoryImpl()

    @singleton
    @provider
    def provideLookup__Equipment__EquipmentProjectCategoryRepository(self) -> Lookup__Equipment__EquipmentProjectCategoryRepository:
        from src.port_adapter.repository.lookup.equipment.EquipmentProjectCategoryRepositoryImpl import EquipmentProjectCategoryRepositoryImpl
        return EquipmentProjectCategoryRepositoryImpl()        

    @singleton
    @provider
    def provideLookup__Equipment__EquipmentCategoryGroupRepository(self) -> Lookup__Equipment__EquipmentCategoryGroupRepository:
        from src.port_adapter.repository.lookup.equipment.EquipmentCategoryGroupRepositoryImpl import EquipmentCategoryGroupRepositoryImpl
        return EquipmentCategoryGroupRepositoryImpl()        

    @singleton
    @provider
    def provideLookup__Equipment__BuildingRepository(self) -> Lookup__Equipment__BuildingRepository:
        from src.port_adapter.repository.lookup.equipment.BuildingRepositoryImpl import BuildingRepositoryImpl
        return BuildingRepositoryImpl()        

    @singleton
    @provider
    def provideLookup__Equipment__BuildingLevelRepository(self) -> Lookup__Equipment__BuildingLevelRepository:
        from src.port_adapter.repository.lookup.equipment.BuildingLevelRepositoryImpl import BuildingLevelRepositoryImpl
        return BuildingLevelRepositoryImpl()        

    @singleton
    @provider
    def provideLookup__Equipment__BuildingLevelRoomRepository(self) -> Lookup__Equipment__BuildingLevelRoomRepository:
        from src.port_adapter.repository.lookup.equipment.BuildingLevelRoomRepositoryImpl import BuildingLevelRoomRepositoryImpl
        return BuildingLevelRoomRepositoryImpl()        

    @singleton
    @provider
    def provideLookup__Equipment__ManufacturerRepository(self) -> Lookup__Equipment__ManufacturerRepository:
        from src.port_adapter.repository.lookup.equipment.ManufacturerRepositoryImpl import ManufacturerRepositoryImpl
        return ManufacturerRepositoryImpl()        

    @singleton
    @provider
    def provideLookup__Equipment__EquipmentModelRepository(self) -> Lookup__Equipment__EquipmentModelRepository:
        from src.port_adapter.repository.lookup.equipment.EquipmentModelRepositoryImpl import EquipmentModelRepositoryImpl
        return EquipmentModelRepositoryImpl()        

    @singleton
    @provider
    def provideLookup__Equipment__UnitRepository(self) -> Lookup__Equipment__UnitRepository:
        from src.port_adapter.repository.lookup.equipment.UnitRepositoryImpl import UnitRepositoryImpl
        return UnitRepositoryImpl()        

    @singleton
    @provider
    def provideLookup__Unit__UnitRepository(self) -> Lookup__Unit__UnitRepository:
        from src.port_adapter.repository.lookup.daily_check_procedure.UnitRepositoryImpl import UnitRepositoryImpl
        return UnitRepositoryImpl()        

    @singleton
    @provider
    def provideLookup__DailyCheckProcedureOperationParameter__DailyCheckProcedureOperationParameterRepository(self) -> Lookup__DailyCheckProcedureOperationParameter__DailyCheckProcedureOperationParameterRepository:
        from src.port_adapter.repository.lookup.daily_check_procedure.DailyCheckProcedureOperationParameterRepositoryImpl import DailyCheckProcedureOperationParameterRepositoryImpl
        return DailyCheckProcedureOperationParameterRepositoryImpl()        

    @singleton
    @provider
    def provideLookup__DailyCheckProcedureOperation__DailyCheckProcedureOperationRepository(self) -> Lookup__DailyCheckProcedureOperation__DailyCheckProcedureOperationRepository:
        from src.port_adapter.repository.lookup.daily_check_procedure.DailyCheckProcedureOperationRepositoryImpl import DailyCheckProcedureOperationRepositoryImpl
        return DailyCheckProcedureOperationRepositoryImpl()        

    @singleton
    @provider
    def provideLookup__EquipmentCategoryGroup__EquipmentCategoryGroupRepository(self) -> Lookup__EquipmentCategoryGroup__EquipmentCategoryGroupRepository:
        from src.port_adapter.repository.lookup.daily_check_procedure.EquipmentCategoryGroupRepositoryImpl import EquipmentCategoryGroupRepositoryImpl
        return EquipmentCategoryGroupRepositoryImpl()        

    @singleton
    @provider
    def provideLookup__DailyCheckProcedure__DailyCheckProcedureRepository(self) -> Lookup__DailyCheckProcedure__DailyCheckProcedureRepository:
        from src.port_adapter.repository.lookup.daily_check_procedure.DailyCheckProcedureRepositoryImpl import DailyCheckProcedureRepositoryImpl
        return DailyCheckProcedureRepositoryImpl()        

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
        return RoleService(repository=self.__injector__.get(RoleRepository))

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
        return BuildingLevelService(
            buildingLevelRepo=self.__injector__.get(BuildingLevelRepository),
            buildingRepo=self.__injector__.get(BuildingRepository),
        )

    @singleton
    @provider
    def provideBuildingLevelRoomService(self) -> BuildingLevelRoomService:
        return BuildingLevelRoomService(
            buildingLevelRoomRepo=self.__injector__.get(BuildingLevelRoomRepository),
            buildingLevelRepo=self.__injector__.get(BuildingLevelRepository),
        )

    @singleton
    @provider
    def provideBuildingLevelRoomService(self) -> BuildingLevelRoomService:
        return BuildingLevelRoomService(
            buildingLevelRoomRepo=self.__injector__.get(BuildingLevelRoomRepository),
            buildingLevelRepo=self.__injector__.get(BuildingLevelRepository),
        )

    @singleton
    @provider
    def provideEquipmentService(self) -> EquipmentService:
        return EquipmentService(repository=self.__injector__.get(EquipmentRepository))

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
        return SubcontractorService(repository=self.__injector__.get(SubcontractorRepository))

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
    def provideMaintenanceProcedureOperationService(
        self,
    ) -> MaintenanceProcedureOperationService:
        return MaintenanceProcedureOperationService(
            repository=self.__injector__.get(MaintenanceProcedureOperationRepository)
        )

    @singleton
    @provider
    def provideMaintenanceProcedureOperationParameterService(
        self,
    ) -> MaintenanceProcedureOperationParameterService:
        return MaintenanceProcedureOperationParameterService(
            repository=self.__injector__.get(MaintenanceProcedureOperationParameterRepository)
        )

    @singleton
    @provider
    def provideDailyCheckProcedureService(self) -> DailyCheckProcedureService:
        return DailyCheckProcedureService(repository=self.__injector__.get(DailyCheckProcedureRepository))

    @singleton
    @provider
    def provideDailyCheckProcedureOperationService(
        self,
    ) -> DailyCheckProcedureOperationService:
        return DailyCheckProcedureOperationService(
            repository=self.__injector__.get(DailyCheckProcedureOperationRepository)
        )

    @singleton
    @provider
    def provideDailyCheckProcedureOperationParameterService(
        self,
    ) -> DailyCheckProcedureOperationParameterService:
        return DailyCheckProcedureOperationParameterService(
            repository=self.__injector__.get(DailyCheckProcedureOperationParameterRepository)
        )

    @singleton
    @provider
    def provideStandardMaintenanceProcedureService(
        self,
    ) -> StandardMaintenanceProcedureService:
        return StandardMaintenanceProcedureService(
            repository=self.__injector__.get(StandardMaintenanceProcedureRepository)
        )

    @singleton
    @provider
    def provideSubcontractorCategoryService(self) -> SubcontractorCategoryService:
        return SubcontractorCategoryService(repository=self.__injector__.get(SubcontractorCategoryRepository))

    @singleton
    @provider
    def provideStandardEquipmentCategoryService(
        self,
    ) -> StandardEquipmentCategoryService:
        return StandardEquipmentCategoryService(repository=self.__injector__.get(StandardEquipmentCategoryRepository))

    @singleton
    @provider
    def provideStandardEquipmentCategoryGroupService(
        self,
    ) -> StandardEquipmentCategoryGroupService:
        return StandardEquipmentCategoryGroupService(
            repository=self.__injector__.get(StandardEquipmentCategoryGroupRepository)
        )

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
    def provideConsumer(
        self,
        groupId: str = uuid4(),
        autoCommit: bool = False,
        partitionEof: bool = True,
        autoOffsetReset: str = ConsumerOffsetReset.earliest.name,
    ) -> Consumer:
        return KafkaConsumer(
            groupId=groupId,
            autoCommit=autoCommit,
            partitionEof=partitionEof,
            autoOffsetReset=autoOffsetReset,
        )

    # endregion

    # region db
    @singleton
    @provider
    def provideDbBase(self) -> DbBase:
        return declarative_base()

    @singleton
    @provider
    def provideDbContext(self) -> BaseDbContainer:
        from src.port_adapter.repository.DbContainer import DbContainer
        return DbContainer()
    # endregion

    # region Resource
    @singleton
    @provider
    def provideOpenTelemetry(self) -> OpenTelemetry:
        return OpenTelemetry()

    # endregion


class Builder:
    @classmethod
    def buildConsumer(
        cls,
        groupId: str = uuid4(),
        autoCommit: bool = False,
        partitionEof: bool = True,
        autoOffsetReset: str = ConsumerOffsetReset.earliest.name,
    ) -> Consumer:
        builder = instance.get(ClassAssistedBuilder[KafkaConsumer])
        return builder.build(
            groupId=groupId,
            autoCommit=autoCommit,
            partitionEof=partitionEof,
            autoOffsetReset=autoOffsetReset,
        )


instance = Injector([AppDi])
