"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import re


class Util:
    pattern = re.compile(r"(?<!^)(?=[A-Z])")

    @staticmethod
    def camelCaseToLowerSnakeCase(camelCaseString: str) -> str:
        return Util.pattern.sub("_", camelCaseString).lower()

    @staticmethod
    def snakeCaseToLowerCameCaseDict(dataDict: dict) -> dict:
        result = {}
        for key, val in dataDict.items():
            components = key.split("_")
            result[components[0] + "".join(x.title() for x in components[1:])] = val
        return result

    @staticmethod
    def snakeCaseToLowerCameCaseString(string: str) -> str:
        components = string.split("_")
        return components[0] + "".join(x.title() for x in components[1:])

    @staticmethod
    def snakeCaseToUpperCameCaseString(string: str) -> str:
        components = string.split("_")
        return "".join(x.title() for x in components)

    @staticmethod
    def snakeCaseToLowerSpacedWordsString(string: str) -> str:
        components = string.split("_")
        return " ".join(x.lower() for x in components)
