from abc import ABC, abstractmethod
from typing import List
from models.pharmacist import Pharmacist
from models.pharmacist import Bill
class PharmacistDaoService(ABC):
    @abstractmethod
    def display_all_medicines(self) -> List[Pharmacist]:
        pass

    @abstractmethod
    def add_medicine(self, medicine: Pharmacist) -> bool:
        pass

    @abstractmethod
    def update_medicine(self, medicine: Pharmacist, med_id: int) -> bool:
        pass

    @abstractmethod
    def delete_medicine(self, med_id: int) -> bool:
        pass

    @abstractmethod
    def add_bill(self, bill: Bill) -> bool: 
        pass

    @abstractmethod
    def search_bill(self, bill_id: int) -> Bill:
        pass

    @abstractmethod
    def update_Bill(self, bill: Bill, bill_id: int) -> bool:
        pass

    @abstractmethod
    def delete_Bill(self, bill_id: int) -> bool:
        pass

    @abstractmethod
    def list_bills(self) -> List[Bill]:
        pass

    @abstractmethod
    def pay_Bill(self, bill_id: int) -> bool:
        pass
