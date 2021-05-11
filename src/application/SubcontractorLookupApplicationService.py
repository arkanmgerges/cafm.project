"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from src.application.lookup.subcontractor.SubcontractorLookupRepository import SubcontractorLookupRepository
from src.application.user_lookup.UserLookup import UserLookup
from src.domain_model.subcontractor.Subcontractor import Subcontractor
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class SubcontractorLookupApplicationService:
    def __init__(self, repo: SubcontractorLookupRepository):
        self._repo = repo

    @debugLogger
    def saveBySource(self, source: Subcontractor, token: str = ""):
        _tokenData = TokenService.tokenDataFromToken(token=token)
        _userLookup: UserLookup = self._repo.saveBySource(source=source)
