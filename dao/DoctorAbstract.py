from abc import ABC, abstractmethod
from typing import List, Optional
from models.doctor import Appointment


class DoctorDaoService(ABC):
    """Abstract class defining DAO operations for Doctor role."""

    @abstractmethod
    def display_appointments(self, doc_id: int) -> List[Appointment]:
        """Fetch appointments for a specific doctor"""
        pass

    @abstractmethod
    def find_by_app_id(self, app_id: int) -> Optional[Appointment]:
        """Find appointment by appointment ID"""
        pass

    @abstractmethod
    def update_appointment_notes(self, app_id: int, notes: str, symptoms: str, diagnosis: str) -> bool:
        """Update notes, symptoms, and diagnosis for an appointment"""
        pass
    
    @abstractmethod
    def fetch_medicines(self) -> List[dict]:
        """Fetch all medicines from the medicine table"""
        pass

    @abstractmethod
    def create_prescription(self, app_id: int, medicine_id: int, dosage: str, duration: str, pre_date: str) -> bool:
        """Insert a prescription record into med_prescription"""
        pass