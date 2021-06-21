from copy import copy

from uuid import uuid4


class Tag:
    def __init__(
        self,
        id: str = None,
        name: str = None,
        skipValidation: bool = False,
    ):
        if not skipValidation:
            if name is None or name == "":
                from src.domain_model.resource.exception.InvalidArgumentException import (
                    InvalidArgumentException,
                )

                raise InvalidArgumentException(
                    f"Invalid tag name: {name}, for tag id: {id}"
                )

        self._id = str(uuid4()) if id is None else id
        self._name = name

    def id(self) -> str:
        return self._id

    def name(self) -> str:
        return self._name

    def update(self, data: dict):
        updated = False
        old = copy(self)
        if "name" in data and data["name"] != self._name and data["name"] is not None:
            updated = True
            self._name = data["name"]
        if updated:
            self.publishUpdate(old)

    def toMap(self) -> dict:
        return {"tag_id": self.id(), "name": self.name()}

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __eq__(self, other):
        if not isinstance(other, Tag):
            raise NotImplementedError(
                f"other: {other} can not be compared with Role class"
            )
        return (
            self.id() == other.id()
            and self.name() == other.name()
        )
