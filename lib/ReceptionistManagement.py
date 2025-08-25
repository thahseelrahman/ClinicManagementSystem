from dao.ReceptionistImple import ReceptionistImple
from dao.ReceptionistAbstract import ReceptionistAbstract
from models.receptionist import Patient, Appointment
from datetime import date,time,datetime

class ReceptionmanagementLib:
    'handle crud logic for receptionist'
    dao_service: ReceptionistAbstract = ReceptionistImple()

    @staticmethod
    def add_patient():
        patient = Patient()
        first_name = input("Enter First Name: ")
        patient.set_first_name(first_name)
        last_name = input("Enter Last Name: ")
        patient.set_last_name(last_name)
        dob = input("Enter Date of Birth (YYYY-MM-DD): ")
        patient.set_dob(datetime.strptime(dob, "%Y-%m-%d").date())
        patient.set_blood_group(input("Enter Blood Group: "))
        patient.set_gender(input("Enter Gender: "))
        patient.set_phone_no(input("Enter Phone Number: "))
        patient.set_address(input("Enter Address: "))
        patient.set_email(input("Enter Email: "))
        patient.set_reg_date(date.today())
        if ReceptionmanagementLib.dao_service.add_patient(patient):
            print("Patient added successfully.")
        else:
            print("Failed to add patient.")

    @staticmethod
    def update_patient():
        searchid = int(input("Enter Patient Id: "))
        #create a method in DAO
        patient = ReceptionmanagementLib.dao_service.get_patient(searchid)
        if not patient:
            print("Patient not found.")
            return
        print(patient)
        confirm = input("Do you want to update this patient? (y/n): ")
        if confirm.lower() == 'y':
            patient.set_first_name(input("Enter new First Name: "))
            patient.set_last_name(input("Enter new Last Name: "))
            dob = input("Enter new Date of Birth (YYYY-MM-DD): ")
            patient.set_dob(datetime.strptime(dob, "%Y-%m-%d").date())
            patient.set_blood_group(input("Enter new Blood Group: "))
            patient.set_gender(input("Enter new Gender: "))
            patient.set_phone_no(input("Enter new Phone Number: "))
            patient.set_address(input("Enter new Address: "))
            patient.set_email(input("Enter new Email: "))
            if ReceptionmanagementLib.dao_service.update_patient(patient):
                print("Patient updated successfully.")
            else:
                print("Failed to update patient.")

    @staticmethod
    def delete_patient():
        searchid = int(input("Enter Patient Id: "))
        patient = ReceptionmanagementLib.dao_service.get_patient(searchid)
        if not patient:
            print("Patient not found.")
            return
        print(patient)
        confirm = input("Do you want to delete this patient? (y/n): ")
        if confirm.lower() != 'y':
            return
        if ReceptionmanagementLib.dao_service.delete_patient(patient):
            print("Patient deleted successfully.")
        else:
            print("Failed to delete patient.")

    @staticmethod
    def get_patient():
        searchid = int(input("Enter Patient Id: "))
        patient = ReceptionmanagementLib.dao_service.get_patient(searchid)
        if not patient:
            print("Patient not found.")
            return
        print(patient)

    @staticmethod
    def schedule_appoinment():
        appointment = Appointment()
        appointment.set_token_no(int(input("Enter Token Number: ")))
        appointment.set_patient_id(int(input("Enter Patient Id: ")))
        appointment.set_doctor_id(int(input("Enter Doctor Id: ")))
        appointment_date = input("Enter Appointment Date (YYYY-MM-DD): ")
        appointment.set_appointment_date(datetime.strptime(appointment_date, "%Y-%m-%d").date())
        appointment_time = input("Enter Appointment Time (HH:MM:SS): ")
        appointment.set_appointment_time(datetime.strptime(appointment_time, "%H:%M:%S").time())
        appointment.set_status(input("Enter Status (Scheduled/Completed/Canceled): "))
        appointment.set_symptoms(input("Enter Symptoms: "))
        appointment.set_diagnosis(input("Enter Diagnosis: "))
        if ReceptionmanagementLib.dao_service.schedule_appointment(appointment):
            print("Appointment scheduled successfully.")
        else:
            print("Failed to schedule appointment.")

    @staticmethod
    def update_appointment():
        token_no = int(input("Enter Token Number: "))
        appointment = ReceptionmanagementLib.dao_service.get_appointment(token_no)
        if not appointment:
            print("Appointment not found.")
            return
        print(appointment)
        confirm = input("Do you want to update this appointment? (y/n): ")
        if confirm.lower() == 'y':
            appointment.set_patient_id(int(input("Enter new Patient Id: ")))
            appointment.set_doctor_id(int(input("Enter new Doctor Id: ")))
            appointment_date = input("Enter new Appointment Date (YYYY-MM-DD): ")
            appointment.set_appointment_date(datetime.strptime(appointment_date, "%Y-%m-%d").date())
            appointment_time = input("Enter new Appointment Time (HH:MM:SS): ")
            appointment.set_appointment_time(datetime.strptime(appointment_time, "%H:%M:%S").time())
            appointment.set_status(input("Enter new Status (Scheduled/Completed/Canceled): "))
            appointment.set_symptoms(input("Enter new Symptoms: "))
            appointment.set_diagnosis(input("Enter new Diagnosis: "))
            if ReceptionmanagementLib.dao_service.update_appointment(appointment):
                print("Appointment updated successfully.")
            else:
                print("Failed to update appointment.")

    @staticmethod
    def cancel_appointment():
        token_no = int(input("Enter Token Number: "))
        appointment = ReceptionmanagementLib.dao_service.get_appointment(token_no)
        if not appointment:
            print("Appointment not found.")
            return
        print(appointment)
        confirm = input("Do you want to delete this appointment? (y/n): ")
        if confirm.lower() != 'y':
            return
        if ReceptionmanagementLib.dao_service.delete_appointment(appointment):
            print("Appointment deleted successfully.")
        else:
            print("Failed to delete appointment.")

    @staticmethod
    def get_appointment():
        token_no = int(input("Enter Token Number: "))
        appointment = ReceptionmanagementLib.dao_service.get_appointment(token_no)
        if not appointment:
            print("Appointment not found.")
            return
        print(appointment)
