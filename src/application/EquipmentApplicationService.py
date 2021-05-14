"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from src.application.BaseApplicationService import BaseApplicationService
from src.domain_model.manufacturer.ManufacturerRepository import ManufacturerRepository
from src.domain_model.project.ProjectRepository import ProjectRepository
from src.domain_model.project.building.BuildingRepository import BuildingRepository
from src.domain_model.project.building.level.BuildingLevelRepository import (
    BuildingLevelRepository,
)
from src.domain_model.project.building.level.room.BuildingLevelRoomRepository import (
    BuildingLevelRoomRepository,
)
from src.domain_model.project.equipment.Equipment import Equipment
from src.domain_model.project.equipment.EquipmentRepository import EquipmentRepository
from src.domain_model.project.equipment.EquipmentService import EquipmentService
from src.domain_model.project.equipment.category.EquipmentCategoryRepository import (
    EquipmentCategoryRepository,
)
from src.domain_model.project.equipment.category.group.EquipmentCategoryGroupRepository import (
    EquipmentCategoryGroupRepository,
)
from src.domain_model.project.equipment.model.EquipmentModelRepository import (
    EquipmentModelRepository,
)
from src.domain_model.project.equipment.project_category.EquipmentProjectCategoryRepository import (
    EquipmentProjectCategoryRepository,
)
from src.domain_model.resource.exception.DomainModelException import (
    DomainModelException,
)
from src.domain_model.resource.exception.ProcessBulkDomainException import (
    ProcessBulkDomainException,
)
from src.domain_model.resource.exception.UpdateEquipmentFailedException import (
    UpdateEquipmentFailedException,
)
from src.domain_model.token.TokenService import TokenService
from src.domain_model.util.DomainModelAttributeValidator import DomainModelAttributeValidator
from src.resource.logging.decorator import debugLogger


