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
import traceback
from pathlib import Path

import click
import yaml
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

from src.resource.common.Util import Util


# region Global config & settings
class TerminalColor:
    BLUE = "\x1b[34;21m"
    GREEN = "\x1b[32;21m"
    YELLOW = "\x1b[33;21m"
    RED = "\x1b[31;21m"
    RESET = "\x1b[0m"


class Config:
    configData = None
    projectPath = None
    templatePath = None
    configFilePath = None

    @staticmethod
    def __repr__():
        return f'{TerminalColor.GREEN}projectPath:{TerminalColor.RESET} {Config.projectPath}\n' \
               f'{TerminalColor.GREEN}templatePath:{TerminalColor.RESET} {Config.templatePath}\n' \
               f'{TerminalColor.GREEN}configFilePath:{TerminalColor.RESET} {Config.configFilePath}\n' \
               f'{TerminalColor.GREEN}configData:{TerminalColor.RESET} {json.dumps(Config.configData, indent=2)}\n'


# endregion

# region Cli commands
@click.group()
def cli():
    pass


@cli.command(help='Generate code files based on a config file')
@click.argument('config_file')
def generate(config_file):
    # Init the config data
    initConfigData(config_file)
    # Generate models
    generateDomainModel()
    # Generate application services
    generateApplicationService()
    # Generate repository
    generateRepository()
    # Generate db repository
    generateDbRepository()
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


@cli.command(help='Print config data')
@click.argument('config_file')
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
    Config.projectPath = os.path.abspath(f'{os.path.dirname(__file__)}/../../../..')
    Config.templatePath = f'{Config.projectPath}/src/resource/script/scaffold/template'
    Config.configFilePath = f'{Config.projectPath}/src/resource/script/scaffold'


# Read config yaml file
def readConfig(configFile) -> dict:
    try:
        with open(f'{Config.configFilePath}/{configFile}', 'r') as file:
            return yaml.load(file, Loader=yaml.FullLoader)
    except:
        print(traceback.format_exc())
        print('Could not read config file')
        sys.exit(1)


# Generate domain models classes
def generateDomainModel():
    tabSize = Config.configData['global']['setting']['tab_size']
    domainModelPath = Config.configData['global']['path']['domain_model']
    exceptionPath = Config.configData['global']['path']['exception']
    exceptionFullPath = f'{Config.projectPath}/{exceptionPath}'
    domainModelFullPath = f'{Config.projectPath}/{domainModelPath}'
    _createDir(path=domainModelFullPath)

    modelTemplates = [
        jinjaEnv.get_template(f'domain_model/model.jinja2'),
        jinjaEnv.get_template(f'domain_model/model_created.jinja2'),
        jinjaEnv.get_template(f'domain_model/model_deleted.jinja2'),
        jinjaEnv.get_template(f'domain_model/model_updated.jinja2'),
        jinjaEnv.get_template(f'domain_model/model_repository.jinja2'),
        jinjaEnv.get_template(f'domain_model/model_service.jinja2'),
    ]

    for modelConfig in Config.configData['domain_model']:
        model = modelConfig['model']
        doNotSkip = True if ('skip' in model and 'model' not in model['skip']) or ('skip' not in model) else False
        if doNotSkip:
            dirPath = f'{domainModelFullPath}/{model["path"]}'
            _createDir(dirPath)
            # Generate model, repository, events and service
            for actionFuncIndex, action in {0: '', 1: 'Created', 2: 'Deleted', 3: 'Updated', 4: 'Repository',
                                            5: 'Service'}.items():
                with open(f'{dirPath}/{Util.snakeCaseToUpperCameCaseString(string=model["name"])}{action}.py',
                          'w+') as file:
                    file.write(modelTemplates[actionFuncIndex].render(model=model))
                    file.write('\n')

            # Generate Exceptions
            fileNamePrefix = Util.snakeCaseToUpperCameCaseString(model['name'])
            exceptionTemplates = [
                jinjaEnv.get_template(f'domain_model/exception/model_already_exist.jinja2'),
                jinjaEnv.get_template(f'domain_model/exception/model_does_not_exist.jinja2'),
                jinjaEnv.get_template(f'domain_model/exception/update_model_failed.jinja2'),
            ]
            for templateIndex, fileName in {0: f'{fileNamePrefix}AlreadyExistException',
                                            1: f'{fileNamePrefix}DoesNotExistException',
                                            2: f'Update{fileNamePrefix}FailedException',
                                            }.items():
                with open(f'{exceptionFullPath}/{fileName}.py', 'w+') as file:
                    file.write(exceptionTemplates[templateIndex].render(model=model))
                    file.write('\n')
            # Add events
            spaces = ' ' * tabSize
            eventsString = f'\t{model["name"].upper()}_CREATED = \'{model["name"]}_created\'\n\t{model["name"].upper()}_UPDATED = \'{model["name"]}_updated\'\n\t{model["name"].upper()}_DELETED = \'{model["name"]}_deleted\'\n'.replace(
                '\t', spaces)
            currentEvents = ''
            with open(f'{domainModelFullPath}/event/EventConstant.py', 'r+') as file:
                currentEvents = file.read()
            if currentEvents.find(eventsString) == -1:
                currentEvents = f'{currentEvents}{eventsString}'
                with open(f'{domainModelFullPath}/event/EventConstant.py', 'w+') as file:
                    file.write(currentEvents)


