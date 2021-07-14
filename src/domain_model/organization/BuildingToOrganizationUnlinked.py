from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant

class BuildingToOrganizationUnlinked (DomainEvent):
    def __init__(self, organizationId:str = None, buildingId:str = None, buildingLevelId:str = None, buildingLevelRoomId:str =None):
        super().__init__(
            id=str(uuid4()), name=CommonEventConstant.BUILDING_TO_ORGANIZATION_UNLINKED.value
        )
        self._data = {
            "organization_id": organizationId,
            "building_id": buildingId,
            "building_level_id": buildingLevelId,
            "building_level_room_id": buildingLevelRoomId,
        }
