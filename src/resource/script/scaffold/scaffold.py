"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>

Usage:
    python -m src.resource.script.scaffold.scaffold
    # Print config
    python -m src.resource.script.scaffold.scaffold print-config config.yaml
    # Generate code
    python -m src.resource.script.scaffold.scaffold generate config.yaml
"""

import json
import os
import sys
import re
import traceback
from pathlib import Path

import click
import emoji
import yaml
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

from src.resource.common.Util import Util


# region Global config & settings
class FrontTextTerminalColor:
    BLUE = "\x1b[34m"
    LIGHT_BLUE = "\x1b[94m"
    GREEN = "\x1b[32m"
    YELLOW = "\x1b[33m"
    RED = "\x1b[31m"
    RESET = "\x1b[0m"
    BLACK = "\x1B[30m"
    CYAN = "\x1b[36m"
    BOLD = "\x1B[1m"
    MAGENTA = "\x1b[35m"
    UNDERLINE_ON = "\x1b[4m"
    UNDERLINE_OFF = "\x1b[24m"


class BackgroundTextTerminalColor:
    BLUE = "\x1B[44m"
    LIGHT_BLUE = "\x1b[104m"
    GREEN = "\x1B[42m"
    YELLOW = "\x1B[43m"
    RED = "\x1B[41m"
    RESET = "\x1b[0m"
    CYAN = "\x1b[46m"
    BLACK = "\x1B[40m"
    MAGENTA = "\x1b[45m"
    UNDERLINE_ON = "\x1b[4m"
    UNDERLINE_OFF = "\x1b[24m"


class Config:
    configData = None
    projectPath = None
    templatePath = None
    configFilePath = None

    @staticmethod
    def __repr__():
        return (
            f"{FrontTextTerminalColor.GREEN}projectPath:{FrontTextTerminalColor.RESET} {Config.projectPath}\n"
            f"{FrontTextTerminalColor.GREEN}templatePath:{FrontTextTerminalColor.RESET} {Config.templatePath}\n"
            f"{FrontTextTerminalColor.GREEN}configFilePath:{FrontTextTerminalColor.RESET} {Config.configFilePath}\n"
            f"{FrontTextTerminalColor.GREEN}configData:{FrontTextTerminalColor.RESET} {json.dumps(Config.configData, indent=2)}\n"
        )


# endregion

# region Cli commands
@click.group()
def cli():
    pass


@cli.command(help="Generate code files based on a config file")
@click.argument("config_file")
def generate(config_file):
    # Init the config data
    initConfigData(config_file)
    # Generate models
    generateDomainModel()
    # Generate domain model services
    generateDomainModelService()
    # Generate domain model repositories
    generateDomainModelRepository()
    # Generate application services
    generateApplicationService()
    # Generate repository
    generateRepositoryImplementation()
    # Generate db model repository
    generateDbRepository()
    # Generate es model repository
    generateEsRepository()
    # Generate messaging listener
    generateMessagingListener()
    # Generate protocol buffer files
    generateProtoBuffer()
    # Generate grpc api
    generateGrpcApi()
    # Generate test
    generateTest()
    # Generate app di
    generateAppDi()


@cli.command(help="Print config data")
@click.argument("config_file")
def print_config(config_file):
    initConfigData(config_file)
    print(Config.__repr__())


# endregion

# Read the config data and save it into Config class
def initConfigData(configFile):
    configData = readConfig(configFile)
    Config.configData = configData


# Initialize the global configuration, provide full paths to the script
def initGlobalConfig():
    Config.projectPath = os.path.abspath(f"{os.path.dirname(__file__)}/../../../..")
    Config.templatePath = f"{Config.projectPath}/src/resource/script/scaffold/template"
    Config.configFilePath = f"{Config.projectPath}/src/resource/script/scaffold"


# Read config yaml file
def readConfig(configFile) -> dict:
    try:
        with open(f"{Config.configFilePath}/{configFile}", "r") as file:
            return yaml.load(file, Loader=yaml.FullLoader)
    except:
        print(traceback.format_exc())
        print("Could not read config file")
        sys.exit(1)


# Generate domain model services
def generateDomainModelService():
    _print(modelName="", message=":gear: Generating domain model services")
    domainModelPath = Config.configData["global"]["path"]["domain_model"]
    domainModelFullPath = f"{Config.projectPath}/{domainModelPath}"
    _createDir(path=domainModelFullPath)
    modelTemplates = jinjaEnv.get_template(f"domain_model/service/segment.jinja2")

    for modelConfig in Config.configData["domain_model"]:
        isGenerated = False
        model = modelConfig["model"]
        doNotSkip = (
            True
            if (
                "skip" in model
                and "domain_service" not in model["skip"]
                and "all" not in model["skip"]
            )
            or ("skip" not in model)
            else False
        )
        if doNotSkip:
            _print(
                modelName=f'{model["name"]}',
                message="generating domain service for #modelName",
                innerDepth=2,
            )
            dirPath = f'{domainModelFullPath}/{model["path"]}'
            _createDir(dirPath)
            domainServiceFileName = (
                f'{Util.snakeCaseToUpperCameCaseString(string=model["name"])}Service'
            )
            renderedTemplate = modelTemplates.render(
                model=model, segment=Config.configData["segment"]
            )
            skipGeneratingFile = False
            if ("file_overwrite" not in model) or (
                "file_overwrite" in model and model["file_overwrite"] is False
            ):
                if _isManuallyModified(
                    fileFullPath=f"{dirPath}/{domainServiceFileName}.py",
                    templateString=renderedTemplate,
                ):
                    _print(
                        modelName="",
                        message=f":locked: the current file {dirPath}/{domainServiceFileName}.py is different from the template, enable file_overwrite to overwrite it",
                        innerDepth=3,
                        error=True,
                    )
                    skipGeneratingFile = True
            if not skipGeneratingFile:
                isGenerated = True
                with open(f"{dirPath}/{domainServiceFileName}.py", "w+") as file:
                    file.write(renderedTemplate)
                    file.write("\n")
                _print(
                    modelName=f'{model["name"]}',
                    message=f"generating {dirPath}/{domainServiceFileName}.py for #modelName",
                    innerDepth=3,
                )

        if isGenerated:
            _print(modelName="", message="done :thumbs_up:", innerDepth=1)
        else:
            _print(
                modelName=model["name"],
                message="nothing is generated for #modelName :frog:",
                innerDepth=1,
            )


# Generate domain model repositories
def generateDomainModelRepository():
    _print(modelName="", message=":gear: Generating domain model repositories")
    domainModelPath = Config.configData["global"]["path"]["domain_model"]
    domainModelFullPath = f"{Config.projectPath}/{domainModelPath}"
    _createDir(path=domainModelFullPath)
    # Generate repository domain model path from the config
    _generateDomainModelRepositoryForConfigDomainModelPath(domainModelFullPath)
    # Generate repository for lookup path from the config
    applicationPath = Config.configData["global"]["path"]["application"]
    applicationFullPath = f"{Config.projectPath}/{applicationPath}"
    _generateRepositoryForConfigLookupPath(applicationFullPath)

def _generateRepositoryForConfigLookupPath(applicationFullPath):
    if 'lookup' not in Config.configData:
        return

    for lookupConfig in Config.configData["lookup"]:
        for lookupData in lookupConfig["data"]:
            model = lookupData['model']
            isGenerated = False
            # Do not generate code for the foreign model
            doNotSkip = (
                True
                if (
                      "skip" in model
                      and "app_service" not in model["skip"]
                      and "all" not in model["skip"]
                   )
                   or ("skip" not in model)
                else False
            )
            if doNotSkip:
                fileNamePrefix = Util.snakeCaseToUpperCameCaseString(model["name"])
                modelFullPath = f'{applicationFullPath}/{model["path"]}'
                _createDir(modelFullPath)
                template = jinjaEnv.get_template(f"application/lookup/repository.jinja2")
                foreignTemplate = jinjaEnv.get_template(f"application/lookup/foreign_repository.jinja2")
                if model['foreign']:
                    renderedTemplate = foreignTemplate.render(model=model)
                else:
                    renderedTemplate = template.render(model=model)
                skipGeneratingFile = False
                if ("file_overwrite" not in model) or (
                        "file_overwrite" in model and model["file_overwrite"] is False
                ):
                    if _isManuallyModified(
                            fileFullPath=f"{modelFullPath}/{fileNamePrefix}Repository.py",
                            templateString=renderedTemplate,
                    ):
                        _print(
                            modelName="",
                            message=f":locked: the current file {modelFullPath}/{fileNamePrefix}Repository.py is different from the template, enable file_overwrite to overwrite it",
                            innerDepth=1,
                            error=True,
                        )
                        skipGeneratingFile = True
                if not skipGeneratingFile:
                    isGenerated = True
                    with open(
                            f"{modelFullPath}/{fileNamePrefix}Repository.py", "w+"
                    ) as file:
                        file.write(renderedTemplate)
                        file.write("\n")
                    _print(
                        modelName=f'{model["name"]}',
                        message=f"generating {modelFullPath}/{fileNamePrefix}Repository.py",
                        innerDepth=1,
                    )
            if isGenerated:
                _print(
                    modelName=model["name"],
                    message="done generating code for #modelName :thumbs_up:",
                    innerDepth=1,
                )
            else:
                _print(
                    modelName=model["name"],
                    message="nothing is generated for #modelName :frog:",
                    innerDepth=1,
                )

def _generateDomainModelRepositoryForConfigDomainModelPath(domainModelFullPath):
    modelTemplates = jinjaEnv.get_template(f"domain_model/repository/segment.jinja2")

    for modelConfig in Config.configData["domain_model"]:
        isGenerated = False
        model = modelConfig["model"]
        doNotSkip = (
            True
            if (
                "skip" in model
                and "domain_repository" not in model["skip"]
                and "all" not in model["skip"]
            )
            or ("skip" not in model)
            else False
        )
        if doNotSkip:
            _print(
                modelName=f'{model["name"]}',
                message="generating domain repository for #modelName",
                innerDepth=2,
            )
            dirPath = f'{domainModelFullPath}/{model["path"]}'
            _createDir(dirPath)
            domainRepositoryFileName = (
                f'{Util.snakeCaseToUpperCameCaseString(string=model["name"])}Repository'
            )
            renderedTemplate = modelTemplates.render(
                model=model, segment=Config.configData["segment"]
            )
            skipGeneratingFile = False
            if ("file_overwrite" not in model) or (
                "file_overwrite" in model and model["file_overwrite"] is False
            ):
                if _isManuallyModified(
                    fileFullPath=f"{dirPath}/{domainRepositoryFileName}.py",
                    templateString=renderedTemplate,
                ):
                    _print(
                        modelName="",
                        message=f":locked: the current file {dirPath}/{domainRepositoryFileName}.py is different from the template, enable file_overwrite to overwrite it",
                        innerDepth=3,
                        error=True,
                    )
                    skipGeneratingFile = True
            if not skipGeneratingFile:
                isGenerated = True
                with open(f"{dirPath}/{domainRepositoryFileName}.py", "w+") as file:
                    file.write(renderedTemplate)
                    file.write("\n")
                _print(
                    modelName=f'{model["name"]}',
                    message=f"generating {dirPath}/{domainRepositoryFileName}.py for #modelName",
                    innerDepth=3,
                )

        if isGenerated:
            _print(modelName="", message="done :thumbs_up:", innerDepth=1)
        else:
            _print(
                modelName=model["name"],
                message="nothing is generated for #modelName :frog:",
                innerDepth=1,
            )


# Generate domain models classes
def generateDomainModel():
    _print(modelName="", message=":gear: Generating domain models")
    tabSize = Config.configData["global"]["setting"]["tab_size"]
    domainModelPath = Config.configData["global"]["path"]["domain_model"]
    exceptionPath = Config.configData["global"]["path"]["exception"]
    exceptionFullPath = f"{Config.projectPath}/{exceptionPath}"
    domainModelFullPath = f"{Config.projectPath}/{domainModelPath}"
    applicationPath = Config.configData["global"]["path"]["application"]
    applicationFullPath = f"{Config.projectPath}/{applicationPath}"
    _createDir(path=applicationFullPath)
    _createDir(path=domainModelFullPath)

    _generateDomainModelForConfigDomainModelPath(
        domainModelFullPath=domainModelFullPath,
        exceptionFullPath=exceptionFullPath,
        tabSize=tabSize)

    _generateDomainModelLookupForConfigLookupPath(applicationFullPath)

def _generateDomainModelLookupForConfigLookupPath(applicationFullPath):
    if 'lookup' not in Config.configData:
        return
    for lookupConfig in Config.configData["lookup"]:
        for lookupData in lookupConfig["data"]:
            model = lookupData['model']
            isGenerated = False
            # Do not generate code for the foreign model
            doNotSkip = (
                True
                if (
                      "skip" in model
                      and "app_service" not in model["skip"]
                      and "all" not in model["skip"]
                   )
                   or ("skip" not in model)
                else False
            )
            if doNotSkip:
                fileNamePrefix = Util.snakeCaseToUpperCameCaseString(model["name"])
                modelFullPath = f'{applicationFullPath}/{model["path"]}'
                _createDir(modelFullPath)
                template = jinjaEnv.get_template(f"application/lookup/model.jinja2")
                foreignTemplate = jinjaEnv.get_template(f"application/lookup/model.jinja2")
                if model["foreign"]:
                    renderedTemplate = foreignTemplate.render(model=model)
                else:
                    renderedTemplate = template.render(model=model)

                skipGeneratingFile = False
                if ("file_overwrite" not in model) or (
                        "file_overwrite" in model and model["file_overwrite"] is False
                ):
                    if _isManuallyModified(
                            fileFullPath=f"{modelFullPath}/{fileNamePrefix}.py",
                            templateString=renderedTemplate,
                    ):
                        _print(
                            modelName="",
                            message=f":locked: the current file {modelFullPath}/{fileNamePrefix}.py is different from the template, enable file_overwrite to overwrite it",
                            innerDepth=1,
                            error=True,
                        )
                        skipGeneratingFile = True
                if not skipGeneratingFile:
                    isGenerated = True
                    with open(
                            f"{modelFullPath}/{fileNamePrefix}.py", "w+"
                    ) as file:
                        file.write(renderedTemplate)
                        file.write("\n")
                    _print(
                        modelName=f'{model["name"]}',
                        message=f"generating {modelFullPath}/{fileNamePrefix}.py",
                        innerDepth=1,
                    )
            if isGenerated:
                _print(
                    modelName=model["name"],
                    message="done generating code for #modelName :thumbs_up:",
                    innerDepth=1,
                )
            else:
                _print(
                    modelName=model["name"],
                    message="nothing is generated for #modelName :frog:",
                    innerDepth=1,
                )

def _generateDomainModelForConfigDomainModelPath(domainModelFullPath, exceptionFullPath, tabSize):
    modelTemplates = [
        jinjaEnv.get_template(f"domain_model/model.jinja2"),
        jinjaEnv.get_template(f"domain_model/model_created.jinja2"),
        jinjaEnv.get_template(f"domain_model/model_deleted.jinja2"),
        jinjaEnv.get_template(f"domain_model/model_updated.jinja2"),
    ]

    for modelConfig in Config.configData["domain_model"]:
        isGenerated = False
        model = modelConfig["model"]
        doNotSkip = (
            True
            if (
                "skip" in model
                and "model" not in model["skip"]
                and "all" not in model["skip"]
            )
            or ("skip" not in model)
            else False
        )
        if doNotSkip:
            _print(
                modelName=f'{model["name"]}',
                message="generating events, repository and domain service for #modelName",
                innerDepth=2,
            )
            dirPath = f'{domainModelFullPath}/{model["path"]}'
            _createDir(dirPath)
            # Generate model, repository, events and service
            for actionFuncIndex, action in {
                0: "",
                1: "Created",
                2: "Deleted",
                3: "Updated",
            }.items():
                modelNameWithAction = f'{Util.snakeCaseToUpperCameCaseString(string=model["name"])}{action}'
                renderedTemplate = modelTemplates[actionFuncIndex].render(model=model)
                skipGeneratingFile = False
                if ("file_overwrite" not in model) or (
                    "file_overwrite" in model and model["file_overwrite"] is False
                ):
                    if _isManuallyModified(
                        fileFullPath=f"{dirPath}/{modelNameWithAction}.py",
                        templateString=renderedTemplate,
                    ):
                        _print(
                            modelName="",
                            message=f":locked: the current file {dirPath}/{modelNameWithAction}.py is different from the template, enable file_overwrite to overwrite it",
                            innerDepth=3,
                            error=True,
                        )
                        skipGeneratingFile = True
                if not skipGeneratingFile:
                    isGenerated = True
                    with open(f"{dirPath}/{modelNameWithAction}.py", "w+") as file:
                        file.write(renderedTemplate)
                        file.write("\n")
                    _print(
                        modelName=f'{model["name"]}',
                        message=f"generating {dirPath}/{modelNameWithAction}.py for #modelName",
                        innerDepth=3,
                    )

            # Generate Exceptions
            _print(
                modelName=f'{model["name"]}',
                message="generating exceptions for #modelName",
                innerDepth=2,
            )
            fileNamePrefix = Util.snakeCaseToUpperCameCaseString(model["name"])
            exceptionTemplates = [
                jinjaEnv.get_template(
                    f"domain_model/exception/model_already_exist.jinja2"
                ),
                jinjaEnv.get_template(
                    f"domain_model/exception/model_does_not_exist.jinja2"
                ),
                jinjaEnv.get_template(
                    f"domain_model/exception/update_model_failed.jinja2"
                ),
            ]
            for templateIndex, fileName in {
                0: f"{fileNamePrefix}AlreadyExistException",
                1: f"{fileNamePrefix}DoesNotExistException",
                2: f"Update{fileNamePrefix}FailedException",
            }.items():
                renderedTemplate = exceptionTemplates[templateIndex].render(model=model)
                skipGeneratingFile = False
                if ("file_overwrite" not in model) or (
                    "file_overwrite" in model and model["file_overwrite"] is False
                ):
                    if _isManuallyModified(
                        fileFullPath=f"{exceptionFullPath}/{fileName}.py",
                        templateString=renderedTemplate,
                    ):
                        _print(
                            modelName="",
                            message=f":locked: the current file {exceptionFullPath}/{fileName}.py is different from the template, enable file_overwrite to overwrite it",
                            innerDepth=3,
                            error=True,
                        )
                        skipGeneratingFile = True
                if not skipGeneratingFile:
                    isGenerated = True
                    with open(f"{exceptionFullPath}/{fileName}.py", "w+") as file:
                        file.write(renderedTemplate)
                        file.write("\n")
                    _print(
                        modelName=f'{model["name"]}',
                        message=f"generating {exceptionFullPath}/{fileName}.py",
                        innerDepth=3,
                    )
            # Add events
            _print(
                modelName=f'{model["name"]}',
                message=f"add events in {domainModelFullPath}/event/EventConstant.py file for #modelName",
            )
            spaces = " " * tabSize
            eventsString = f'\t{model["name"].upper()}_CREATED = \'{model["name"]}_created\'\n\t{model["name"].upper()}_UPDATED = \'{model["name"]}_updated\'\n\t{model["name"].upper()}_DELETED = \'{model["name"]}_deleted\'\n'.replace(
                "\t", spaces
            )
            currentEvents = ""
            with open(f"{domainModelFullPath}/event/EventConstant.py", "r+") as file:
                currentEvents = file.read()
            if currentEvents.find(eventsString) == -1:
                currentEvents = f"{currentEvents}{eventsString}"
                with open(
                    f"{domainModelFullPath}/event/EventConstant.py", "w+"
                ) as file:
                    file.write(currentEvents)
        if isGenerated:
            _print(modelName="", message="done :thumbs_up:", innerDepth=1)
        else:
            _print(
                modelName=model["name"],
                message="nothing is generated for #modelName :frog:",
                innerDepth=1,
            )


# Generate application services
def generateApplicationService():
    _print(modelName="", message=":gear: Generating application service")
    applicationPath = Config.configData["global"]["path"]["application"]
    applicationFullPath = f"{Config.projectPath}/{applicationPath}"
    _createDir(path=applicationFullPath)
    # Generate application service for domain model path from the config
    _generateApplicationServiceForConfigDomainModelPath(applicationFullPath)
    # Generate application service for lookup path from the config
    _generateApplicationServiceForConfigLookupPath(applicationFullPath)

def _generateApplicationServiceForConfigLookupPath(applicationFullPath):
    if 'lookup' not in Config.configData:
        return
    for lookupConfig in Config.configData["lookup"]:
        for lookupData in lookupConfig["data"]:
            model = lookupData['model']
            isGenerated = False
            # Do not generate code for the foreign model
            doNotSkip = (
                True
                if (
                      "skip" in model
                      and "app_service" not in model["skip"]
                      and "all" not in model["skip"]
                   )
                   or ("skip" not in model)
                else False
            )
            if doNotSkip:
                fileNamePrefix = Util.snakeCaseToUpperCameCaseString(model["name"])
                modelFullPath = f'{applicationFullPath}/{model["path"]}'
                _createDir(modelFullPath)
                template = jinjaEnv.get_template(f"application/lookup/application.jinja2")
                renderedTemplate = template.render(model=model)
                skipGeneratingFile = False
                if ("file_overwrite" not in model) or (
                        "file_overwrite" in model and model["file_overwrite"] is False
                ):
                    if _isManuallyModified(
                            fileFullPath=f"{modelFullPath}/{fileNamePrefix}ApplicationService.py",
                            templateString=renderedTemplate,
                    ):
                        _print(
                            modelName="",
                            message=f":locked: the current file {modelFullPath}/{fileNamePrefix}ApplicationService.py is different from the template, enable file_overwrite to overwrite it",
                            innerDepth=1,
                            error=True,
                        )
                        skipGeneratingFile = True
                if not skipGeneratingFile:
                    isGenerated = True
                    with open(
                            f"{modelFullPath}/{fileNamePrefix}ApplicationService.py", "w+"
                    ) as file:
                        file.write(renderedTemplate)
                        file.write("\n")
                    _print(
                        modelName=f'{model["name"]}',
                        message=f"generating {modelFullPath}/{fileNamePrefix}ApplicationService.py",
                        innerDepth=1,
                    )
            if isGenerated:
                _print(
                    modelName=model["name"],
                    message="done generating code for #modelName :thumbs_up:",
                    innerDepth=1,
                )
            else:
                _print(
                    modelName=model["name"],
                    message="nothing is generated for #modelName :frog:",
                    innerDepth=1,
                )

def _generateApplicationServiceForConfigDomainModelPath(applicationFullPath):
    for modelConfig in Config.configData["domain_model"]:
        isGenerated = False
        model = modelConfig["model"]
        doNotSkip = (
            True
            if (
                "skip" in model
                and "app_service" not in model["skip"]
                and "all" not in model["skip"]
            )
            or ("skip" not in model)
            else False
        )
        if doNotSkip:
            fileNamePrefix = Util.snakeCaseToUpperCameCaseString(model["name"])
            template = jinjaEnv.get_template(f"application/segment.jinja2")
            renderedTemplate = template.render(
                model=model, segment=Config.configData["segment"]
            )
            skipGeneratingFile = False
            if ("file_overwrite" not in model) or (
                "file_overwrite" in model and model["file_overwrite"] is False
            ):
                if _isManuallyModified(
                    fileFullPath=f"{applicationFullPath}/{fileNamePrefix}ApplicationService.py",
                    templateString=renderedTemplate,
                ):
                    _print(
                        modelName="",
                        message=f":locked: the current file {applicationFullPath}/{fileNamePrefix}ApplicationService.py is different from the template, enable file_overwrite to overwrite it",
                        innerDepth=1,
                        error=True,
                    )
                    skipGeneratingFile = True
            if not skipGeneratingFile:
                isGenerated = True
                with open(
                    f"{applicationFullPath}/{fileNamePrefix}ApplicationService.py", "w+"
                ) as file:
                    file.write(renderedTemplate)
                    file.write("\n")
                _print(
                    modelName=f'{model["name"]}',
                    message=f"generating {applicationFullPath}/{fileNamePrefix}ApplicationService.py",
                    innerDepth=1,
                )
        if isGenerated:
            _print(
                modelName=model["name"],
                message="done generating code for #modelName :thumbs_up:",
                innerDepth=1,
            )
        else:
            _print(
                modelName=model["name"],
                message="nothing is generated for #modelName :frog:",
                innerDepth=1,
            )

# Generate repositories' implementations
def generateRepositoryImplementation():
    _print(modelName="", message=":gear: Generating repository implementation")
    repositoryPath = Config.configData["global"]["path"]["repository"]
    repositoryFullPath = f"{Config.projectPath}/{repositoryPath}"
    _createDir(path=repositoryFullPath)
    _generateRepositoryImplementationForConfigDomainModelPath(repositoryFullPath)
    _generateRepositoryImplementationForConfigLookupPath(repositoryFullPath)

def _generateRepositoryImplementationForConfigLookupPath(repositoryFullPath):
    if 'lookup' not in Config.configData:
        return
    for lookupConfig in Config.configData["lookup"]:
        for lookupData in lookupConfig["data"]:
            model = lookupData['model']
            isGenerated = False
            # Do not generate code for the foreign model
            doNotSkip = (
                True
                if (
                           "skip" in model
                           and "repository_impl" not in model["skip"]
                           and "all" not in model["skip"]
                   )
                   or ("skip" not in model)
                else False
            )
            if doNotSkip:
                fileNamePrefix = Util.snakeCaseToUpperCameCaseString(model["name"])
                modelFullPath = f'{repositoryFullPath}/{model["path"]}'
                _createDir(modelFullPath)
                template = jinjaEnv.get_template(f"repository/lookup/impl/repository.jinja2")
                foreignTemplate = jinjaEnv.get_template(f"repository/lookup/impl/foreign_repository.jinja2")
                if model['foreign']:
                    renderedTemplate = foreignTemplate.render(model=model)
                else:
                    renderedTemplate = template.render(model=model)

                skipGeneratingFile = False
                if ("file_overwrite" not in model) or (
                        "file_overwrite" in model and model["file_overwrite"] is False
                ):
                    if _isManuallyModified(
                            fileFullPath=f"{modelFullPath}/{fileNamePrefix}RepositoryImpl.py",
                            templateString=renderedTemplate,
                    ):
                        _print(
                            modelName="",
                            message=f":locked: the current file {modelFullPath}/{fileNamePrefix}RepositoryImpl.py is different from the template, enable file_overwrite to overwrite it",
                            innerDepth=1,
                            error=True,
                        )
                        skipGeneratingFile = True
                if not skipGeneratingFile:
                    isGenerated = True
                    with open(
                            f"{modelFullPath}/{fileNamePrefix}RepositoryImpl.py", "w+"
                    ) as file:
                        file.write(renderedTemplate)
                        file.write("\n")
                    _print(
                        modelName=f'{model["name"]}',
                        message=f"generating {modelFullPath}/{fileNamePrefix}RepositoryImpl.py",
                        innerDepth=1,
                    )
            if isGenerated:
                _print(
                    modelName=model["name"],
                    message="done generating code for #modelName :thumbs_up:",
                    innerDepth=1,
                )
            else:
                _print(
                    modelName=model["name"],
                    message="nothing is generated for #modelName :frog:",
                    innerDepth=1,
                )

def _generateRepositoryImplementationForConfigDomainModelPath(repositoryFullPath):
    for modelConfig in Config.configData["domain_model"]:
        isGenerated = False
        model = modelConfig["model"]
        doNotSkip = (
            True
            if (
                "skip" in model
                and "repository_impl" not in model["skip"]
                and "all" not in model["skip"]
            )
            or ("skip" not in model)
            else False
        )
        if doNotSkip:
            modelRepositoryFullPath = f'{repositoryFullPath}/{model["path"]}'
            _createDir(modelRepositoryFullPath)
            fileNamePrefix = Util.snakeCaseToUpperCameCaseString(model["name"])
            template = jinjaEnv.get_template(f"repository/impl/segment.jinja2")
            renderedTemplate = template.render(
                model=model, segment=Config.configData["segment"]
            )
            skipGeneratingFile = False
            if ("file_overwrite" not in model) or (
                "file_overwrite" in model and model["file_overwrite"] is False
            ):
                if _isManuallyModified(
                    fileFullPath=f"{modelRepositoryFullPath}/{fileNamePrefix}RepositoryImpl.py",
                    templateString=renderedTemplate,
                ):
                    _print(
                        modelName="",
                        message=f":locked: the current file {modelRepositoryFullPath}/{fileNamePrefix}RepositoryImpl.py is different from the template, enable file_overwrite to overwrite it",
                        innerDepth=1,
                        error=True,
                    )
                    skipGeneratingFile = True
            if not skipGeneratingFile:
                isGenerated = True
                with open(
                    f"{modelRepositoryFullPath}/{fileNamePrefix}RepositoryImpl.py", "w+"
                ) as file:
                    file.write(renderedTemplate)
                    file.write("\n")
                _print(
                    modelName=f'{model["name"]}',
                    message=f"generating {modelRepositoryFullPath}/{fileNamePrefix}RepositoryImpl.py",
                    innerDepth=1,
                )
        if isGenerated:
            _print(
                modelName=model["name"],
                message="done generating code for #modelName :thumbs_up:",
                innerDepth=1,
            )
        else:
            _print(
                modelName=model["name"],
                message="nothing is generated for #modelName :frog:",
                innerDepth=1,
            )


# Generate db repositories
def generateDbRepository():
    _print(modelName="", message=":gear: Generating db repository")
    dbRepositoryPath = Config.configData["global"]["path"]["db_model"]
    dbRepositoryFullPath = f"{Config.projectPath}/{dbRepositoryPath}"
    _createDir(path=dbRepositoryFullPath)
    for modelConfig in Config.configData["domain_model"]:
        isGenerated = False
        model = modelConfig["model"]
        doNotSkip = (
            True
            if (
                "skip" in model
                and "db_repository" not in model["skip"]
                and "all" not in model["skip"]
            )
            or ("skip" not in model)
            else False
        )
        if doNotSkip:
            dbModelFileName = Util.snakeCaseToUpperCameCaseString(model["name"])
            template = jinjaEnv.get_template(f"repository/model_db_repository.jinja2")

            renderedTemplate = template.render(model=model)
            skipGeneratingFile = False
            if ("file_overwrite" not in model) or (
                "file_overwrite" in model and model["file_overwrite"] is False
            ):
                if _isManuallyModified(
                    fileFullPath=f"{dbRepositoryFullPath}/{dbModelFileName}.py",
                    templateString=renderedTemplate,
                ):
                    _print(
                        modelName="",
                        message=f":locked: the current file {dbRepositoryFullPath}/{dbModelFileName}.py is different from the template, enable file_overwrite to overwrite it",
                        innerDepth=1,
                        error=True,
                    )
                    skipGeneratingFile = True
            if not skipGeneratingFile:
                isGenerated = True
                with open(f"{dbRepositoryFullPath}/{dbModelFileName}.py", "w+") as file:
                    file.write(renderedTemplate)
                    file.write("\n")
                _print(
                    modelName=f'{model["name"]}',
                    message=f"generating {dbRepositoryFullPath}/{dbModelFileName}.py",
                    innerDepth=1,
                )
        if isGenerated:
            _print(
                modelName=model["name"],
                message="done generating code for #modelName :thumbs_up:",
                innerDepth=1,
            )
        else:
            _print(
                modelName=model["name"],
                message="nothing is generated for #modelName :frog:",
                innerDepth=1,
            )

# Generate es repositories
def generateEsRepository():
    if 'lookup' not in Config.configData:
        return
    _print(modelName="", message=":gear: Generating elasticsearch repository model")
    esPath = Config.configData["global"]["path"]["es_model"]
    esFullPath = f"{Config.projectPath}/{esPath}"
    _createDir(path=esFullPath)
    for lookupConfig in Config.configData["lookup"]:
        for lookupData in lookupConfig["data"]:
            model = lookupData['model']
            isGenerated = False
            # Do not generate code for the foreign model
            doNotSkip = (
                True
                if (
                      "skip" in model
                      and "es_repository" not in model["skip"]
                      and "all" not in model["skip"]
                   )
                   or ("skip" not in model)
                else False
            )
            if doNotSkip:
                fileNamePrefix = Util.snakeCaseToUpperCameCaseString(model["domain_model"]["name"])
                modelFullPath = f'{esFullPath}/{model["path"]}'
                _createDir(modelFullPath)
                template = jinjaEnv.get_template(f"repository/es/model.jinja2")
                foreignTemplate = jinjaEnv.get_template(f"repository/es/foreign_model.jinja2")
                if model['foreign']:
                    renderedTemplate = foreignTemplate.render(model=model)
                else:
                    renderedTemplate = template.render(model=model)
                skipGeneratingFile = False
                if ("file_overwrite" not in model) or (
                        "file_overwrite" in model and model["file_overwrite"] is False
                ):
                    if _isManuallyModified(
                            fileFullPath=f"{modelFullPath}/{fileNamePrefix}.py",
                            templateString=renderedTemplate,
                    ):
                        _print(
                            modelName="",
                            message=f":locked: the current file {modelFullPath}/{fileNamePrefix}.py is different from the template, enable file_overwrite to overwrite it",
                            innerDepth=1,
                            error=True,
                        )
                        skipGeneratingFile = True
                if not skipGeneratingFile:
                    isGenerated = True
                    with open(
                            f"{modelFullPath}/{fileNamePrefix}.py", "w+"
                    ) as file:
                        file.write(renderedTemplate)
                        file.write("\n")
                    _print(
                        modelName=f'{model["name"]}',
                        message=f"generating {modelFullPath}/{fileNamePrefix}.py",
                        innerDepth=1,
                    )
            if isGenerated:
                _print(
                    modelName=model["name"],
                    message="done generating code for #modelName :thumbs_up:",
                    innerDepth=1,
                )
            else:
                _print(
                    modelName=model["name"],
                    message="nothing is generated for #modelName :frog:",
                    innerDepth=1,
                )

# Generate messaging listeners
def generateMessagingListener():
    _print(modelName="", message=":gear: Generating messaging listeners")
    messageListenerPath = Config.configData["global"]["path"]["messaging_listener"]
    messageListenerFullPath = f"{Config.projectPath}/{messageListenerPath}"
    _createDir(path=messageListenerFullPath)
    _generateMessagingListenerForDomainModelConfig(messageListenerFullPath)
    _generateMessagingListenerForLookupConfig(messageListenerFullPath)

def _generateMessagingListenerForDomainModelConfig(messageListenerFullPath):
    for modelConfig in Config.configData["domain_model"]:
        isGenerated = False
        model = modelConfig["model"]
        doNotSkip = (
            True
            if (
                "skip" in model
                and "listener" not in model["skip"]
                and "all" not in model["skip"]
            )
            or ("skip" not in model)
            else False
        )
        if doNotSkip:
            _print(
                modelName=f'{model["name"]}',
                message=f"generating handlers",
                innerDepth=1,
            )
            # region Create handlers in common/handler
            commonHandlerDirFullPath = f"{messageListenerFullPath}/common/handler"
            commonModelHandlerDirFullPath = (
                f'{commonHandlerDirFullPath}/{model["path"]}'
            )
            _createDir(commonModelHandlerDirFullPath)
            templates = [
                jinjaEnv.get_template(
                    f"messaging/listener/common/create_model_handler.jinja2"
                ),
                jinjaEnv.get_template(
                    f"messaging/listener/common/delete_model_handler.jinja2"
                ),
                jinjaEnv.get_template(
                    f"messaging/listener/common/update_model_handler.jinja2"
                ),
            ]
            modelFileName = Util.snakeCaseToUpperCameCaseString(model["name"])
            for templateIndex, fileName in {
                0: f"Create{modelFileName}Handler",
                1: f"Delete{modelFileName}Handler",
                2: f"Update{modelFileName}Handler",
            }.items():
                renderedTemplate = templates[templateIndex].render(model=model)
                skipGeneratingFile = False
                if ("file_overwrite" not in model) or (
                    "file_overwrite" in model and model["file_overwrite"] is False
                ):
                    if _isManuallyModified(
                        fileFullPath=f"{commonModelHandlerDirFullPath}/{fileName}.py",
                        templateString=renderedTemplate,
                    ):
                        _print(
                            modelName="",
                            message=f":locked: the current file {commonModelHandlerDirFullPath}/{fileName}.py is different from the template, enable file_overwrite to overwrite it",
                            innerDepth=2,
                            error=True,
                        )
                        skipGeneratingFile = True
                if not skipGeneratingFile:
                    isGenerated = True
                    with open(
                        f"{commonModelHandlerDirFullPath}/{fileName}.py", "w+"
                    ) as file:
                        file.write(renderedTemplate)
                        file.write("\n")
                    _print(
                        modelName=f'{model["name"]}',
                        message=f"{commonModelHandlerDirFullPath}/{fileName}.py",
                        innerDepth=2,
                    )
            # endregion

            # region Create handlers in project_command/handler
            _print(
                modelName=f'{model["name"]}',
                message=f"generating handlers in project_command",
                innerDepth=1,
            )
            projectCommandHandlerDirFullPath = (
                f"{messageListenerFullPath}/project_command/handler"
            )
            projectModelHandlerDirFullPath = (
                f'{projectCommandHandlerDirFullPath}/{model["path"]}'
            )
            _createDir(projectModelHandlerDirFullPath)
            templates = [
                jinjaEnv.get_template(
                    f"messaging/listener/create_model_handler.jinja2"
                ),
                jinjaEnv.get_template(
                    f"messaging/listener/delete_model_handler.jinja2"
                ),
                jinjaEnv.get_template(
                    f"messaging/listener/update_model_handler.jinja2"
                ),
            ]
            modelFileName = Util.snakeCaseToUpperCameCaseString(model["name"])
            for templateIndex, fileName in {
                0: f"Create{modelFileName}Handler",
                1: f"Delete{modelFileName}Handler",
                2: f"Update{modelFileName}Handler",
            }.items():

                renderedTemplate = templates[templateIndex].render(model=model)
                skipGeneratingFile = False
                if ("file_overwrite" not in model) or (
                    "file_overwrite" in model and model["file_overwrite"] is False
                ):
                    if _isManuallyModified(
                        fileFullPath=f"{projectModelHandlerDirFullPath}/{fileName}.py",
                        templateString=renderedTemplate,
                    ):
                        _print(
                            modelName="",
                            message=f":locked: the current file {projectModelHandlerDirFullPath}/{fileName}.py is different from the template, enable file_overwrite to overwrite it",
                            innerDepth=2,
                            error=True,
                        )
                        skipGeneratingFile = True
                if not skipGeneratingFile:
                    isGenerated = True
                    with open(
                        f"{projectModelHandlerDirFullPath}/{fileName}.py", "w+"
                    ) as file:
                        file.write(renderedTemplate)
                        file.write("\n")
                    _print(
                        modelName=f'{model["name"]}',
                        message=f"{projectModelHandlerDirFullPath}/{fileName}.py",
                        innerDepth=2,
                    )
            # endregion

            # # region Create db persistence handler
            # dbPersistenceCommandHandlerDirFullPath = f'{messageListenerFullPath}/db_persistence/handler'
            # dbPersistenceModelHandlerDirFullPath = f'{dbPersistenceCommandHandlerDirFullPath}/{model["path"]}'
            # _createDir(dbPersistenceModelHandlerDirFullPath)
            # template = jinjaEnv.get_template(f'messaging/listener/db_persistence/model_handler.jinja2')
            # modelFileName = Util.snakeCaseToUpperCameCaseString(model['name'])
            # renderedTemplate = template.render(model=model)
            # skipGeneratingFile = False
            # if ('file_overwrite' not in model) or ('file_overwrite' in model and model['file_overwrite'] is False):
            #     if _isManuallyModified(fileFullPath=f'{dbPersistenceModelHandlerDirFullPath}/{modelFileName}Handler.py',
            #                            templateString=renderedTemplate):
            #         _print(modelName='',
            #                message=f':locked: the current file {dbPersistenceModelHandlerDirFullPath}/{modelFileName}Handler.py is different from the template, enable file_overwrite to overwrite it',
            #                innerDepth=1, error=True)
            #         skipGeneratingFile = True
            # if not skipGeneratingFile:
            #     isGenerated = True
            #     with open(f'{dbPersistenceModelHandlerDirFullPath}/{modelFileName}Handler.py', 'w+') as file:
            #         file.write(renderedTemplate)
            #         file.write('\n')
            #     _print(modelName=f'{model["name"]}',
            #            message=f'generating {dbPersistenceModelHandlerDirFullPath}/{modelFileName}Handler.py',
            #            innerDepth=1)
            # # endregion

            # region Add command constants
            _print(
                modelName=f'{model["name"]}',
                message=f"add command constants in {messageListenerFullPath}/CommandConstant.py",
                innerDepth=1,
            )
            _addTemplateBeforeSignatureEnd(
                fullFilePath=f"{messageListenerFullPath}/CommandConstant",
                template=jinjaEnv.get_template(f"messaging/command_constant.jinja2"),
                model=model,
                signatureStart="class CommonCommandConstant(Enum):",
                signatureEnd="@extendEnum(CommonCommandConstant)",
            )
            # endregion
        if isGenerated:
            _print(
                modelName=model["name"],
                message="done generating code for #modelName :thumbs_up:",
                innerDepth=1,
            )
        else:
            _print(
                modelName=model["name"],
                message="nothing is generated for #modelName :frog:",
                innerDepth=1,
            )

def _generateMessagingListenerForLookupConfig(messageListenerFullPath):
    if 'lookup' not in Config.configData:
        return
    for lookupConfig in Config.configData["lookup"]:
        for lookupData in lookupConfig["data"]:
            isGenerated = False
            model = lookupData["model"]
            doNotSkip = (
                True
                if (
                    "skip" in model
                    and "listener" not in model["skip"]
                    and "all" not in model["skip"]
                )
                or ("skip" not in model)
                else False
            )
            if doNotSkip:
                _print(
                    modelName=f'{model["name"]}',
                    message=f"generating handlers",
                    innerDepth=1,
                )
                # region Create handlers in common/handler
                commonHandlerDirFullPath = f"{messageListenerFullPath}/common/handler"
                commonModelHandlerDirFullPath = (
                    f'{commonHandlerDirFullPath}/{model["path"]}'
                )
                _createDir(commonModelHandlerDirFullPath)
                templates = [
                    jinjaEnv.get_template(
                        f"messaging/listener/lookup/common/create_model_handler.jinja2"
                    ),
                    jinjaEnv.get_template(
                        f"messaging/listener/lookup/common/delete_model_handler.jinja2"
                    ),
                    jinjaEnv.get_template(
                        f"messaging/listener/lookup/common/update_model_handler.jinja2"
                    ),
                ]
                modelFileName = Util.snakeCaseToUpperCameCaseString(model["name"])
                for templateIndex, fileName in {
                    0: f"Create{modelFileName}Handler",
                    1: f"Delete{modelFileName}Handler",
                    2: f"Update{modelFileName}Handler",
                }.items():
                    renderedTemplate = templates[templateIndex].render(model=model)
                    skipGeneratingFile = False
                    if ("file_overwrite" not in model) or (
                        "file_overwrite" in model and model["file_overwrite"] is False
                    ):
                        if _isManuallyModified(
                            fileFullPath=f"{commonModelHandlerDirFullPath}/{fileName}.py",
                            templateString=renderedTemplate,
                        ):
                            _print(
                                modelName="",
                                message=f":locked: the current file {commonModelHandlerDirFullPath}/{fileName}.py is different from the template, enable file_overwrite to overwrite it",
                                innerDepth=2,
                                error=True,
                            )
                            skipGeneratingFile = True
                    if not skipGeneratingFile:
                        isGenerated = True
                        with open(
                            f"{commonModelHandlerDirFullPath}/{fileName}.py", "w+"
                        ) as file:
                            file.write(renderedTemplate)
                            file.write("\n")
                        _print(
                            modelName=f'{model["name"]}',
                            message=f"{commonModelHandlerDirFullPath}/{fileName}.py",
                            innerDepth=2,
                        )
                # endregion

                # region Create handlers in project_event/handler
                _print(
                    modelName=f'{model["name"]}',
                    message=f"generating handlers in project_event",
                    innerDepth=1,
                )
                projectCommandHandlerDirFullPath = (
                    f"{messageListenerFullPath}/lookup/project_event/handler"
                )
                modelPathWithoutLookupString = model["path"].replace("lookup/", "")
                projectModelHandlerDirFullPath = (
                    f'{projectCommandHandlerDirFullPath}/{modelPathWithoutLookupString}'
                )
                _createDir(projectModelHandlerDirFullPath)
                templates = [
                    jinjaEnv.get_template(
                        f"messaging/listener/lookup/model_created_handler.jinja2"
                    ),
                    jinjaEnv.get_template(
                        f"messaging/listener/lookup/model_deleted_handler.jinja2"
                    ),
                    jinjaEnv.get_template(
                        f"messaging/listener/lookup/model_updated_handler.jinja2"
                    ),
                ]
                modelFileName = Util.snakeCaseToUpperCameCaseString(model["name"])
                for templateIndex, fileName in {
                    0: f"{modelFileName}CreatedHandler",
                    1: f"{modelFileName}DeletedHandler",
                    2: f"{modelFileName}UpdatedHandler",
                }.items():

                    renderedTemplate = templates[templateIndex].render(model=model)
                    skipGeneratingFile = False
                    if ("file_overwrite" not in model) or (
                        "file_overwrite" in model and model["file_overwrite"] is False
                    ):
                        if _isManuallyModified(
                            fileFullPath=f"{projectModelHandlerDirFullPath}/{fileName}.py",
                            templateString=renderedTemplate,
                        ):
                            _print(
                                modelName="",
                                message=f":locked: the current file {projectModelHandlerDirFullPath}/{fileName}.py is different from the template, enable file_overwrite to overwrite it",
                                innerDepth=2,
                                error=True,
                            )
                            skipGeneratingFile = True
                    if not skipGeneratingFile:
                        isGenerated = True
                        with open(
                            f"{projectModelHandlerDirFullPath}/{fileName}.py", "w+"
                        ) as file:
                            file.write(renderedTemplate)
                            file.write("\n")
                        _print(
                            modelName=f'{model["name"]}',
                            message=f"{projectModelHandlerDirFullPath}/{fileName}.py",
                            innerDepth=2,
                        )
                # endregion

            if isGenerated:
                _print(
                    modelName=model["name"],
                    message="done generating code for #modelName :thumbs_up:",
                    innerDepth=1,
                )
            else:
                _print(
                    modelName=model["name"],
                    message="nothing is generated for #modelName :frog:",
                    innerDepth=1,
                )            


# Generate protocol buffer files
def generateProtoBuffer():
    _print(modelName="", message=":gear: Generating protocol buffer files")
    protoPath = Config.configData["global"]["path"]["proto_buffer"]
    protoFullPath = f"{Config.projectPath}/{protoPath}"
    _createDir(path=protoFullPath)
    _generateProtoBufferForConfigDomainModel(protoFullPath)
    _generateProtoBufferForConfigLookup(protoFullPath)

def _generateProtoBufferForConfigDomainModel(protoFullPath):
    for modelConfig in Config.configData["domain_model"]:
        isGenerated = False
        model = modelConfig["model"]
        doNotSkip = (
            True
            if (
                "skip" in model
                and "proto" not in model["skip"]
                and "all" not in model["skip"]
            )
            or ("skip" not in model)
            else False
        )
        
        if doNotSkip:
            modelProtoName = f'{protoFullPath}/{model["name"]}'
            modelTemplate = jinjaEnv.get_template(f"proto/model.jinja2")
            renderedModelTemplate = modelTemplate.render(model=model)
            modelAppTemplate = jinjaEnv.get_template(f"proto/segment.jinja2")
            renderedModelAppTemplate = modelAppTemplate.render(
                model=model, segment=Config.configData["segment"]
            )
            skipGeneratingFile = False
            if ("file_overwrite" not in model) or (
                "file_overwrite" in model and model["file_overwrite"] is False
            ):
                if _isManuallyModified(
                    fileFullPath=f"{modelProtoName}.proto",
                    templateString=renderedModelTemplate,
                ):
                    _print(
                        modelName="",
                        message=f":locked: the current file {modelProtoName}.proto is different from the template, enable file_overwrite to overwrite it",
                        innerDepth=1,
                        error=True,
                    )
                    skipGeneratingFile = True
            if not skipGeneratingFile:
                isGenerated = True
                with open(f"{modelProtoName}.proto", "w+") as file:
                    file.write(renderedModelTemplate)
                    file.write("\n")
                _print(
                    modelName=f'{model["name"]}',
                    message=f"generating {modelProtoName}.proto for #modelName",
                    innerDepth=1,
                )

            skipGeneratingFile = False
            if ("file_overwrite" not in model) or (
                "file_overwrite" in model and model["file_overwrite"] is False
            ):
                if _isManuallyModified(
                    fileFullPath=f"{modelProtoName}_app_service.proto",
                    templateString=renderedModelAppTemplate,
                ):
                    _print(
                        modelName="",
                        message=f":locked: the current file {modelProtoName}_app_service.proto is different from the template, enable file_overwrite to overwrite it",
                        innerDepth=1,
                        error=True,
                    )
                    skipGeneratingFile = True
            if not skipGeneratingFile:
                isGenerated = True
                with open(f"{modelProtoName}_app_service.proto", "w+") as file:
                    file.write(renderedModelAppTemplate)
                    file.write("\n")
                _print(
                    modelName=f'{model["name"]}',
                    message=f"generating {modelProtoName}_app_service.proto for #modelName",
                    innerDepth=1,
                )
        if isGenerated:
            _print(
                modelName=model["name"],
                message="done generating code for #modelName :thumbs_up:",
                innerDepth=1,
            )
        else:
            _print(
                modelName=model["name"],
                message="nothing is generated for #modelName :frog:",
                innerDepth=1,
            )

def _generateProtoBufferForConfigLookup(protoFullPath):
    if 'lookup' not in Config.configData:
        return
    packagePath = ''
    for lookupConfig in Config.configData["lookup"]:
        for item in lookupConfig["data"]:
            if not item["model"]["foreign"]:
                packagePath = item["model"]["path"]
                item["model"]["package_path"] = packagePath
                break
        if packagePath != '':
            break
    for lookupConfig in Config.configData["lookup"]:
        for lookupData in lookupConfig["data"]:
            isGenerated = False
            model = lookupData["model"]
            doNotSkip = (
                True
                if (
                    "skip" in model
                    and "proto" not in model["skip"]
                    and "all" not in model["skip"]
                )
                or ("skip" not in model)
                else False
            )
            if doNotSkip:
                _createDir(path=f'{protoFullPath}/{model["path"]}')
                modelProtoName = f'{protoFullPath}/{model["path"]}/{model["name"]}'
                modelTemplate = jinjaEnv.get_template(f"proto/lookup/model.jinja2")
                modelAppTemplate = jinjaEnv.get_template(f"proto/lookup/model_app.jinja2")
                renderedModelAppTemplate = modelAppTemplate.render(model=model)

                # Generate for non-foreign models
                model["package_path"] = packagePath
                isGenerated |= _renderProtoModel(modelTemplate=modelTemplate,
                                  modelItem=model,
                                  model=model,
                                  modelProtoName=modelProtoName)
                # Generate for foreign models
                for modelField in model['field']:
                    if modelField['type'] != 'foreign':
                        continue
                    modelItem = modelField['link']
                    modelProtoName = f'{protoFullPath}/{modelItem["path"]}/{modelItem["name"]}'
                    model["package_path"] = packagePath
                    isGenerated |= _renderProtoModel(modelTemplate=modelTemplate,
                                      modelItem=modelItem,
                                      model=model,
                                      modelProtoName=modelProtoName)


                # Generate for non-foreign app service
                if model['foreign']:
                    continue
                modelProtoName = f'{protoFullPath}/{model["path"]}/{model["name"]}'
                skipGeneratingFile = False
                if ("file_overwrite" not in model) or (
                    "file_overwrite" in model and model["file_overwrite"] is False
                ):
                    if _isManuallyModified(
                        fileFullPath=f"{modelProtoName}_app_service.proto",
                        templateString=renderedModelAppTemplate,
                    ):
                        _print(
                            modelName="",
                            message=f":locked: the current file {modelProtoName}_app_service.proto is different from the template, enable file_overwrite to overwrite it",
                            innerDepth=1,
                            error=True,
                        )
                        skipGeneratingFile = True
                if not skipGeneratingFile:
                    isGenerated = True
                    with open(f"{modelProtoName}_app_service.proto", "w+") as file:
                        file.write(renderedModelAppTemplate)
                        file.write("\n")
                    _print(
                        modelName=f'{model["name"]}',
                        message=f"generating {modelProtoName}_app_service.proto for #modelName",
                        innerDepth=1,
                    )
            if isGenerated:
                _print(
                    modelName=model["name"],
                    message="done generating code for #modelName :thumbs_up:",
                    innerDepth=1,
                )
            else:
                _print(
                    modelName=model["name"],
                    message="nothing is generated for #modelName :frog:",
                    innerDepth=1,
                )

def _renderProtoModel(modelTemplate, modelItem, model, modelProtoName):
    isGenerated = False
    renderedModelTemplate = modelTemplate.render(model=modelItem)
    skipGeneratingFile = False
    if ("file_overwrite" not in model) or (
            "file_overwrite" in model and model["file_overwrite"] is False
    ):
        if _isManuallyModified(
                fileFullPath=f"{modelProtoName}.proto",
                templateString=renderedModelTemplate,
        ):
            _print(
                modelName="",
                message=f":locked: the current file {modelProtoName}.proto is different from the template, enable file_overwrite to overwrite it",
                innerDepth=1,
                error=True,
            )
            skipGeneratingFile = True
    if not skipGeneratingFile:
        isGenerated = True
        with open(f"{modelProtoName}.proto", "w+") as file:
            file.write(renderedModelTemplate)
            file.write("\n")
        _print(
            modelName=f'{modelItem["name"]}',
            message=f"generating {modelProtoName}.proto for #modelName",
            innerDepth=1,
        )
    return isGenerated

# Generate grpc listener files
def generateGrpcApi():
    _print(modelName="", message=":gear: Generating grpc")
    grpcPath = Config.configData["global"]["path"]["grpc_api_listener"]
    grpcFullPath = f"{Config.projectPath}/{grpcPath}"
    _createDir(path=grpcFullPath)
    _generateGrpcForConfigDomainModel(grpcFullPath)
    _generateGrpcForConfigLookup(grpcFullPath)

def _generateGrpcForConfigLookup(grpcFullPath):
    if 'lookup' not in Config.configData:
        return
    for lookupConfig in Config.configData["lookup"]:
        for lookupData in lookupConfig["data"]:
            isGenerated = False
            model = lookupData['model']
            if model['foreign']:
                continue
            _print(
                modelName=f'{model["name"]}',
                message="work in progress for #modelName",
                innerDepth=1,
            )
            doNotSkip = (
                True
                if (
                    "skip" in model
                    and "grpc" not in model["skip"]
                    and "all" not in model["skip"]
                )
                or ("skip" not in model)
                else False
            )
            if doNotSkip:
                modelGrpcName = f'{grpcFullPath}/lookup/{Util.snakeCaseToUpperCameCaseString(model["name"])}AppServiceListener'
                modelTemplate = jinjaEnv.get_template(f"grpc/lookup/model.jinja2")
                renderedTemplate = modelTemplate.render(model=model)
                if ("file_overwrite" not in model) or (
                    "file_overwrite" in model and model["file_overwrite"] is False
                ):
                    if _isManuallyModified(
                        fileFullPath=f"{modelGrpcName}.py", templateString=renderedTemplate
                    ):
                        _print(
                            modelName="",
                            message=f":locked: the current file {modelGrpcName}.py is different from the template, enable file_overwrite to overwrite it",
                            innerDepth=1,
                            error=True,
                        )
                        continue

                isGenerated = True
                _print(
                    modelName=f'{model["name"]}',
                    message=f"generating {modelGrpcName}.py",
                    innerDepth=2,
                )
                with open(f"{modelGrpcName}.py", "w+") as file:
                    file.write(renderedTemplate)
                    file.write("\n")
            if isGenerated:
                _print(
                    modelName=model["name"],
                    message="done generating code for #modelName :thumbs_up:",
                    innerDepth=1,
                )
            else:
                _print(
                    modelName=model["name"],
                    message="nothing is generated for #modelName :frog:",
                    innerDepth=1,
                )

def _generateGrpcForConfigDomainModel(grpcFullPath):
    for modelConfig in Config.configData["domain_model"]:
        isGenerated = False
        model = modelConfig["model"]
        _print(
            modelName=f'{model["name"]}',
            message="work in progress for #modelName",
            innerDepth=1,
        )
        doNotSkip = (
            True
            if (
                "skip" in model
                and "grpc" not in model["skip"]
                and "all" not in model["skip"]
            )
            or ("skip" not in model)
            else False
        )
        if doNotSkip:
            modelGrpcName = f'{grpcFullPath}/{Util.snakeCaseToUpperCameCaseString(model["name"])}AppServiceListener'
            modelTemplate = jinjaEnv.get_template(f"grpc/segment.jinja2")
            renderedTemplate = modelTemplate.render(
                model=model, segment=Config.configData["segment"]
            )
            if ("file_overwrite" not in model) or (
                "file_overwrite" in model and model["file_overwrite"] is False
            ):
                if _isManuallyModified(
                    fileFullPath=f"{modelGrpcName}.py", templateString=renderedTemplate
                ):
                    _print(
                        modelName="",
                        message=f":locked: the current file {modelGrpcName}.py is different from the template, enable file_overwrite to overwrite it",
                        innerDepth=1,
                        error=True,
                    )
                    continue

            isGenerated = True
            _print(
                modelName=f'{model["name"]}',
                message=f"generating {modelGrpcName}.py",
                innerDepth=2,
            )
            with open(f"{modelGrpcName}.py", "w+") as file:
                file.write(renderedTemplate)
                file.write("\n")
        if isGenerated:
            _print(
                modelName=model["name"],
                message="done generating code for #modelName :thumbs_up:",
                innerDepth=1,
            )
        else:
            _print(
                modelName=model["name"],
                message="nothing is generated for #modelName :frog:",
                innerDepth=1,
            )


# Generate model test files
def generateTest():
    _print(modelName="", message=":gear: Generating test files")
    testPath = Config.configData["global"]["path"]["test"]
    testFullPath = f"{Config.projectPath}/{testPath}"
    _createDir(path=testFullPath)
    for modelConfig in Config.configData["domain_model"]:
        isGenerated = False
        model = modelConfig["model"]
        doNotSkip = (
            True
            if (
                "skip" in model
                and "test" not in model["skip"]
                and "all" not in model["skip"]
            )
            or ("skip" not in model)
            else False
        )
        if doNotSkip:
            modelTestDirFullPath = f'{testFullPath}/domain_model/{model["path"]}'
            modelTestName = f'{modelTestDirFullPath}/test_{model["name"]}'
            _createDir(path=modelTestDirFullPath)
            testTemplate = jinjaEnv.get_template(f"test/model.jinja2")
            renderedTemplate = testTemplate.render(model=model)
            if ("file_overwrite" not in model) or (
                "file_overwrite" in model and model["file_overwrite"] is False
            ):
                if _isManuallyModified(
                    fileFullPath=f"{modelTestName}.py", templateString=renderedTemplate
                ):
                    _print(
                        modelName="",
                        message=f":locked: the current file {modelTestName}.py is different from the template, enable file_overwrite to overwrite it",
                        innerDepth=1,
                        error=True,
                    )
                    continue

            isGenerated = True
            _print(modelName="", message=f"generating {modelTestName}.py", innerDepth=1)
            with open(f"{modelTestName}.py", "w+") as file:
                file.write(renderedTemplate)
                file.write("\n")

        if isGenerated:
            _print(
                modelName=model["name"],
                message="done generating code for #modelName :thumbs_up:",
                innerDepth=1,
            )
        else:
            _print(
                modelName=model["name"],
                message="nothing is generated for #modelName :frog:",
                innerDepth=1,
            )

# Generate application dependency injection methods
def generateAppDi():
    _print(modelName="", message=":gear: Generating app dependency injection data")
    appDiPath = Config.configData["global"]["path"]["app_di"]
    tabSize = Config.configData["global"]["setting"]["tab_size"]
    appDiFullPath = f"{Config.projectPath}/{appDiPath}"
    _createDir(path=appDiFullPath)
    _generateAppDiForDomainModelConfig(appDiFullPath)
    _generateAppDiForLookupConfig(appDiFullPath)

def _generateAppDiForDomainModelConfig(appDiFullPath):
    for modelConfig in Config.configData["domain_model"]:
        isGenerated = False
        model = modelConfig["model"]
        doNotSkip = (
            True
            if (
                "skip" in model
                and "app_di" not in model["skip"]
                and "all" not in model["skip"]
            )
            or ("skip" not in model)
            else False
        )
        if doNotSkip:
            isGenerated = True
            _print(
                modelName=f'{model["name"]}',
                message=f"updating {appDiFullPath}/AppDi.py for #modelName",
                innerDepth=1,
            )
            appDiName = f"{appDiFullPath}/AppDi"
            appServiceDataList = [
                {
                    "template": jinjaEnv.get_template(f"app_di/app_service.jinja2"),
                    "signature": "# region Application service",
                },
                {
                    "template": jinjaEnv.get_template(f"app_di/repository.jinja2"),
                    "signature": "# region Repository",
                },
                {
                    "template": jinjaEnv.get_template(f"app_di/domain_service.jinja2"),
                    "signature": "# region Domain service",
                },
            ]
            for data in appServiceDataList:
                _addTemplateBeforeSignatureEnd(
                    fullFilePath=appDiName,
                    template=data["template"],
                    model=model,
                    signatureStart=data["signature"],
                    signatureEnd="# endregion",
                )
            _addTemplateBeforeSignatureEnd(
                fullFilePath=appDiName,
                template=jinjaEnv.get_template(f"app_di/import.jinja2"),
                model=model,
                signatureStart="from sqlalchemy.ext.declarative.api import DeclarativeMeta, declarative_base",
                signatureEnd="DbBase = DeclarativeMeta",
            )
        if isGenerated:
            _print(
                modelName=model["name"],
                message="done generating code for #modelName :thumbs_up:",
                innerDepth=1,
            )
        else:
            _print(
                modelName=model["name"],
                message="nothing is generated for #modelName :frog:",
                innerDepth=1,
            )

def _generateAppDiForLookupConfig(appDiFullPath):
    if 'lookup' not in Config.configData:
        return
    for modelConfig in Config.configData["lookup"]:
        for item in modelConfig["data"]:
            isGenerated = False
            model = item["model"]
            model['is_lookup'] = True
            doNotSkip = (
                True
                if (
                    "skip" in model
                    and "app_di" not in model["skip"]
                    and "all" not in model["skip"]
                )
                or ("skip" not in model)
                else False
            )
            if doNotSkip:
                isGenerated = True
                _print(
                    modelName=f'{model["name"]}',
                    message=f"updating {appDiFullPath}/AppDi.py for #modelName",
                    innerDepth=1,
                )
                appDiName = f"{appDiFullPath}/AppDi"
                appServiceDataList = [
                    {
                        "template": jinjaEnv.get_template(f"app_di/app_service.jinja2"),
                        "signature": "# region Application service",
                    },
                    {
                        "template": jinjaEnv.get_template(f"app_di/repository.jinja2"),
                        "signature": "# region Repository",
                    }
                ]
                for data in appServiceDataList:
                    _addTemplateBeforeSignatureEnd(
                        fullFilePath=appDiName,
                        template=data["template"],
                        model=model,
                        signatureStart=data["signature"],
                        signatureEnd="# endregion",
                    )
                _addTemplateBeforeSignatureEnd(
                    fullFilePath=appDiName,
                    template=jinjaEnv.get_template(f"app_di/import.jinja2"),
                    model=model,
                    signatureStart="from sqlalchemy.ext.declarative.api import DeclarativeMeta, declarative_base",
                    signatureEnd="DbBase = DeclarativeMeta",
                )
            if isGenerated:
                _print(
                    modelName=model["name"],
                    message="done generating code for #modelName :thumbs_up:",
                    innerDepth=1,
                )
            else:
                _print(
                    modelName=model["name"],
                    message="nothing is generated for #modelName :frog:",
                    innerDepth=1,
                )


def _isManuallyModified(fileFullPath, templateString) -> bool:
    data = None
    if os.path.exists(fileFullPath):
        with open(fileFullPath, "r") as file:
            data = file.read()
    return data is not None and data.strip() != templateString.strip()


def _addTemplateBeforeSignatureEnd(
    fullFilePath, template, model, signatureStart, signatureEnd
):
    tabSize = Config.configData["global"]["setting"]["tab_size"]
    renderedTemplate = template.render(model=model)
    spaces = " " * tabSize
    spacedRenderedTemplate = renderedTemplate.replace("\t", spaces)
    fileLines = []
    currentContent = ""
    with open(f"{fullFilePath}.py", "r+") as file:
        fileLines = file.readlines()
        file.seek(0)
        currentContent = file.read()
    with open(f"{fullFilePath}.py", "w+") as file:
        if currentContent.find(spacedRenderedTemplate.strip()) == -1:
            for signatureStartIndex in range(0, len(fileLines)):
                if fileLines[signatureStartIndex].find(signatureStart) != -1:
                    for signatureEndIndex in range(
                        signatureStartIndex + 1, len(fileLines)
                    ):
                        if fileLines[signatureEndIndex].find(signatureEnd) != -1:
                            fileLines.insert(
                                signatureEndIndex - 1, f"{spacedRenderedTemplate}\n"
                            )
                            break
                    break
        file.writelines(fileLines)


def _print(
    modelName: str = None, message: str = None, innerDepth: int = 0, error: bool = False
):
    colorIndex = {
        0: FrontTextTerminalColor.MAGENTA,
        1: FrontTextTerminalColor.CYAN,
        2: FrontTextTerminalColor.BLUE,
        3: FrontTextTerminalColor.YELLOW,
        4: FrontTextTerminalColor.LIGHT_BLUE,
        5: FrontTextTerminalColor.RED,
    }
    modelString = f"{FrontTextTerminalColor.GREEN}{FrontTextTerminalColor.BOLD}{modelName}{FrontTextTerminalColor.RESET}"
    messageString = message.replace("#modelName", modelString)
    selectedIndex = innerDepth
    if error:
        selectedIndex = 5
    if innerDepth > 0:
        messageString = f"{FrontTextTerminalColor.RESET}{colorIndex[selectedIndex]}{messageString}{FrontTextTerminalColor.RESET}"
        tabs = "\t" * innerDepth
        print(emoji.emojize(f"{tabs}---> {messageString}"))
    else:
        print(
            emoji.emojize(
                f"{FrontTextTerminalColor.RESET}{FrontTextTerminalColor.UNDERLINE_ON}{FrontTextTerminalColor.MAGENTA}{messageString}{FrontTextTerminalColor.RESET}"
            )
        )


def _createDir(path: str):
    os.makedirs(path, exist_ok=True)
    Path(f"{path}/__init__.py").touch()


# region jinja filters
def funcParamsJinjaFilter(value, defaultNone=False):
    res = []
    if defaultNone:
        res = map(
            lambda x: f'{Util.snakeCaseToLowerCameCaseString(x["name"])}: {x["type"]} = None',
            value,
        )
    else:
        res = map(
            lambda x: f'{Util.snakeCaseToLowerCameCaseString(x["name"])}: {x["type"]} = {x["default"]}',
            value,
        )
    return ", ".join(list(res))


def funcArgsLowerKeyJinjaFilter(
    value, objectName=None, objectType=None, sign="=", defaultNone=False
):
    res = ""
    if objectName is not None:
        if objectType == "function":
            res = map(
                lambda x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{objectName}.{x["name"]}()',
                value,
            )
        elif objectType == "dictionary":
            if defaultNone:
                res = map(
                    lambda x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{objectName}["{x["name"]}"] if "{x["name"]}" in {objectName} else None',
                    value,
                )
            else:
                res = map(
                    lambda x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{objectName}["{x["name"]}"]',
                    value,
                )
        else:
            res = map(
                lambda x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{objectName}.{x["name"]}',
                value,
            )
    else:
        res = map(
            lambda x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{x["name"]}',
            value,
        )
    joinedString = ",\n\t\t\t".join(list(res))
    return f"\n\t\t\t{joinedString}" if res != "" else res


def funcArgsLowerValueJinjaFilter(value, objectName=None, objectType=None, sign="="):
    if objectName is not None:
        if objectType == "function":
            res = map(
                lambda x: f'{_argKey(x["name"], sign)}{sign}{objectName}.{Util.snakeCaseToLowerCameCaseString(x["name"])}()',
                value,
            )
        elif objectType == "dictionary":
            res = map(
                lambda x: f'{_argKey(x["name"], sign)}{sign}{objectName}["{Util.snakeCaseToLowerCameCaseString(x["name"])}"]',
                value,
            )
        else:
            res = map(
                lambda x: f'{_argKey(x["name"], sign)}{sign}{objectName}.{Util.snakeCaseToLowerCameCaseString(x["name"])}',
                value,
            )
    else:
        res = map(
            lambda x: f'{_argKey(x["name"], sign)}{sign}{Util.snakeCaseToLowerCameCaseString(x["name"])}',
            value,
        )
    return ", ".join(list(res))


def funcArgsJinjaFilter(value, objectName=None, objectType=None, sign="=", isLeftSideLowerCamel=False):
    if objectName is not None:
        if objectType == "function":
            res = map(
                lambda x: f'{_argKey(x["name"], sign)}{sign}{objectName}.{x["name"]}()',
                value,
            )
        elif objectType == "dictionary":
            if isLeftSideLowerCamel:
                res = map(
                    lambda x: f'{_argKey(x["name"], sign, isLeftSideLowerCamel)}{sign}{objectName}["{x["name"]}"]',
                    value,
                )
            else:
                res = map(
                    lambda x: f'{_argKey(x["name"], sign)}{sign}{objectName}["{x["name"]}"]',
                    value,
                )
        else:
            res = map(
                lambda x: f'{_argKey(x["name"], sign)}{sign}{objectName}.{x["name"]}',
                value,
            )
    else:
        res = map(lambda x: f'{_argKey(x["name"], sign)}{sign}{x["name"]}', value)
    return ", ".join(list(res))


def funcArgsLowerCamelCaseJinjaFilter(
    value, objectName=None, objectType=None, sign="=", elseObjectName=None
):
    if objectName is not None:
        if objectType == "function":
            res = map(
                lambda x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{objectName}.{Util.snakeCaseToLowerCameCaseString(x["name"])}()',
                value,
            )
        elif objectType == "dictionary":
            if elseObjectName is not None:
                res = map(
                    lambda x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{objectName}["{Util.snakeCaseToLowerCameCaseString(x["name"])}"] if {Util.snakeCaseToLowerCameCaseString(x["name"])} is not None else {elseObjectName}.{Util.snakeCaseToLowerCameCaseString(x["name"])}()',
                    value,
                )
            else:
                res = map(
                    lambda x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{objectName}["{Util.snakeCaseToLowerCameCaseString(x["name"])}"]',
                    value,
                )
        else:
            res = map(
                lambda x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{objectName}.{Util.snakeCaseToLowerCameCaseString(x["name"])}',
                value,
            )
    else:
        if elseObjectName is not None:
            res = map(
                lambda x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{Util.snakeCaseToLowerCameCaseString(x["name"])} if {Util.snakeCaseToLowerCameCaseString(x["name"])} is not None else {elseObjectName}.{Util.snakeCaseToLowerCameCaseString(x["name"])}()',
                value,
            )
        else:
            res = map(
                lambda x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{Util.snakeCaseToLowerCameCaseString(x["name"])}',
                value,
            )
    joinedString = ",\n\t\t\t".join(list(res))
    return f"\n\t\t\t{joinedString}" if res != "" else res


def _argKey(string: str, sign: str, isLowerCamelCase: bool = False):
    if isLowerCamelCase:
        string = Util.snakeCaseToLowerCameCaseString(string)
        return f'"{string}"' if sign == ":" else string
    else:
        return f'"{string}"' if sign == ":" else string


def funcToMapReturnDataJinjaFilter(value):
    res = map(
        lambda x: f"'{x['name']}': self.{Util.snakeCaseToLowerCameCaseString(x['name'])}()",
        value,
    )
    return ", ".join(list(res))


def funcMapCompareJinjaFilter(value):
    res = map(
        lambda x: f"self.{Util.snakeCaseToLowerCameCaseString(x['name'])}() == other.{Util.snakeCaseToLowerCameCaseString(x['name'])}()",
        value,
    )
    return " and ".join(list(res))


def pluralizeJinjaFilter(singular):
    """Return plural form of given lowercase singular word (English only)."""

    ABERRANT_PLURAL_MAP = {
        "appendix": "appendices",
        "barracks": "barracks",
        "cactus": "cacti",
        "child": "children",
        "criterion": "criteria",
        "deer": "deer",
        "echo": "echoes",
        "elf": "elves",
        "embargo": "embargoes",
        "focus": "foci",
        "fungus": "fungi",
        "goose": "geese",
        "hero": "heroes",
        "hoof": "hooves",
        "index": "indices",
        "knife": "knives",
        "leaf": "leaves",
        "life": "lives",
        "man": "men",
        "mouse": "mice",
        "nucleus": "nuclei",
        "person": "people",
        "phenomenon": "phenomena",
        "potato": "potatoes",
        "self": "selves",
        "syllabus": "syllabi",
        "tomato": "tomatoes",
        "torpedo": "torpedoes",
        "veto": "vetoes",
        "woman": "women",
    }

    VOWELS = set("aeiou")

    if not singular:
        return ""
    plural = ABERRANT_PLURAL_MAP.get(singular)
    if plural:
        return plural
    root = singular
    try:
        if singular[-1] == "y" and singular[-2] not in VOWELS:
            root = singular[:-1]
            suffix = "ies"
        elif singular[-1] == "s":
            if singular[-2] in VOWELS:
                if singular[-3:] == "ius":
                    root = singular[:-2]
                    suffix = "i"
                else:
                    root = singular[:-1]
                    suffix = "ses"
            else:
                suffix = "es"
        elif singular[-2:] in ("ch", "sh"):
            suffix = "es"
        else:
            suffix = "s"
    except IndexError:
        suffix = "s"
    plural = root + suffix
    return plural

def singularizeJinjaFilter(plural):
    '''Singularizes English nouns.'''

    rules = [
        ['(?i)(quiz)zes$', '\\1'],
        ['(?i)(matr)ices$', '\\1ix'],
        ['(?i)(vert|ind)ices$', '\\1ex'],
        ['(?i)^(ox)en', '\\1'],
        ['(?i)(alias|status)es$', '\\1'],
        ['(?i)([octop|vir])i$', '\\1us'],
        ['(?i)(cris|ax|test)es$', '\\1is'],
        ['(?i)(shoe)s$', '\\1'],
        ['(?i)(o)es$', '\\1'],
        ['(?i)(bus)es$', '\\1'],
        ['(?i)([m|l])ice$', '\\1ouse'],
        ['(?i)(x|ch|ss|sh)es$', '\\1'],
        ['(?i)(m)ovies$', '\\1ovie'],
        ['(?i)(s)eries$', '\\1eries'],
        ['(?i)([^aeiouy]|qu)ies$', '\\1y'],
        ['(?i)([lr])ves$', '\\1f'],
        ['(?i)(tive)s$', '\\1'],
        ['(?i)(hive)s$', '\\1'],
        ['(?i)([^f])ves$', '\\1fe'],
        ['(?i)(^analy)ses$', '\\1sis'],
        ['(?i)((a)naly|(b)a|(d)iagno|(p)arenthe|(p)rogno|(s)ynop|(t)he)ses$', '\\1\\2sis'],
        ['(?i)([ti])a$', '\\1um'],
        ['(?i)(n)ews$', '\\1ews'],
        ['(?i)s$', ''],
    ];

    uncountable_words = ['equipment', 'information', 'rice', 'money', 'species', 'series', 'fish', 'sheep', 'sms'];

    irregular_words = {
        'people': 'person',
        'men': 'man',
        'children': 'child',
        'sexes': 'sex',
        'moves': 'move'
    }

    lower_cased_word = plural.lower();

    for uncountable_word in uncountable_words:
        if lower_cased_word[-1 * len(uncountable_word):] == uncountable_word:
            return plural

    for irregular in irregular_words.keys():
        match = re.search('(' + irregular + ')$', plural, re.IGNORECASE)
        if match:
            return re.sub('(?i)' + irregular + '$', match.expand('\\1')[0] + irregular_words[irregular][1:], plural)

    for rule in range(len(rules)):
        match = re.search(rules[rule][0], plural, re.IGNORECASE)
        if match:
            groups = match.groups()
            for k in range(0, len(groups)):
                if groups[k] == None:
                    rules[rule][1] = rules[rule][1].replace('\\' + str(k + 1), '')

            return re.sub(rules[rule][0], rules[rule][1], plural)

    return plural

# endregion


initGlobalConfig()
fileLoader = FileSystemLoader(Config.templatePath)
jinjaEnv = Environment(loader=fileLoader)
jinjaEnv.filters["mapFuncParams"] = funcParamsJinjaFilter
jinjaEnv.filters["mapFuncArgs"] = funcArgsJinjaFilter
jinjaEnv.filters["mapFuncArgsLowerKey"] = funcArgsLowerKeyJinjaFilter
jinjaEnv.filters["mapFuncArgsLowerValue"] = funcArgsLowerValueJinjaFilter
jinjaEnv.filters["mapFuncArgsLowerCase"] = funcArgsLowerCamelCaseJinjaFilter
jinjaEnv.filters["mapFunToMapReturnData"] = funcToMapReturnDataJinjaFilter
jinjaEnv.filters["mapFunCompare"] = funcMapCompareJinjaFilter
jinjaEnv.filters["pluralize"] = pluralizeJinjaFilter
jinjaEnv.filters["singularize"] = singularizeJinjaFilter
jinjaEnv.filters["spacedWords"] = lambda x: Util.snakeCaseToLowerSpacedWordsString(
    string=x
)
jinjaEnv.filters["upperCamelCase"] = lambda x: Util.snakeCaseToUpperCameCaseString(
    string=x
)
jinjaEnv.filters["lowerCamelCase"] = lambda x: Util.snakeCaseToLowerCameCaseString(
    string=x
)

if __name__ == "__main__":
    cli()