# Generate application services
def generateApplicationService():
    applicationPath = Config.configData['global']['path']['application']
    applicationFullPath = f'{Config.projectPath}/{applicationPath}'
    _createDir(path=applicationFullPath)
    for modelConfig in Config.configData['domain_model']:
        model = modelConfig['model']
        doNotSkip = True if ('skip' in model and 'app_service' not in model['skip']) or ('skip' not in model) else False
        if doNotSkip:
            fileNamePrefix = Util.snakeCaseToUpperCameCaseString(model['name'])
            template = jinjaEnv.get_template(f'application/model_application.jinja2')
            with open(f'{applicationFullPath}/{fileNamePrefix}ApplicationService.py',
                      'w+') as file:
                file.write(template.render(model=model))
                file.write('\n')


# Generate repositories
def generateRepository():
    repositoryPath = Config.configData['global']['path']['repository']
    repositoryFullPath = f'{Config.projectPath}/{repositoryPath}'
    _createDir(path=repositoryFullPath)

    for modelConfig in Config.configData['domain_model']:
        model = modelConfig['model']
        doNotSkip = True if ('skip' in model and 'repository_impl' not in model['skip']) or (
                'skip' not in model) else False
        if doNotSkip:
            modelRepositoryFullPath = f'{repositoryFullPath}/{model["path"]}'
            _createDir(modelRepositoryFullPath)
            fileNamePrefix = Util.snakeCaseToUpperCameCaseString(model['name'])
            template = jinjaEnv.get_template(f'repository/model_repository.jinja2')
            with open(f'{modelRepositoryFullPath}/{fileNamePrefix}RepositoryImpl.py',
                      'w+') as file:
                file.write(template.render(model=model))
                file.write('\n')


# Generate db repositories
def generateDbRepository():
    dbRepositoryPath = Config.configData['global']['path']['db_model']
    dbRepositoryFullPath = f'{Config.projectPath}/{dbRepositoryPath}'
    _createDir(path=dbRepositoryFullPath)

    for modelConfig in Config.configData['domain_model']:
        model = modelConfig['model']
        doNotSkip = True if ('skip' in model and 'db_repository' not in model['skip']) or (
                'skip' not in model) else False
        if doNotSkip:
            dbModelFileName = Util.snakeCaseToUpperCameCaseString(model['name'])
            template = jinjaEnv.get_template(f'repository/model_db_repository.jinja2')
            with open(f'{dbRepositoryFullPath}/{dbModelFileName}.py',
                      'w+') as file:
                file.write(template.render(model=model))
                file.write('\n')