class EquipmentApplicationService(BaseApplicationService):
    def __init__(
        self,
        repo: EquipmentRepository,
        equipmentService: EquipmentService,
        projectRepo: ProjectRepository,
        equipmentProjectCategoryRepo: EquipmentProjectCategoryRepository,
        equipmentCategoryRepo: EquipmentCategoryRepository,
        equipmentCategoryGroupRepo: EquipmentCategoryGroupRepository,
        buildingRepo: BuildingRepository,
        buildingLevelRepo: BuildingLevelRepository,
        buildingLevelRoomRepo: BuildingLevelRoomRepository,
        manufacturerRepo: ManufacturerRepository,
        equipmentModelRepo: EquipmentModelRepository,
    ):
        self._repo = repo
        self._equipmentService = equipmentService
        self._projectRepo = projectRepo
        self._equipmentProjectCategoryRepo = equipmentProjectCategoryRepo
        self._equipmentCategoryRepo = equipmentCategoryRepo
        self._equipmentCategoryGroupRepo = equipmentCategoryGroupRepo
        self._buildingRepo = buildingRepo
        self._buildingLevelRepo = buildingLevelRepo
        self._buildingLevelRoomRepo = buildingLevelRoomRepo
        self._manufacturerRepo = manufacturerRepo
        self._equipmentModelRepo = equipmentModelRepo

    @debugLogger
    def newId(self):
        return Equipment.createFrom(skipValidation=True).id()

    @debugLogger
    def createEquipment(
        self,
        id: str = None,
        name: str = None,
        projectId: str = None,
        equipmentProjectCategoryId: str = None,
        equipmentCategoryId: str = None,
        equipmentCategoryGroupId: str = None,
        buildingId: str = None,
        buildingLevelId: str = None,
        buildingLevelRoomId: str = None,
        manufacturerId: str = None,
        equipmentModelId: str = None,
        quantity: int = None,
        objectOnly: bool = False,
        token: str = "",
    ):
        obj: Equipment = self._constructObject(
            id=id,
            name=name,
            projectId=projectId,
            equipmentProjectCategoryId=equipmentProjectCategoryId,
            equipmentCategoryId=equipmentCategoryId,
            equipmentCategoryGroupId=equipmentCategoryGroupId,
            buildingId=buildingId,
            buildingLevelId=buildingLevelId,
            buildingLevelRoomId=buildingLevelRoomId,
            manufacturerId=manufacturerId,
            equipmentModelId=equipmentModelId,
            quantity=quantity,
        )
        tokenData = TokenService.tokenDataFromToken(token=token)
        self._projectRepo.projectById(id=projectId)
        self._equipmentProjectCategoryRepo.equipmentProjectCategoryById(id=equipmentProjectCategoryId)
        self._equipmentCategoryRepo.equipmentCategoryById(id=equipmentCategoryId)
        self._equipmentCategoryGroupRepo.equipmentCategoryGroupById(id=equipmentCategoryGroupId)
        self._buildingRepo.buildingById(id=buildingId, include=[])
        self._buildingLevelRepo.buildingLevelById(id=buildingLevelId, include=[])
        self._buildingLevelRoomRepo.buildingLevelRoomById(id=buildingLevelRoomId)
        self._manufacturerRepo.manufacturerById(id=manufacturerId)
        self._equipmentModelRepo.equipmentModelById(id=equipmentModelId)
        return self._equipmentService.createEquipment(obj=obj, objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def updateEquipment(
        self,
        id: str,
        name: str = None,
        projectId: str = None,
        equipmentProjectCategoryId: str = None,
        equipmentCategoryId: str = None,
        equipmentCategoryGroupId: str = None,
        buildingId: str = None,
        buildingLevelId: str = None,
        buildingLevelRoomId: str = None,
        manufacturerId: str = None,
        equipmentModelId: str = None,
        quantity: int = None,
        token: str = None,
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: Equipment = self._repo.equipmentById(id=id)
            obj: Equipment = self._constructObject(
                id=id,
                name=name,
                projectId=projectId,
                equipmentProjectCategoryId=equipmentProjectCategoryId,
                equipmentCategoryId=equipmentCategoryId,
                equipmentCategoryGroupId=equipmentCategoryGroupId,
                buildingId=buildingId,
                buildingLevelId=buildingLevelId,
                buildingLevelRoomId=buildingLevelRoomId,
                manufacturerId=manufacturerId,
                equipmentModelId=equipmentModelId,
                quantity=quantity,
                _sourceObject=oldObject,
            )
            self._equipmentService.updateEquipment(oldObject=oldObject, newObject=obj, tokenData=tokenData)
        except Exception as e:
            raise UpdateEquipmentFailedException(message=str(e))

    @debugLogger
    def deleteEquipment(self, id: str, token: str = None):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.equipmentById(id=id)
        self._equipmentService.deleteEquipment(obj=obj, tokenData=tokenData)

    @debugLogger
    def bulkCreate(self, objListParams: List[dict], token: str = ""):
        objList = []
        exceptions = []
        for objListParamsItem in objListParams:
            try:
                DomainModelAttributeValidator.validate(
                    domainModelObject=self._constructObject(skipValidation=True), attributeDictionary=objListParamsItem
                )
                objList.append(
                    self._constructObject(
                        id=objListParamsItem["equipment_id"],
                        name=objListParamsItem["name"],
                        projectId=objListParamsItem["project_id"],
                        equipmentProjectCategoryId=objListParamsItem["equipment_project_category_id"],
                        equipmentCategoryId=objListParamsItem["equipment_category_id"],
                        equipmentCategoryGroupId=objListParamsItem["equipment_category_group_id"],
                        buildingId=objListParamsItem["building_id"],
                        buildingLevelId=objListParamsItem["building_level_id"],
                        buildingLevelRoomId=objListParamsItem["building_level_room_id"],
                        manufacturerId=objListParamsItem["manufacturer_id"],
                        equipmentModelId=objListParamsItem["equipment_model_id"],
                        quantity=objListParamsItem["quantity"],
                    )
                )
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._equipmentService.bulkCreate(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    @debugLogger
    def bulkDelete(self, objListParams: List[dict], token: str = ""):
        objList = []
        exceptions = []
        for objListParamsItem in objListParams:
            try:
                DomainModelAttributeValidator.validate(
                    domainModelObject=self._constructObject(skipValidation=True), attributeDictionary=objListParamsItem
                )
                objList.append(self._constructObject(id=objListParamsItem["equipment_id"], skipValidation=True))
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._equipmentService.bulkDelete(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    @debugLogger
    def bulkUpdate(self, objListParams: List[dict], token: str = ""):
        objList = []
        exceptions = []
        for objListParamsItem in objListParams:
            try:
                DomainModelAttributeValidator.validate(
                    domainModelObject=self._constructObject(skipValidation=True), attributeDictionary=objListParamsItem
                )
                oldObject: Equipment = self._repo.equipmentById(id=objListParamsItem["equipment_id"])
                newObject = self._constructObject(
                    id=objListParamsItem["equipment_id"],
                    name=objListParamsItem["name"] if "name" in objListParamsItem else None,
                    projectId=objListParamsItem["project_id"] if "project_id" in objListParamsItem else None,
                    equipmentProjectCategoryId=objListParamsItem["equipment_project_category_id"]
                    if "equipment_project_category_id" in objListParamsItem
                    else None,
                    equipmentCategoryId=objListParamsItem["equipment_category_id"]
                    if "equipment_category_id" in objListParamsItem
                    else None,
                    equipmentCategoryGroupId=objListParamsItem["equipment_category_group_id"]
                    if "equipment_category_group_id" in objListParamsItem
                    else None,
                    buildingId=objListParamsItem["building_id"] if "building_id" in objListParamsItem else None,
                    buildingLevelId=objListParamsItem["building_level_id"]
                    if "building_level_id" in objListParamsItem
                    else None,
                    buildingLevelRoomId=objListParamsItem["building_level_room_id"]
                    if "building_level_room_id" in objListParamsItem
                    else None,
                    manufacturerId=objListParamsItem["manufacturer_id"]
                    if "manufacturer_id" in objListParamsItem
                    else None,
                    equipmentModelId=objListParamsItem["equipment_model_id"]
                    if "equipment_model_id" in objListParamsItem
                    else None,
                    quantity=objListParamsItem["quantity"] if "quantity" in objListParamsItem else None,
                    _sourceObject=oldObject,
                )
                objList.append(
                    (newObject, oldObject),
                )
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._equipmentService.bulkUpdate(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    @debugLogger
    def equipmentById(self, id: str, token: str = None) -> Equipment:
        equipment = self._repo.equipmentById(id=id)
        TokenService.tokenDataFromToken(token=token)
        return equipment

    @debugLogger
    def equipments(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        token: str = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._equipmentService.equipments(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> Equipment:
        kwargs[BaseApplicationService.APPLICATION_SERVICE_CLASS] = Equipment
        return super()._constructObject(*args, **kwargs)
