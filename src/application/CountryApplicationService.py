"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


from src.application.BaseApplicationService import BaseApplicationService
from src.application.lifecycle.decorator.readOnly import readOnly
from src.application.model.BaseApplicationServiceModelData import BaseApplicationServiceModelData
from src.domain_model.country.Country import Country
from src.domain_model.country.CountryRepository import CountryRepository
from src.domain_model.country.state.State import State
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class CountryApplicationService(BaseApplicationService):
    def __init__(self, repo: CountryRepository):
        self._repo = repo

    @readOnly
    @debugLogger
    def countryById(self, id: int, token: str = None, **_kwargs) -> Country:
        TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(getterFunction=self._repo.countryById, kwargs={"id": id})
        )

    @readOnly
    @debugLogger
    def stateByCountryIdAndStateId(self, countryId: int, stateId: str, token: str = None, **_kwargs) -> State:
        TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(getterFunction=self._repo.stateByCountryIdAndStateId,
                                                      kwargs={"countryId": countryId, 'stateId': stateId})
        )

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> Country:
        kwargs[BaseApplicationService.DOMAIN_MODEL_CLASS] = Country
        return super()._constructObject(*args, **kwargs)
