"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import os
from typing import List, Optional

from elasticsearch_dsl.connections import connections
from sqlalchemy import create_engine

from src.domain_model.project.building.Building import Building
from src.domain_model.project.building.BuildingRepository import BuildingRepository
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.project.building.level.BuildingLevelRepository import BuildingLevelRepository
from src.domain_model.project.building.level.room.BuildingLevelRoom import BuildingLevelRoom
from src.domain_model.project.building.level.room.BuildingLevelRoomRepository import BuildingLevelRoomRepository
from src.domain_model.project.equipment.EquipmentRepository import EquipmentRepository
from src.domain_model.project.equipment.model.EquipmentModelRepository import EquipmentModelRepository
from src.domain_model.project.maintenance.procedure.MaintenanceProcedure import MaintenanceProcedure
from src.domain_model.project.maintenance.procedure.MaintenanceProcedureRepository import MaintenanceProcedureRepository
from src.port_adapter.repository.lookup.BaseLookupRepository import BaseLookupRepository

from src.application.lookup.equipment.EquipmentLookup import EquipmentLookup
from src.domain_model.project.equipment.Equipment import Equipment
from src.application.lookup.equipment.EquipmentLookupRepository import EquipmentLookupRepository
from src.port_adapter.repository.es_model.lookup.equipment.Equipment import Equipment as EsEquipment
from src.domain_model.project.equipment.project_category.EquipmentProjectCategory import EquipmentProjectCategory
from src.domain_model.project.equipment.project_category.EquipmentProjectCategoryRepository import EquipmentProjectCategoryRepository
from src.port_adapter.repository.es_model.lookup.equipment.EquipmentProjectCategory import EquipmentProjectCategory as EsEquipmentProjectCategory
from src.domain_model.project.equipment.category.EquipmentCategory import EquipmentCategory
from src.domain_model.project.equipment.category.EquipmentCategoryRepository import EquipmentCategoryRepository
from src.port_adapter.repository.es_model.lookup.equipment.EquipmentModel import EquipmentModel as EsEquipmentModel
from src.port_adapter.repository.es_model.lookup.equipment.EquipmentCategory import EquipmentCategory as EsEquipmentCategory
from src.domain_model.project.equipment.category.group.EquipmentCategoryGroup import EquipmentCategoryGroup
from src.domain_model.project.equipment.category.group.EquipmentCategoryGroupRepository import EquipmentCategoryGroupRepository
from src.port_adapter.repository.es_model.lookup.equipment.EquipmentCategoryGroup import EquipmentCategoryGroup as EsEquipmentCategoryGroup
from src.port_adapter.repository.es_model.lookup.equipment.Building import Building as EsBuilding
from src.port_adapter.repository.es_model.lookup.equipment.BuildingLevel import BuildingLevel as EsBuildingLevel
from src.port_adapter.repository.es_model.lookup.equipment.BuildingLevelRoom import BuildingLevelRoom as EsBuildingLevelRoom
from src.domain_model.manufacturer.Manufacturer import Manufacturer
from src.domain_model.manufacturer.ManufacturerRepository import ManufacturerRepository
from src.port_adapter.repository.es_model.lookup.equipment.Manufacturer import Manufacturer as EsManufacturer
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class EquipmentLookupRepositoryImpl(BaseLookupRepository, EquipmentLookupRepository):
    def __init__(self):
        import src.port_adapter.AppDi as AppDi
        self._equipmentProjectCategoryRepo: EquipmentProjectCategoryRepository = AppDi.instance.get(EquipmentProjectCategoryRepository)
        self._equipmentCategoryRepo: EquipmentCategoryRepository = AppDi.instance.get(EquipmentCategoryRepository)
        self._equipmentCategoryGroupRepo: EquipmentCategoryGroupRepository = AppDi.instance.get(EquipmentCategoryGroupRepository)
        self._buildingRepo: BuildingRepository = AppDi.instance.get(BuildingRepository)
        self._buildingLevelRepo: BuildingLevelRepository = AppDi.instance.get(BuildingLevelRepository)
        self._buildingLevelRoomRepo: BuildingLevelRoomRepository = AppDi.instance.get(BuildingLevelRoomRepository)
        self._manufacturerRepo: ManufacturerRepository = AppDi.instance.get(ManufacturerRepository)
        self._equipmentModelRepo: EquipmentModelRepository = AppDi.instance.get(EquipmentModelRepository)
        self._equipmentRepo: EquipmentRepository = AppDi.instance.get(EquipmentRepository)
        self._maintenanceProcedureRepo: MaintenanceProcedureRepository = AppDi.instance.get(MaintenanceProcedureRepository)


        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}"
            )
            self._es = connections.create_connection(
                hosts=[
                    f'{os.getenv("CAFM_PROJECT_ELASTICSEARCH_HOST", "elasticsearch")}:{os.getenv("CAFM_PROJECT_ELASTICSEARCH_PORT", 9200)}'
                ]
            )
        except Exception as e:
            logger.warn(
                f"[{EquipmentLookupRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}"
            )
            raise Exception(f"Could not connect to the db, message: {e}")

    @debugLogger
    def save(self, obj: Equipment):
        equipmentProjectCategory: Optional[EquipmentProjectCategory, None] = None
        equipmentCategory: Optional[EquipmentCategory, None] = None
        equipmentCategoryGroup: Optional[EquipmentCategoryGroup, None] = None
        building: Optional[Building, None] = None
        buildingLevel: Optional[BuildingLevel, None] = None
        buildingLevelRoom: Optional[BuildingLevelRoom, None] = None
        manufacturer: Optional[Manufacturer, None] = None
        equipment: Optional[Equipment, None] = None
        maintenanceProcedure: Optional[MaintenanceProcedure, None] = None
        equipmentProjectCategory = self._equipmentProjectCategoryRepo.equipmentProjectCategoryById(id=obj.equipmentProjectCategoryId()) if obj.equipmentProjectCategoryId() is not None else None
        equipmentCategory = self._equipmentCategoryRepo.equipmentCategoryById(id=obj.equipmentCategoryId()) if obj.equipmentCategoryId() is not None else None
        equipmentCategoryGroup = self._equipmentCategoryGroupRepo.equipmentCategoryGroupById(id=obj.equipmentCategoryGroupId()) if obj.equipmentCategoryGroupId() is not None else None
        building = self._buildingRepo.buildingById(id=obj.buildingId()) if obj.buildingId() is not None else None
        buildingLevel = self._buildingLevelRepo.buildingLevelById(id=obj.buildingLevelId()) if obj.buildingLevelId() is not None else None
        buildingLevelRoom = self._buildingLevelRoomRepo.buildingLevelRoomById(id=obj.buildingLevelRoomId()) if obj.buildingLevelRoomId() is not None else None
        manufacturer = self._manufacturerRepo.manufacturerById(id=obj.manufacturerId()) if obj.manufacturerId() is not None else None
        equipment = self._equipmentRepo.equipmentById(id=obj.id()) if obj.id() is not None else None

        esDoc = EsEquipment.get(id=obj.id(), ignore=404)
        if esDoc is None:
            # Create
            EsEquipment(
                _id=obj.id(),
                id=obj.id(),
                name=obj.name(),
                quantity=obj.quantity(),
                project_id=obj.projectId(),
                equipment_project_category=EsEquipmentProjectCategory(
                    _id=equipmentProjectCategory.id(),
                    id=equipmentProjectCategory.id(),
                    name=equipmentProjectCategory.name(),
                ) if equipmentProjectCategory is not None else None,
                equipment_category=EsEquipmentCategory(
                    _id=equipmentCategory.id(),
                    id=equipmentCategory.id(),
                    name=equipmentCategory.name(),
                ) if equipmentCategory is not None else None,
                equipment_category_group=EsEquipmentCategoryGroup(
                    _id=equipmentCategoryGroup.id(),
                    id=equipmentCategoryGroup.id(),
                    name=equipmentCategoryGroup.name(),
                ) if equipmentCategoryGroup is not None else None,
                building=EsBuilding(
                    _id=building.id(),
                    id=building.id(),
                    name=building.name(),
                ),
                building_level=EsBuildingLevel(
                    _id=buildingLevel.id(),
                    id=buildingLevel.id(),
                    name=buildingLevel.name(),
                    is_sub_level=buildingLevel.isSubLevel(),
                ),
                building_level_room=EsBuildingLevelRoom(
                    _id=buildingLevelRoom.id(),
                    id=buildingLevelRoom.id(),
                    name=buildingLevelRoom.name(),
                    description=buildingLevelRoom.description(),
                ),
                manufacturer=EsManufacturer(
                    _id=manufacturer.id(),
                    id=manufacturer.id(),
                    name=manufacturer.name(),
                ),
                equipment_model=EsEquipmentModel(
                    _id=equipment.id(),
                    id=equipment.id(),
                    name=equipment.name(),
                ),
                maintenanceProcedures=[]
            ).save()
        else:
            # Update
            EsEquipment(
                _id=obj.id(),
                id=obj.id() if obj.id() is not None else esDoc.id,
                name=obj.name() if obj.name() is not None else esDoc.name,
                quantity=obj.quantity() if obj.quantity() is not None else esDoc.quantity,
                project_id=obj.projectId() if obj.projectId() is not None else esDoc.project_id,
                equipment_project_category=EsEquipmentProjectCategory(
                    _id=equipmentProjectCategory.id(),
                    id=equipmentProjectCategory.id(),
                    name=equipmentProjectCategory.name(),
                ) if obj.equipmentProjectCategoryId() is not None else esDoc.equipment_project_category,
                equipment_category=EsEquipmentCategory(
                    _id=equipmentCategory.id(),
                    id=equipmentCategory.id(),
                    name=equipmentCategory.name(),
                ) if obj.equipmentCategoryId() is not None else esDoc.equipment_category,
                equipment_category_group=EsEquipmentCategoryGroup(
                    _id=equipmentCategoryGroup.id(),
                    id=equipmentCategoryGroup.id(),
                    name=equipmentCategoryGroup.name(),
                ) if obj.equipmentCategoryGroupId() is not None else esDoc.equipment_category_group,
                building=EsBuilding(
                    _id=building.id(),
                    id=building.id(),
                    name=building.name(),
                ) if obj.buildingId() is not None else esDoc.building,
                building_level=EsBuildingLevel(
                    _id=buildingLevel.id(),
                    id=buildingLevel.id(),
                    name=buildingLevel.name(),
                    is_sub_level=buildingLevel.isSubLevel(),
                ) if obj.buildingLevelId() is not None else esDoc.building_level,
                building_level_room=EsBuildingLevelRoom(
                    _id=buildingLevelRoom.id(),
                    id=buildingLevelRoom.id(),
                    name=buildingLevelRoom.name(),
                    description=buildingLevelRoom.description(),
                ) if obj.buildingLevelRoomId() is not None else esDoc.building_level_room,
                manufacturer=EsManufacturer(
                    _id=manufacturer.id(),
                    id=manufacturer.id(),
                    name=manufacturer.name(),
                ) if obj.manufacturerId() is not None else esDoc.manufacturer,
                equipment_model=EsEquipment(
                    _id=equipment.id(),
                    id=equipment.id(),
                    name=equipment.name(),
                ) if obj.equipmentModelId() is not None else esDoc.equipment_model,
            ).save()

    @debugLogger
    def delete(self, obj: Equipment):
        esDoc = EsEquipment.get(id=obj.id(), ignore=404)
        if esDoc is not None:
            esDoc.delete(id=obj.id(), ignore=404)

    @debugLogger
    def lookup(self, resultFrom: int, resultSize: int, orders: List[dict], filters: List[dict]):
        return super().lookup(
            resultFrom=resultFrom,
            resultSize=resultSize,
            orders=orders,
            filters=filters,
            esModel=EsEquipment,
            lookupModel=EquipmentLookup,
        )
