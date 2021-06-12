"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


def readOnly(f):
    def wrapper(*args, **kwargs):
        from src.application.lifecycle.ApplicationServiceLifeCycle import ApplicationServiceLifeCycle

        ApplicationServiceLifeCycle.begin()

        try:
            return f(*args, **kwargs)
        finally:
            ApplicationServiceLifeCycle.close()

    return wrapper
