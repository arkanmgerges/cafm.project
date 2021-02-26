"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import datetime

import datetime as datetime


class DateTimeHelper:
    @staticmethod
    def utcNow() -> int:
        """Return current utc time in milliseconds

        Returns:
             int: Current UTC time in milliseconds
        """
        epoch = datetime.datetime(1970, 1, 1, 0, 0, 0)
        now = datetime.datetime.utcnow()
        return round((now - epoch).total_seconds() * 1000)

    @staticmethod
    def datetimeToInt(datetimeObject: datetime.datetime) -> int:
        """Return int from a datetime

        Returns:
            int: Current time as integer
        """
        if datetimeObject is not None:
            return round(datetimeObject.timestamp())
        return None

    @staticmethod
    def intOneYearAfterEpochTimeInSeconds() -> int:
        """Return epoch time in seconds

        Returns:
            int: Epoch time as integer
        """
        epoch = datetime.datetime(1970, 1, 1, 0, 0, 0)
        epochPlusOneYear = datetime.datetime(1971, 1, 1, 0, 0, 0)
        return round((epochPlusOneYear - epoch).total_seconds())
