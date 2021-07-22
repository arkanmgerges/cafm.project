"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


class ProjectStatistic:
    def __init__(
        self,
        projectId: str = None,
        projectName: str = None,
        projectCreatedAt: int = None,
        projectModifiedAt: int = None,
        buildingCount: int = None,
        equipmentCount: int = None,
        maintenanceProcedureCount: int = None,
    ):
        self._projectId: str = projectId
        self._projectName: str = projectName
        self._projectCreatedAt: int = projectCreatedAt
        self._projectModifiedAt: int = projectModifiedAt
        self._buildingCount: int = buildingCount
        self._equipmentCount: int = equipmentCount
        self._maintenanceProcedureCount: int = maintenanceProcedureCount

    def projectId(self) -> str:
        return self._projectId

    def projectName(self) -> str:
        return self._projectName

    def projectCreatedAt(self) -> int:
        return self._projectCreatedAt

    def projectModifiedAt(self) -> int:
        return self._projectModifiedAt

    def buildingCount(self) -> int:
        return self._buildingCount

    def equipmentCount(self) -> int:
        return self._equipmentCount

    def maintenanceProcedureCount(self) -> int:
        return self._maintenanceProcedureCount



    def result(self) -> dict:
        return {
            "project_id": self._projectId,
            "project_name": self._projectName,
            "project_created_at": self._projectCreatedAt,
            "project_modified_at": self._projectModifiedAt,
            "building_count": self._buildingCount,
            "equipment_count": self._equipmentCount,
            "maintenance_procedure_count": self._maintenanceProcedureCount,
        }

    def toMap(self) -> dict:
        return self.result()

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"
