"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


class UpdateByQueryValidator:
    @classmethod
    def validate(cls, response):
        resDict = response.to_dict()
        if 'updated' not in resDict:
            from src.resource.logging.logger import logger
            logger.error(f'Elastic error for update by query with result dict: {resDict}')
            raise Exception(f"{resDict}")
        if resDict["updated"] == 0:
            if 'failures' in resDict and resDict['failures'] == []:
                return
            raise Exception(f"{resDict}")