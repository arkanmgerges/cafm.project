"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


def transactional(f):
    from sqlalchemy.exc import IntegrityError

    def wrapper(*args, **kwargs):
        from src.application.lifecycle.ApplicationServiceLifeCycle import ApplicationServiceLifeCycle
        ApplicationServiceLifeCycle.begin()

        try:
            result = f(*args, **kwargs)
            ApplicationServiceLifeCycle.success()
            return result
        except IntegrityError as e:
            from src.resource.logging.logger import logger
            logger.debug(e)
            from src.port_adapter.repository.resource.exception.IntegrityErrorRepositoryException import \
                IntegrityErrorRepositoryException
            from src.domain_model.common.HasToMap import HasToMap
            objects = []
            hasToMapObjects = []
            for value in kwargs.values():
                if isinstance(value, HasToMap):
                    hasToMapObjects.append(value)
                elif isinstance(value, list) and len(value) > 0 and isinstance(value[0], HasToMap):
                    hasToMapObjects = hasToMapObjects + value
                elif isinstance(value, list) and len(value) > 0:
                    objects = objects + value
            if len(hasToMapObjects) == 0:
                if len(objects) > 0:
                    raise IntegrityErrorRepositoryException(
                        f'Not allowed action, integrity error exception, data : {objects}')
                else:
                    raise IntegrityErrorRepositoryException(
                        f'Not allowed action, integrity error exception')
            else:
                raise IntegrityErrorRepositoryException(f'Not allowed action, integrity error exception, data : {[x.toMap() for x in hasToMapObjects]}')
        finally:
            ApplicationServiceLifeCycle.close()

    return wrapper
