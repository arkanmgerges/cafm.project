"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


class BaseListener:
    from src.resource.logging.decorator import debugLogger

    @debugLogger
    def _token(self, context) -> str:
        metadata = context.invocation_metadata()
        for key, value in metadata:
            if "token" == key:
                return value
        return ""