# Generate messaging listeners
def generateMessagingListener():
    messageListenerPath = Config.configData['global']['path']['messaging_listener']
    messageListenerFullPath = f'{Config.projectPath}/{messageListenerPath}'
    _createDir(path=messageListenerFullPath)

    for modelConfig in Config.configData['domain_model']:
        model = modelConfig['model']
        doNotSkip = True if ('skip' in model and 'listener' not in model['skip']) or ('skip' not in model) else False
        if doNotSkip:
            # region Create handlers in common/handler
            commonHandlerDirFullPath = f'{messageListenerFullPath}/common/handler'
            commonModelHandlerDirFullPath = f'{commonHandlerDirFullPath}/{model["path"]}'
            _createDir(commonModelHandlerDirFullPath)
            templates = [
                jinjaEnv.get_template(f'messaging/listener/common/create_model_handler.jinja2'),
                jinjaEnv.get_template(f'messaging/listener/common/delete_model_handler.jinja2'),
                jinjaEnv.get_template(f'messaging/listener/common/update_model_handler.jinja2'),
            ]
            modelFileName = Util.snakeCaseToUpperCameCaseString(model['name'])
            for templateIndex, fileName in {0: f'Create{modelFileName}Hanlder',
                                            1: f'Delete{modelFileName}Handler',
                                            2: f'Update{modelFileName}Handler',
                                            }.items():
                with open(f'{commonModelHandlerDirFullPath}/{fileName}.py', 'w+') as file:
                    file.write(templates[templateIndex].render(model=model))
                    file.write('\n')
            # endregion

            # region Create handlers in project_command/handler
            projectCommandHandlerDirFullPath = f'{messageListenerFullPath}/project_command/handler'
            projectModelHandlerDirFullPath = f'{projectCommandHandlerDirFullPath}/{model["path"]}'
            _createDir(projectModelHandlerDirFullPath)
            templates = [
                jinjaEnv.get_template(f'messaging/listener/create_model_handler.jinja2'),
                jinjaEnv.get_template(f'messaging/listener/delete_model_handler.jinja2'),
                jinjaEnv.get_template(f'messaging/listener/update_model_handler.jinja2'),
            ]
            modelFileName = Util.snakeCaseToUpperCameCaseString(model['name'])
            for templateIndex, fileName in {0: f'Create{modelFileName}Hanlder',
                                            1: f'Delete{modelFileName}Handler',
                                            2: f'Update{modelFileName}Handler',
                                            }.items():
                with open(f'{projectModelHandlerDirFullPath}/{fileName}.py', 'w+') as file:
                    file.write(templates[templateIndex].render(model=model))
                    file.write('\n')
            # endregion

            # region Create db persistence handler
            dbPersistenceCommandHandlerDirFullPath = f'{messageListenerFullPath}/db_persistence/handler'
            dbPersistenceModelHandlerDirFullPath = f'{dbPersistenceCommandHandlerDirFullPath}/{model["path"]}'
            _createDir(dbPersistenceModelHandlerDirFullPath)
            template = jinjaEnv.get_template(f'messaging/listener/db_persistence/model_handler.jinja2')
            modelFileName = Util.snakeCaseToUpperCameCaseString(model['name'])
            with open(f'{dbPersistenceModelHandlerDirFullPath}/{modelFileName}Handler.py', 'w+') as file:
                file.write(template.render(model=model))
                file.write('\n')
            # endregion

            # region Add command constants
            _addTemplateBeforeSignatureEnd(fullFilePath=f'{messageListenerFullPath}/CommandConstant',
                                           template=jinjaEnv.get_template(f'messaging/command_constant.jinja2'),
                                           model=model,
                                           signatureStart='class CommonCommandConstant(Enum):',
                                           signatureEnd='@extendEnum(CommonCommandConstant)'
                                           )
            # endregion


# Generate protocol buffer files
def generateProtoBuffer():
    protoPath = Config.configData['global']['path']['proto_buffer']
    protoFullPath = f'{Config.projectPath}/{protoPath}'
    _createDir(path=protoFullPath)
    for modelConfig in Config.configData['domain_model']:
        model = modelConfig['model']
        doNotSkip = True if ('skip' in model and 'proto' not in model['skip']) or ('skip' not in model) else False
        if doNotSkip:
            modelProtoName = f'{protoFullPath}/{model["name"]}'
            modelTemplate = jinjaEnv.get_template(f'proto/model.jinja2')
            modelAppTemplate = jinjaEnv.get_template(f'proto/model_app.jinja2')
            with open(f'{modelProtoName}.proto', 'w+') as file:
                file.write(modelTemplate.render(model=model))
                file.write('\n')
            with open(f'{modelProtoName}_app_service.proto', 'w+') as file:
                file.write(modelAppTemplate.render(model=model))
                file.write('\n')


# Generate grpc listener files
def generateGrpcApi():
    grpcPath = Config.configData['global']['path']['grpc_api_listener']
    grpcFullPath = f'{Config.projectPath}/{grpcPath}'
    _createDir(path=grpcFullPath)
    for modelConfig in Config.configData['domain_model']:
        model = modelConfig['model']
        doNotSkip = True if ('skip' in model and 'grpc' not in model['skip']) or ('skip' not in model) else False
        if doNotSkip:
            modelGrpcName = f'{grpcFullPath}/{Util.snakeCaseToUpperCameCaseString(model["name"])}AppServiceListener'
            modelTemplate = jinjaEnv.get_template(f'grpc/model.jinja2')
            with open(f'{modelGrpcName}.py', 'w+') as file:
                file.write(modelTemplate.render(model=model))
                file.write('\n')


