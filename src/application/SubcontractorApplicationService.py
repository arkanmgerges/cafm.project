"""
@author: Mohammad S. moso<moso@develoop.run>
"""

from src.domain_model.subcontractor.Subcontractor import Subcontractor
from src.domain_model.subcontractor.SubcontractorRepository import SubcontractorRepository
from src.domain_model.subcontractor.SubcontractorService import SubcontractorService
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class SubcontractorApplicationService:
    def __init__(self, repo: SubcontractorRepository, domainService: SubcontractorService):
        self._repo = repo
        self._domainService = domainService

    @debugLogger
    def createSubcontractor(self, id: str = None, companyName: str = '', websiteUrl: str = '', contactPerson: str = '',
                            email: str = '', phoneNumber: str = '', addressOne: str = '', addressTwo: str = '',
                            objectOnly: bool = False, token: str = '') -> Subcontractor:
        obj: Subcontractor = self.constructObject(id=id,
                                                  companyName=companyName,
                                                  websiteUrl=websiteUrl,
                                                  contactPerson=contactPerson,
                                                  email=email,
                                                  phoneNumber=phoneNumber,
                                                  addressOne=addressOne,
                                                  addressTwo=addressTwo)
        tokenData = TokenService.tokenDataFromToken(token=token)

        return self._domainService.createSubcontractor(obj=obj,
                                                       objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def constructObject(self, id: str = None, companyName: str = '', websiteUrl: str = '', contactPerson: str = '',
                        email: str = '', phoneNumber: str = '', addressOne: str = '',
                        addressTwo: str = '') -> Subcontractor:
        return Subcontractor.createFrom(id=id,
                                        companyName=companyName,
                                        websiteUrl=websiteUrl,
                                        contactPerson=contactPerson,
                                        email=email,
                                        phoneNumber=phoneNumber,
                                        addressOne=addressOne,
                                        addressTwo=addressTwo)
