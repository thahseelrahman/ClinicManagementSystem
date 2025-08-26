from abc import ABC,abstractmethod
from typing import List
from models.admin import Staff
class AdminAbstarct(ABC):
    @abstractmethod
    def display_staff(self)->List[Staff]:
        pass
    @abstractmethod
    def add_staff(self)->bool:
        pass
    def add_credential(self)->bool:
        pass
    @abstractmethod
    def display_staff_id(self):
        pass