# Generate model test files
def generateTest():
    testPath = Config.configData['global']['path']['test']
    testFullPath = f'{Config.projectPath}/{testPath}'
    _createDir(path=testFullPath)
    for modelConfig in Config.configData['domain_model']:
        model = modelConfig['model']
        doNotSkip = True if ('skip' in model and 'test' not in model['skip']) or ('skip' not in model) else False
        if doNotSkip:
            modelTestName = f'{testFullPath}/domain_model/test_{model["name"]}'
            testTemplate = jinjaEnv.get_template(f'test/model.jinja2')
            with open(f'{modelTestName}.py', 'w+') as file:
                file.write(testTemplate.render(model=model))
                file.write('\n')


# Generate application dependency injection methods
def generateAppDi():
    appDiPath = Config.configData['global']['path']['app_di']
    tabSize = Config.configData['global']['setting']['tab_size']
    appDiFullPath = f'{Config.projectPath}/{appDiPath}'
    _createDir(path=appDiFullPath)
    for modelConfig in Config.configData['domain_model']:
        model = modelConfig['model']
        doNotSkip = True if ('skip' in model and 'test' not in model['skip']) or ('skip' not in model) else False
        if doNotSkip:
            appDiName = f'{appDiFullPath}/AppDi'
            appServiceDataList = [
                {'template': jinjaEnv.get_template(f'app_di/app_service.jinja2'),
                 'signature': '# region Application service'},
                {'template': jinjaEnv.get_template(f'app_di/repository.jinja2'), 'signature': '# region Repository'},
                {'template': jinjaEnv.get_template(f'app_di/domain_service.jinja2'),
                 'signature': '# region Domain service'},
            ]
            for data in appServiceDataList:
                _addTemplateBeforeSignatureEnd(fullFilePath=appDiName,
                                               template=data['template'],
                                               model=model,
                                               signatureStart=data['signature'],
                                               signatureEnd='# endregion'
                                               )
            _addTemplateBeforeSignatureEnd(fullFilePath=appDiName,
                                           template=jinjaEnv.get_template(f'app_di/import.jinja2'),
                                           model=model,
                                           signatureStart='from sqlalchemy.ext.declarative.api import DeclarativeMeta, declarative_base',
                                           signatureEnd='DbBase = DeclarativeMeta'
                                           )


def _addTemplateBeforeSignatureEnd(fullFilePath, template, model, signatureStart, signatureEnd):
    tabSize = Config.configData['global']['setting']['tab_size']
    renderedTemplate = template.render(model=model)
    spaces = ' ' * tabSize
    spacedRenderedTemplate = renderedTemplate.replace('\t', spaces)
    fileLines = []
    currentContent = ''
    with open(f'{fullFilePath}.py', 'r+') as file:
        fileLines = file.readlines()
        file.seek(0)
        currentContent = file.read()
    with open(f'{fullFilePath}.py', 'w+') as file:
        if currentContent.find(spacedRenderedTemplate) == -1:
            for signatureStartIndex in range(0, len(fileLines)):
                if fileLines[signatureStartIndex].find(signatureStart) != -1:
                    for signatureEndIndex in range(signatureStartIndex + 1, len(fileLines)):
                        if fileLines[signatureEndIndex].find(signatureEnd) != -1:
                            fileLines.insert(signatureEndIndex - 1, f'{renderedTemplate}\n')
                            break
                    break
        file.writelines(fileLines)


def _createDir(path: str):
    os.makedirs(path, exist_ok=True)
    Path(f'{path}/__init__.py').touch()


# region jinja filters
def funcParamsJinjaFilter(value):
    res = map(lambda x: f'{Util.snakeCaseToLowerCameCaseString(x["name"])}: {x["type"]} = {x["default"]}', value)
    return ', '.join(list(res))


