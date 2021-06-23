"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import glob
import re
from shutil import copyfile
import click

pattern = re.compile(r"([0-9]+)__")


@click.group()
def cli():
    pass



@cli.command(help="Rename files with new counter starting at 1 and zero filled based on the current files")
@click.argument("files_path")
def generate(files_path):
    filesPathWithRegex = f"{files_path}/[0-9]*.py"
    files = glob.glob(filesPathWithRegex, recursive=True, )
    counter = 1
    for filename in files:
        number = _extractNumber(filename)
        numberLength = len(number)
        newNumber = str(counter).zfill(numberLength)
        counter += 1
        newFileName = filename.replace(number, newNumber)
        copyfile(filename, newFileName)
        print(newFileName)

def _extractNumber(name):
    return pattern.search(name).group(1)
