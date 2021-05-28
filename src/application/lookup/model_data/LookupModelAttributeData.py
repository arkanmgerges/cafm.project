"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

class LookupModelAttributeData:
    __slots__ = ["dataType", "isClass", "isArray"]

    def __init__(self, *_args, **kwargs):
        self.dataType = kwargs['dataType'] if 'dataType' in kwargs else str
        self.isClass = kwargs['isClass'] if 'isClass' in kwargs else False
        self.isArray = kwargs['isArray'] if 'isArray' in kwargs else False

    def __repr__(self):
        return f'{{"data_type": {self.dataType}, "is_class": {self.isClass}, "is_array": {self.isArray}}}'