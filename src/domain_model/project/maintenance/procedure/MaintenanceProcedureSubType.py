"""
@author: Mohammad S. moso<moso@develoop.run>
"""

from enum import Enum


class MaintenanceProcedureSubType(str, Enum):
    OUTSOURCED = "outsourced"
    IN_HOUSE = "in_house"
