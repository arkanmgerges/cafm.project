"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json

from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.user.User import User
from src.domain_model.user.UserRepository import UserRepository
from src.resource.logging.logger import logger


class UserHandler():
    def __init__(self):
        import src.port_adapter.AppDi as AppDi
        self._eventConstants = [
            CommonEventConstant.USER_CREATED.value,
            CommonEventConstant.USER_UPDATED.value,
            CommonEventConstant.USER_DELETED.value,
        ]
        self._userRepository: UserRepository = AppDi.instance.get(UserRepository)

    def canHandle(self, name: str) -> bool:
        return name in self._eventConstants

    def handleCommand(self, messageData: dict):
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{UserHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')
        dataDict = json.loads(data)
        # metadataDict = json.loads(metadata)
        #
        # if 'token' not in metadataDict:
        #     raise UnAuthorizedException()

        return self.handlers(name, **dataDict)

    def handlers(self, event, *args, **kwargs):
        funcSwitcher = {
            CommonEventConstant.USER_CREATED.value: self._save,
            CommonEventConstant.USER_UPDATED.value: self._save,
            CommonEventConstant.USER_DELETED.value: self._save,
        }

        argSwitcher = {
            CommonEventConstant.USER_CREATED.value: lambda: {'obj': User.createFrom(**self._snakeCaseToLowerCameCaseDict(kwargs))},
            CommonEventConstant.USER_UPDATED.value: lambda: {'obj': User.createFrom(**self._snakeCaseToLowerCameCaseDict(kwargs['new']))},
            CommonEventConstant.USER_DELETED.value: lambda: {'obj': User.createFrom(**self._snakeCaseToLowerCameCaseDict(kwargs))},
        }
        func = funcSwitcher.get(event, None)
        if func is not None:
            func(*args, **(argSwitcher.get(event))())
        return None

    def _save(self, *_args, obj: User):
        self._userRepository.save(obj=obj)
        return None

    def _delete(self, *_args, obj: User):
        self._userRepository.deleteUser(obj=obj)
        return None

    def _snakeCaseToLowerCameCaseDict(self, dataDict: dict) -> dict:
        result = {}
        for key, val in dataDict.items():
            components = key.split('_')
            result[components[0] + ''.join(x.title() for x in components[1:])] = val
        return result
