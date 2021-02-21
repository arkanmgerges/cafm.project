"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import csv
import os
import sys
import yaml
import jinja2
import traceback

import click

@click.group()
def cli():
    pass

@cli.command(help='Generate code files based on a config file')
@click.argument('config_file')
def generate(config_file):
    fileData = readConfig(config_file)
    print(fileData)

def readConfig(configFile):
    try:
        with open(f'{os.path.dirname(os.path.abspath(__file__))}/{configFile}', 'r') as file:
            return yaml.load(file, Loader=yaml.FullLoader)
    except:
        print(traceback.format_exc())
        print('Could not read config file')
        sys.exit(1)

if __name__ == '__main__':
    cli()
