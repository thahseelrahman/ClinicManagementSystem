from abc import ABC, abstractmethod

class ReceptionistAbstract(ABC):

    @abstractmethod
    def add_patient(self, patient):
        pass

    @abstractmethod
    def update_patient(self, patient):
        pass

    # @abstractmethod
    # def delete_patient(self, patient_id):
    #     pass

    @abstractmethod
    def get_all_patients(self):
        pass

    @abstractmethod
    def get_patient(self, patient_id):
        pass

    @abstractmethod
    def schedule_appointment(self, appointment):
        pass

    @abstractmethod
    def get_all_appointments(self):
        pass

    @abstractmethod
    def update_appointment(self, appointment):
        pass

    # @abstractmethod
    # def cancel_appointment(self, appointment_id):
    #     pass

    @abstractmethod
    def get_appointment(self, appointment_id):
        pass
    
        # Bill management methods
    @abstractmethod
    def get_consultation_fee(self, doctor_id):
            pass
    
    @abstractmethod
    def insert_bill(self, bill_type, patient_id, ref_id, total_amount, status, bill_date):
            pass