def funcArgsLowerKeyJinjaFilter(value, objectName=None, objectType=None, sign='='):
    if objectName is not None:
        if objectType == 'function':
            res = map(lambda
                          x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{objectName}.{x["name"]}()',
                      value)
        elif objectType == 'dictionary':
            res = map(lambda
                          x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{objectName}["{x["name"]}"]',
                      value)
        else:
            res = map(lambda
                          x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{objectName}.{x["name"]}',
                      value)
    else:
        res = map(lambda x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{x["name"]}', value)
    return ', '.join(list(res))


def funcArgsLowerValueJinjaFilter(value, objectName=None, objectType=None, sign='='):
    if objectName is not None:
        if objectType == 'function':
            res = map(lambda
                          x: f'{_argKey(x["name"], sign)}{sign}{objectName}.{Util.snakeCaseToLowerCameCaseString(x["name"])}()',
                      value)
        elif objectType == 'dictionary':
            res = map(lambda
                          x: f'{_argKey(x["name"], sign)}{sign}{objectName}["{Util.snakeCaseToLowerCameCaseString(x["name"])}"]',
                      value)
        else:
            res = map(lambda
                          x: f'{_argKey(x["name"], sign)}{sign}{objectName}.{Util.snakeCaseToLowerCameCaseString(x["name"])}',
                      value)
    else:
        res = map(lambda x: f'{_argKey(x["name"], sign)}{sign}{Util.snakeCaseToLowerCameCaseString(x["name"])}', value)
    return ', '.join(list(res))


def funcArgsJinjaFilter(value, objectName=None, objectType=None, sign='='):
    if objectName is not None:
        if objectType == 'function':
            res = map(lambda x: f'{_argKey(x["name"], sign)}{sign}{objectName}.{x["name"]}()', value)
        elif objectType == 'dictionary':
            res = map(lambda x: f'{_argKey(x["name"], sign)}{sign}{objectName}["{x["name"]}"]', value)
        else:
            res = map(lambda x: f'{_argKey(x["name"], sign)}{sign}{objectName}.{x["name"]}', value)
    else:
        res = map(lambda x: f'{_argKey(x["name"], sign)}{sign}{x["name"]}', value)
    return ', '.join(list(res))


def funcArgsLowerCamelCaseJinjaFilter(value, objectName=None, objectType=None, sign='='):
    if objectName is not None:
        if objectType == 'function':
            res = map(lambda
                          x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{objectName}.{Util.snakeCaseToLowerCameCaseString(x["name"])}()',
                      value)
        elif objectType == 'dictionary':
            res = map(lambda
                          x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{objectName}["{Util.snakeCaseToLowerCameCaseString(x["name"])}"]',
                      value)
        else:
            res = map(lambda
                          x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{objectName}.{Util.snakeCaseToLowerCameCaseString(x["name"])}',
                      value)
    else:
        res = map(lambda
                      x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{Util.snakeCaseToLowerCameCaseString(x["name"])}',
                  value)
    return ', '.join(list(res))


def _argKey(string: str, sign: str):
    return f'"{string}"' if sign == ':' else string


def funcToMapReturnDataJinjaFilter(value):
    res = map(lambda x: f"'{x['name']}': self.{Util.snakeCaseToLowerCameCaseString(x['name'])}()", value)
    return ', '.join(list(res))


def funcMapCompareJinjaFilter(value):
    res = map(lambda
                  x: f"self.{Util.snakeCaseToLowerCameCaseString(x['name'])}() == other.{Util.snakeCaseToLowerCameCaseString(x['name'])}()",
              value)
    return ' and '.join(list(res))


# endregion


initGlobalConfig()
fileLoader = FileSystemLoader(Config.templatePath)
jinjaEnv = Environment(loader=fileLoader)
jinjaEnv.filters['mapFuncParams'] = funcParamsJinjaFilter
jinjaEnv.filters['mapFuncArgs'] = funcArgsJinjaFilter
jinjaEnv.filters['mapFuncArgsLowerKey'] = funcArgsLowerKeyJinjaFilter
jinjaEnv.filters['mapFuncArgsLowerValue'] = funcArgsLowerValueJinjaFilter
jinjaEnv.filters['mapFuncArgsLowerCase'] = funcArgsLowerCamelCaseJinjaFilter
jinjaEnv.filters['mapFunToMapReturnData'] = funcToMapReturnDataJinjaFilter
jinjaEnv.filters['mapFunCompare'] = funcMapCompareJinjaFilter
jinjaEnv.filters['spacedWords'] = lambda x: Util.snakeCaseToLowerSpacedWordsString(string=x)
jinjaEnv.filters['upperCamelCase'] = lambda x: Util.snakeCaseToUpperCameCaseString(string=x)
jinjaEnv.filters['lowerCamelCase'] = lambda x: Util.snakeCaseToLowerCameCaseString(string=x)

if __name__ == '__main__':
    cli()
