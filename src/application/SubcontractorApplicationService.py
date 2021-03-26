"""
@author: Mohammad S. moso<moso@develoop.run>
"""
from typing import List

from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.resource.exception.UpdateSubcontractorFailedException import UpdateSubcontractorFailedException
from src.domain_model.subcontractor.Subcontractor import Subcontractor
from src.domain_model.subcontractor.SubcontractorRepository import SubcontractorRepository
from src.domain_model.subcontractor.SubcontractorService import SubcontractorService
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class SubcontractorApplicationService:
    def __init__(self, repo: SubcontractorRepository,
                 orgRepo: OrganizationRepository,
                 domainService: SubcontractorService):
        self._repo = repo
        self._orgRepo = orgRepo
        self._domainService = domainService

    @debugLogger
    def newId(self):
        return Subcontractor.createFrom().id()

    @debugLogger
    def createSubcontractor(self, id: str = None, companyName: str = None, websiteUrl: str = None,
                            contactPerson: str = None,
                            email: str = None, phoneNumber: str = None, addressOne: str = None, addressTwo: str = None,
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
    def updateSubcontractor(self, id: str = None, companyName: str = None, websiteUrl: str = None,
                            contactPerson: str = None,
                            email: str = None, phoneNumber: str = None, addressOne: str = None, addressTwo: str = None,
                            token: str = ''):
        obj: Subcontractor = self.constructObject(id=id,
                                                  companyName=companyName,
                                                  websiteUrl=websiteUrl,
                                                  contactPerson=contactPerson,
                                                  email=email,
                                                  phoneNumber=phoneNumber,
                                                  addressOne=addressOne,
                                                  addressTwo=addressTwo)
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: Subcontractor = self._repo.subcontractorById(id=id)
            self._domainService.updateSubcontractor(oldObject=oldObject,
                                                    newObject=obj,
                                                    tokenData=tokenData)
        except Exception as e:
            raise UpdateSubcontractorFailedException(message=str(e))

    @debugLogger
    def deleteSubcontractor(self, id: str, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.subcontractorById(id=id)
        self._domainService.deleteSubcontractor(obj=obj, tokenData=tokenData)

    @debugLogger
    def assignSubcontractor(self, id: str, organizationId: str, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        subcontractor = self._repo.subcontractorById(id=id)
        organization = self._orgRepo.organizationById(id=organizationId)
        self._domainService.assignSubcontractor(subcontractor=subcontractor, organization=organization,
                                                tokenData=tokenData)

    @debugLogger
    def revokeSubcontractor(self, id: str, organizationId: str, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        subcontractor = self._repo.subcontractorById(id=id)
        organization = self._orgRepo.organizationById(id=organizationId)
        self._domainService.revokeSubcontractor(subcontractor=subcontractor, organization=organization,
                                                tokenData=tokenData)

    @debugLogger
    def subcontractorById(self, id: str, token: str = '') -> Subcontractor:
        obj = self._repo.subcontractorById(id=id)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return obj

    @debugLogger
    def subcontractors(self, resultFrom: int = 0, resultSize: int = 100, token: str = '',
                       order: List[dict] = None) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._domainService.subcontractors(tokenData=tokenData,
                                                  resultFrom=resultFrom,
                                                  resultSize=resultSize,
                                                  order=order)

    @debugLogger
    def constructObject(self, id: str = None, companyName: str = None, websiteUrl: str = None,
                        contactPerson: str = None,
                        email: str = None, phoneNumber: str = None, addressOne: str = None,
                        addressTwo: str = None) -> Subcontractor:
        return Subcontractor.createFrom(id=id,
                                        companyName=companyName,
                                        websiteUrl=websiteUrl,
                                        contactPerson=contactPerson,
                                        email=email,
                                        phoneNumber=phoneNumber,
                                        addressOne=addressOne,
                                        addressTwo=addressTwo)
