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
    @abstractmethod
    def check_username(self,username):
        pass
    @abstractmethod
    def check_password(self,password):
        pass
    @abstractmethod
    def update_staff(self)->bool:
        pass
    @abstractmethod
    def diable_staff(self)->bool:
        pass
    @abstractmethod
    def staff_specialization(self)->bool:
        pass
    @abstractmethod
    def staff_specialization(self)->bool:
        pass
    @abstractmethod
    def search_by_id(self,staff_id):
        pass
    @abstractmethod
    def check_doc_id(self, username):
        pass



