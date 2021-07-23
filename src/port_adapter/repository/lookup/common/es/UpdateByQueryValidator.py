"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

class UpdateByQueryValidator:
    @classmethod
    def validate(cls, response):
        resDict = response.to_dict()
        if resDict["updated"] == 0:
            raise Exception(f"{resDict}")