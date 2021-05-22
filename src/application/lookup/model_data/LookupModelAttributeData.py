"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

class LookupModelAttributeData:
    __slots__ = ["dataType", "isLookupClass"]
    def __init__(self, *args, **kwargs):
        self.dataType = kwargs['dataType'] if 'dataType' in kwargs else str
        self.isLookupClass = kwargs['isLookupClass'] if 'isLookupClass' in kwargs else False