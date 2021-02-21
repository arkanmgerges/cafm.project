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
    domainModelPath = Config.configData['globals']['paths']['domain_model']
    exceptionPath = Config.configData['globals']['paths']['exception']
    exceptionFullPath = f'{Config.projectPath}/{exceptionPath}'
    domainModelFullPath = f'{Config.projectPath}/{domainModelPath}'
    createDir(path=domainModelFullPath)

    modelTemplates = [
        jinjaEnv.get_template(f'domain_model/model.jinja2'),
        jinjaEnv.get_template(f'domain_model/model_created.jinja2'),
        jinjaEnv.get_template(f'domain_model/model_deleted.jinja2'),
        jinjaEnv.get_template(f'domain_model/model_updated.jinja2'),
        jinjaEnv.get_template(f'domain_model/model_repository.jinja2'),
        jinjaEnv.get_template(f'domain_model/model_service.jinja2'),
    ]

    for modelConfig in Config.configData['domain_models']:
        model = modelConfig['model']
        dirPath = f'{domainModelFullPath}/{model["path"]}'
        createDir(dirPath)
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


# Generate application services
def generateApplicationService():
    applicationPath = Config.configData['globals']['paths']['application']
    applicationFullPath = f'{Config.projectPath}/{applicationPath}'
    createDir(path=applicationFullPath)
    for modelConfig in Config.configData['domain_models']:
        model = modelConfig['model']
        fileNamePrefix = Util.snakeCaseToUpperCameCaseString(model['name'])
        template = jinjaEnv.get_template(f'application/model_application.jinja2')
        with open(f'{applicationFullPath}/{fileNamePrefix}ApplicationService.py',
                  'w+') as file:
            file.write(template.render(model=model))
            file.write('\n')

# Generate repositories
def generateRepository():
    repositoryPath = Config.configData['globals']['paths']['repository']
    repositoryFullPath = f'{Config.projectPath}/{repositoryPath}'
    createDir(path=repositoryFullPath)

    for modelConfig in Config.configData['domain_models']:
        model = modelConfig['model']
        modelRepositoryFullPath = f'{repositoryFullPath}/{model["name"]}'
        createDir(modelRepositoryFullPath)
        fileNamePrefix = Util.snakeCaseToUpperCameCaseString(model['name'])
        template = jinjaEnv.get_template(f'repository/model_repository.jinja2')
        with open(f'{modelRepositoryFullPath}/{fileNamePrefix}RepositoryImpl.py',
                  'w+') as file:
            file.write(template.render(model=model))
            file.write('\n')

# Generate db repositories
def generateDbRepository():
    dbRepositoryPath = Config.configData['globals']['paths']['db_model']
    dbRepositoryFullPath = f'{Config.projectPath}/{dbRepositoryPath}'
    createDir(path=dbRepositoryFullPath)

    for modelConfig in Config.configData['domain_models']:
        model = modelConfig['model']
        dbModelFileName = Util.snakeCaseToUpperCameCaseString(model['name'])
        template = jinjaEnv.get_template(f'repository/model_db_repository.jinja2')
        with open(f'{dbRepositoryFullPath}/{dbModelFileName}.py',
                  'w+') as file:
            file.write(template.render(model=model))
            file.write('\n')

# Generate messaging listeners
def generateMessagingListener():
    messageListenerPath = Config.configData['globals']['paths']['messaging_listener']
    messageListenerFullPath = f'{Config.projectPath}/{messageListenerPath}'
    createDir(path=messageListenerFullPath)

    for modelConfig in Config.configData['domain_models']:
        model = modelConfig['model']
        # region Create handlers in common/handler
        commonHandlerDirFullPath = f'{messageListenerFullPath}/common/handler'
        commonModelHandlerDirFullPath = f'{commonHandlerDirFullPath}/{model["path"]}'
        createDir(commonModelHandlerDirFullPath)
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
        createDir(projectModelHandlerDirFullPath)
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

def createDir(path: str):
    os.makedirs(path, exist_ok=True)
    Path(f'{path}/__init__.py').touch()


# region jinja filters
def funcParamsJinjaFilter(value):
    res = map(lambda x: f'{x["name"]}: {x["type"]} = {x["default"]}', value)
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

def _argKey(string: str, sign: str):
    return f'"{string}"' if sign == ':' else string


def funcToMapReturnDataJinjaFilter(value):
    res = map(lambda x: f"'{x['name']}': self.{x['name']}()", value)
    return ', '.join(list(res))


def funcMapCompareJinjaFilter(value):
    res = map(lambda x: f"self.{x['name']}() == other.{x['name']}()", value)
    return ' and '.join(list(res))
# endregion


initGlobalConfig()
fileLoader = FileSystemLoader(Config.templatePath)
jinjaEnv = Environment(loader=fileLoader)
jinjaEnv.filters['mapFuncParams'] = funcParamsJinjaFilter
jinjaEnv.filters['mapFuncArgs'] = funcArgsJinjaFilter
jinjaEnv.filters['mapFunToMapReturnData'] = funcToMapReturnDataJinjaFilter
jinjaEnv.filters['mapFunCompare'] = funcMapCompareJinjaFilter
jinjaEnv.filters['spacedWords'] = lambda x: Util.snakeCaseToLowerSpacedWordsString(string=x)
jinjaEnv.filters['upperCamelCase'] = lambda x: Util.snakeCaseToUpperCameCaseString(string=x)
jinjaEnv.filters['lowerCamelCase'] = lambda x: Util.snakeCaseToLowerCameCaseString(string=x)

if __name__ == '__main__':
    cli()
