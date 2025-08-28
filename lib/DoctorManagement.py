from dao.DoctorImple import DoctorDaoImplementation
from dao.DoctorAbstract import DoctorDaoService
from models.doctor import Appointment
from datetime import date


class DoctorManagement:
    """Handles Doctor role operations like viewing and finding appointments."""

    dao_service: DoctorDaoService = DoctorDaoImplementation()

    @staticmethod
    def display_appointments():
        """Display all appointments for a specific doctor"""
        try:
            doc_id = int(input("Enter Doctor ID: "))
            appointments = DoctorManagement.dao_service.display_appointments(doc_id)

            if not appointments:
                print(f"No appointments found for Doctor ID {doc_id}")
                return

            print(f"\n--- Appointments for Doctor ID: {doc_id} ---")
            for app in appointments:
                app.display_patient_details()  # This will show age if model is updated
        except ValueError:
            print("❌ Invalid Doctor ID. Please enter a number.")

    @staticmethod
    def find_appointment_by_id():
        """Find and display a single appointment by Appointment ID"""
        try:
            app_id = int(input("Enter Appointment ID: "))
            appointment = DoctorManagement.dao_service.find_by_app_id(app_id)

            if appointment:
                print("\n--- Appointment Found ---")
                appointment.display_patient_details()  # This will show age if model is updated
            else:
                print("❌ Appointment not found")
        except ValueError:
            print("❌ Invalid Appointment ID. Please enter a number.")
            
    @staticmethod
    def update_appointment_notes():
        """Update notes, symptom, and diagnosis for a specific appointment"""
        try:
            app_id = int(input("Enter Appointment ID: "))

            # Get the appointment first to confirm it exists
            appointment = DoctorManagement.dao_service.find_by_app_id(app_id)
            if not appointment:
                print("❌ Appointment not found")
                return

            print(f"\n--- Updating Appointment ID: {app_id} ---")
            notes = input("Enter doctor's notes: ")
            symptom = input("Enter patient's symptoms: ")
            diagnosis = input("Enter diagnosis: ")

            success = DoctorManagement.dao_service.update_appointment_notes(
                app_id, notes, symptom, diagnosis
            )

            if success:
                print("✅ Appointment notes updated successfully")
            else:
                print("⚠️ Failed to update appointment notes")

        except ValueError:
            print("❌ Invalid Appointment ID. Please enter a number.")
            
    
    @staticmethod
    def fetch_medicines():
        """Display all available medicines"""
        medicines = DoctorManagement.dao_service.fetch_medicines()
        if not medicines:
            print("No medicines found.")
            return

        print("\n--- Available Medicines ---")
        for med in medicines:
            print(f"ID: {med['med_id']}, Name: {med['med_name']}, Description: {med['description']}, Price: {med['price']}, Stock: {med['stock']}")

    @staticmethod
    def create_prescription():
        """Create a prescription for an appointment"""
        try:
            pre_id = int(input("Enter Prescription ID: "))
            patient_id = int(input("Enter Patient ID: "))
            doc_id = int(input("Enter Doctor ID: "))
            med_id = int(input("Enter Medicine ID: "))
            dosage = input("Enter Dosage (e.g., 1 tablet): ")
            duration = input("Enter Duration (e.g., 5 days): ")
            pre_date = input("Enter Prescription Date (YYYY-MM-DD): ")
            # pre_date can't be in past
            if pre_date < str(date.today()):
                print("❌ Prescription date can't be in the past.")
                return

            success = DoctorManagement.dao_service.create_prescription(
                pre_id, patient_id, doc_id, med_id, dosage, duration, pre_date
            )

            if success:
                print("✅ Prescription created successfully")
            else:
                print("⚠️ Failed to create prescription")

        except ValueError:
            print("❌ Invalid input. Please enter valid numbers for IDs.")


