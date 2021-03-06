"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


from abc import ABC, abstractmethod
from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperation import DailyCheckProcedureOperation


class DailyCheckProcedureOperationRepository(ABC):
    @abstractmethod
    def save(self, obj: DailyCheckProcedureOperation):
        """Save daily check procedure operation

        Args:
            obj (DailyCheckProcedureOperation): The daily check procedure operation that needs to be saved

        """

    @abstractmethod
    def delete(self, obj: DailyCheckProcedureOperation):
        """Delete daily check procedure operation

        Args:
            obj (DailyCheckProcedureOperation): The daily check procedure operation that needs to be deleted

        """
