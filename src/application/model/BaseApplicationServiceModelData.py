"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import Callable, Tuple

class BaseApplicationServiceModelData:
    def __init__(self,
                 getterFunction: Callable = None,
                 function: Callable = None,
                 args: Tuple = None,
                 kwargs: dict = None,
                 ):
        self.getterFunction: Callable = getterFunction
        self.function: Callable = function
        self.args: Tuple = args if args is not None else tuple()
        self.kwargs: dict = kwargs if kwargs is not None else {}

