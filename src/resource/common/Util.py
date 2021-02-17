"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


class Util:
    @staticmethod
    def snakeCaseToLowerCameCaseDict(dataDict: dict) -> dict:
        result = {}
        for key, val in dataDict.items():
            components = key.split('_')
            result[components[0] + ''.join(x.title() for x in components[1:])] = val
        return result

    @staticmethod
    def snakeCaseToLowerCameCaseString(string: str) -> str:
        components = string.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])