"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from enum import Enum


class OrganizationType(Enum):
    PROVIDER = "provider"
    BENEFICIARY = "beneficiary"
    TENANT = "tenant"
