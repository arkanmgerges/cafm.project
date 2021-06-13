"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


class DbUtil:
    @classmethod
    def disableForeignKeyChecks(cls, dbSession):
        dbSession.execute("SET FOREIGN_KEY_CHECKS=0")

    @classmethod
    def enableForeignKeyChecks(cls, dbSession):
        dbSession.execute("SET FOREIGN_KEY_CHECKS=1")
