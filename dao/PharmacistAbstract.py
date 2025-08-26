from abc import ABC, abstractmethod
from typing import List
from models.pharmacist import Pharmacist
class PharmacistDaoService(ABC):
    @abstractmethod
    def display_all_medicines(self) -> List[Pharmacist]:
        pass

    @abstractmethod
    def add_medicine(self, medicine: Pharmacist) -> bool:
        pass
