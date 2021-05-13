"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.project.Project import Project
from src.domain_model.project.ProjectRepository import ProjectRepository
from src.domain_model.project.ProjectService import ProjectService
from src.domain_model.resource.exception.UpdateProjectFailedException import (
    UpdateProjectFailedException,
)
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class ProjectApplicationService:
    def __init__(self, repo: ProjectRepository, projectService: ProjectService):
        self._repo = repo
        self._projectService = projectService

    @debugLogger
    def newId(self):
        return Project.createFrom(skipValidation=True).id()

    @debugLogger
    def createProject(
        self,
        id: str = None,
        name: str = "",
        cityId: int = 0,
        countryId: int = 0,
        addressLine: str = "",
        beneficiaryId: str = "",
        objectOnly: bool = False,
        startDate: int = None,
        token: str = "",
    ):
        obj: Project = self.constructObject(
            id=id,
            name=name,
            cityId=cityId,
            countryId=countryId,
            addressLine=addressLine,
            beneficiaryId=beneficiaryId,
            startDate=startDate,
        )
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._projectService.createProject(
            obj=obj, objectOnly=objectOnly, tokenData=tokenData
        )

    @debugLogger
    def updateProject(
        self,
        id: str,
        name: str = None,
        cityId: int = None,
        countryId: int = None,
        addressLine: str = None,
        addressLineTwo: str = None,
        beneficiaryId: str = None,
        startDate: int = None,
        developerName: str = None,
        developerCityId: int = None,
        developerCountryId: int = None,
        developerAddressLineOne: str = None,
        developerAddressLineTwo: str = None,
        developerContact: str = None,
        developerEmail: str = None,
        developerPhoneNumber: str = None,
        developerWarranty: str = None,
        token: str = "",
    ):

        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: Project = self._repo.projectById(id=id)
            obj: Project = self.constructObject(
                id=id,
                name=name,
                cityId=cityId,
                countryId=countryId,
                addressLine=addressLine,
                addressLineTwo=addressLineTwo,
                beneficiaryId=beneficiaryId,
                startDate=startDate,
                developerName=developerName,
                developerCityId=developerCityId,
                developerCountryId=developerCountryId,
                developerAddressLineOne=developerAddressLineOne,
                developerAddressLineTwo=developerAddressLineTwo,
                developerContact=developerContact,
                developerEmail=developerEmail,
                developerPhoneNumber=developerPhoneNumber,
                developerWarranty=developerWarranty,
                _sourceObject=oldObject,
            )
            self._projectService.updateProject(
                oldObject=oldObject, newObject=obj, tokenData=tokenData
            )
        except Exception as e:
            raise UpdateProjectFailedException(message=str(e))

    @debugLogger
    def deleteProject(self, id: str, token: str = ""):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.projectById(id=id)
        self._projectService.deleteProject(obj=obj, tokenData=tokenData)

    @debugLogger
    def changeState(self, projectId: str, state: str, token: str = ""):
        tokenData = TokenService.tokenDataFromToken(token=token)
        project = self._repo.projectById(id=projectId)
        project.changeState(Project.stateStringToProjectState(state))
        self._repo.changeState(project=project, tokenData=tokenData)

    @debugLogger
    def projectById(self, id: str, token: str = "") -> Project:
        project = self._repo.projectById(id=id)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return project

    @debugLogger
    def projects(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        token: str = "",
        order: List[dict] = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._projectService.projects(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def constructObject(
        self,
        id: str,
        name: str,
        cityId: int,
        countryId: int,
        addressLine: str,
        beneficiaryId: str,
        startDate: int,
        addressLineTwo: str = "",
        _sourceObject: Project = None,
        developerName: str = None,
        developerCityId: int = None,
        developerCountryId: int = None,
        developerAddressLineOne: str = None,
        developerAddressLineTwo: str = None,
        developerContact: str = None,
        developerEmail: str = None,
        developerPhoneNumber: str = None,
        developerWarranty: str = None,
        skipValidation: bool = False,
    ) -> Project:
        if _sourceObject is not None:
            return Project.createFrom(
                id=id,
                name=name if name is not None else _sourceObject.name(),
                cityId=cityId if cityId is not None else _sourceObject.cityId(),
                countryId=countryId
                if countryId is not None
                else _sourceObject.countryId(),
                addressLine=addressLine
                if addressLine is not None
                else _sourceObject.addressLine(),
                addressLineTwo=addressLineTwo
                if addressLineTwo is not None
                else _sourceObject.addressLineTwo(),
                beneficiaryId=beneficiaryId
                if beneficiaryId is not None
                else _sourceObject.beneficiaryId(),
                startDate=startDate
                if startDate is not None
                else _sourceObject.startDate(),
                developerName=developerName
                if developerName is not None
                else _sourceObject.developerName(),
                developerCityId=developerCityId
                if developerCityId is not None
                else _sourceObject.developerCityId(),
                developerCountryId=developerCountryId
                if developerCountryId is not None
                else _sourceObject.developerCountryId(),
                developerAddressLineOne=developerAddressLineOne
                if developerAddressLineOne is not None
                else _sourceObject.developerAddressLineOne(),
                developerAddressLineTwo=developerAddressLineTwo
                if developerAddressLineTwo is not None
                else _sourceObject.developerAddressLineTwo(),
                developerContact=developerContact
                if developerContact is not None
                else _sourceObject.developerContact(),
                developerEmail=developerEmail
                if developerEmail is not None
                else _sourceObject.developerEmail(),
                developerPhoneNumber=developerPhoneNumber
                if developerPhoneNumber is not None
                else _sourceObject.developerPhoneNumber(),
                developerWarranty=developerWarranty
                if developerWarranty is not None
                else _sourceObject.developerWarranty(),
                skipValidation=skipValidation,
            )
        else:
            return Project.createFrom(
                id=id,
                name=name,
                cityId=cityId,
                countryId=countryId,
                addressLine=addressLine,
                addressLineTwo=addressLineTwo,
                beneficiaryId=beneficiaryId,
                startDate=startDate,
                skipValidation=skipValidation,
            )
