# Example for doctor module: display all appointments for a doctor
@staticmethod
def display_appointments_for_doctor():  # This line is now removed
    try:
        from db.db_connection import DBConnection
        conn = DBConnection().get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT doc_id FROM doctor")
        doctors = cursor.fetchall()
        cursor.close()
        if not doctors:
            print("No doctors found.")
            return
        print("Available Doctors:")
        for d in doctors:
            print(f"ID: {d['doc_id']}")
        doctor_id = int(input("Enter Doctor Id: "))
        # ...existing code to display appointments for doctor_id...
    except Exception as e:
        print(f"Error displaying doctors: {e}")
from dao.ReceptionistImple import ReceptionistImple
from dao.ReceptionistAbstract import ReceptionistAbstract
from models.receptionist import Patient, Appointment
from datetime import date,time,datetime

class ReceptionmanagementLib:
    @staticmethod
    def create_bill():
        try:
            patient_id = int(input("Enter Patient Id: "))
            doctor_id = int(input("Enter Doctor Id: "))
            bill_type = input("Enter Bill Type: ")
            status = input("Enter Bill Status: ")
            # Validate bill_date
            while True:
                bill_date_str = input("Enter Bill Date (YYYY-MM-DD) or leave blank for today: ")
                if not bill_date_str:
                    bill_date = date.today()
                    break
                try:
                    bill_date = datetime.strptime(bill_date_str, "%Y-%m-%d").date()
                    break
                except Exception as e:
                    print(f"Bill Date Error: {e}")
                    print("Please enter the date in YYYY-MM-DD format.")
            # Fetch consultation fee from doctor table
            consultation_fee = ReceptionmanagementLib.dao_service.get_consultation_fee(doctor_id)
            if consultation_fee is None:
                print("Doctor not found or no consultation fee set by Admin.")
                return
            total_amount = consultation_fee + 150
            # Insert bill into bill table
            success = ReceptionmanagementLib.dao_service.insert_bill(
                bill_type,
                patient_id,
                doctor_id,
                total_amount,
                status,
                bill_date
            )
            if success:
                print(f"Bill created successfully. Total Amount: {total_amount}")
            else:
                print("Failed to create bill.")
        except Exception as e:
            print(f"Error creating bill: {e}")
    'handle crud logic for receptionist'
    dao_service: ReceptionistAbstract = ReceptionistImple()

    @staticmethod
    def add_patient():
        patient = Patient()
        errors = []
        # Validate first name
        first_name = input("Enter First Name: ")
        try:
            patient.set_first_name(first_name)
        except Exception as e:
            errors.append(f"First Name: {e}")
        # Validate last name
        last_name = input("Enter Last Name: ")
        try:
            patient.set_last_name(last_name)
        except Exception as e:
            errors.append(f"Last Name: {e}")
        # Validate date of birth
        while True:
            dob = input("Enter Date of Birth (YYYY-MM-DD): ")
            try:
                dob_date = datetime.strptime(dob, "%Y-%m-%d").date()
                patient.set_dob(dob_date)
                break
            except Exception as e:
                print(f"Date of Birth Error: {e}")
                print("Please enter the date in YYYY-MM-DD format.")
        # Validate blood group
        blood_group = input("Enter Blood Group: ")
        try:
            patient.set_blood_group(blood_group)
        except Exception as e:
            errors.append(f"Blood Group: {e}")
        # Validate gender
        gender = input("Enter Gender: ")
        try:
            patient.set_gender(gender)
        except Exception as e:
            errors.append(f"Gender: {e}")
        # Validate phone number
        phone_no = input("Enter Phone Number: ")
        try:
            patient.set_phone_no(phone_no)
        except Exception as e:
            errors.append(f"Phone Number: {e}")
        # Validate address
        address = input("Enter Address: ")
        try:
            patient.set_address(address)
        except Exception as e:
            errors.append(f"Address: {e}")
        # Validate email
        email = input("Enter Email: ")
        try:
            patient.set_email(email)
        except Exception as e:
            errors.append(f"Email: {e}")
        # Validate registration date
        reg_date = date.today()
        try:
            patient.set_reg_date(reg_date)
        except Exception as e:
            errors.append(f"Registration Date: {e}")
        if errors:
            print("Error(s) adding patient:")
            for err in errors:
                print(err)
            print("Patient not added due to validation errors.")
        else:
            if ReceptionmanagementLib.dao_service.add_patient(patient):
                print("Patient added successfully.")
            else:
                print("Failed to add patient.")

    @staticmethod
    def update_patient():
        # List available patient IDs and names
        patients = ReceptionmanagementLib.dao_service.get_all_patients()
        if not patients:
            print("No patients found.")
            return
        print("Available Patients:")
        for p in patients:
            print(f"ID: {p.get_patient_id()} | Name: {p.get_first_name()} {p.get_last_name()}")
        searchid = int(input("Enter Patient Id: "))
        patient = ReceptionmanagementLib.dao_service.get_patient(searchid)
        if not patient:
            print("Patient not found.")
            return
        print(patient)
        confirm = input("Do you want to update this patient? (y/n): ")
        if confirm.lower() == 'y':
            errors = []
            phone_no = input("Enter new Phone Number: ")
            try:
                patient.set_phone_no(phone_no)
            except Exception as e:
                errors.append(f"Phone Number: {e}")
            email = input("Enter new Email: ")
            try:
                patient.set_email(email)
            except Exception as e:
                errors.append(f"Email: {e}")
            # Enable repeated prompt for DOB update
            while True:
                dob = input("Enter new Date of Birth (YYYY-MM-DD) or leave blank to skip: ")
                if not dob:
                    break
                try:
                    dob_date = datetime.strptime(dob, "%Y-%m-%d").date()
                    patient.set_dob(dob_date)
                    break
                except Exception as e:
                    print(f"Date of Birth Error: {e}")
                    print("Please enter the date in YYYY-MM-DD format.")
            if errors:
                print("Error(s) updating patient:")
                for err in errors:
                    print(err)
                print("Patient not updated due to validation errors.")
            else:
                if ReceptionmanagementLib.dao_service.update_patient(patient, searchid):
                    print("Patient updated successfully.")
                else:
                    print("Failed to update patient.")

    # @staticmethod
    # def delete_patient():
    #     searchid = int(input("Enter Patient Id: "))
    #     patient = ReceptionmanagementLib.dao_service.get_patient(searchid)
    #     if not patient:
    #         print("Patient not found.")
    #         return
    #     print(patient)
    #     confirm = input("Do you want to delete this patient? (y/n): ")
    #     if confirm.lower() != 'y':
    #         return
    #     if ReceptionmanagementLib.dao_service.delete_patient(patient):
    #         print("Patient deleted successfully.")
    #     else:
    #         print("Failed to delete patient.")

    @staticmethod
    def get_patient():
        searchid = int(input("Enter Patient Id: "))
        patient = ReceptionmanagementLib.dao_service.get_patient(searchid)
        if not patient:
            print("Patient not found.")
            return
        print(patient)

    @staticmethod
    def get_all_patients():
        patients = ReceptionmanagementLib.dao_service.get_all_patients()
        if not patients:
            print("No patients found.")
            return
        for patient in patients:
            print(patient)

    @staticmethod
    def schedule_appoinment():
        try:
            appointment = Appointment()
            token_no = int(input("Enter Token Number: "))
            appointment.set_token_no(token_no)
            # List available patient IDs and names
            patients = ReceptionmanagementLib.dao_service.get_all_patients()
            if not patients:
                print("No patients found. Cannot schedule appointment.")
                return
            print("Available Patients:")
            for p in patients:
                print(f"ID: {p.get_patient_id()} | Name: {p.get_first_name()} {p.get_last_name()}")
            patient_id = int(input("Enter Patient Id: "))
            appointment.set_patient_id(patient_id)
            # List available doctor IDs and names
            try:
                from db.db_connection import DBConnection
                conn = DBConnection().get_connection()
                cursor = conn.cursor(dictionary=True)
                cursor.execute("SELECT doc_id FROM doctor")
                doctors = cursor.fetchall()
                cursor.close()
                if not doctors:
                    print("No doctors found. Cannot schedule appointment.")
                    return
                print("Available Doctors:")
                for d in doctors:
                    print(f"ID: {d['doc_id']} ")
            except Exception as e:
                print(f"Error fetching doctors: {e}")
                return
            doctor_id = int(input("Enter Doctor Id: "))
            appointment.set_doctor_id(doctor_id)
            appointment_date = input("Enter Appointment Date (YYYY-MM-DD): ")
            try:
                app_date = datetime.strptime(appointment_date, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("Invalid date format for Appointment Date. Please use YYYY-MM-DD.")
            appointment.set_appointment_date(app_date)
            appointment_time = input("Enter Appointment Time (HH:MM:SS): ")
            try:
                app_time = datetime.strptime(appointment_time, "%H:%M:%S").time()
            except ValueError:
                raise ValueError("Invalid time format for Appointment Time. Please use HH:MM:SS.")
            appointment.set_appointment_time(app_time)
            appointment.set_status(input("Enter Status (Scheduled/Completed/Canceled): "))
            if ReceptionmanagementLib.dao_service.schedule_appointment(appointment):
                print("Appointment scheduled successfully.")
            else:
                print("Failed to schedule appointment.")
        except Exception as e:
            print(f"Error scheduling appointment: {e}")

    @staticmethod
    def get_all_appointments():
        appointments = ReceptionmanagementLib.dao_service.get_all_appointments()
        if not appointments:
            print("No appointments found.")
            return
        for appointment in appointments:
            print(appointment)

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
            try:
                appointment.set_patient_id(int(input("Enter new Patient Id: ")))
                appointment.set_doctor_id(int(input("Enter new Doctor Id: ")))
                # Repeated prompt for appointment date
                while True:
                    appointment_date = input("Enter new Appointment Date (YYYY-MM-DD): ")
                    try:
                        app_date = datetime.strptime(appointment_date, "%Y-%m-%d").date()
                        appointment.set_appointment_date(app_date)
                        break
                    except Exception as e:
                        print(f"Appointment Date Error: {e}")
                        print("Please enter the date in YYYY-MM-DD format.")
                appointment_time = input("Enter new Appointment Time (HH:MM:SS): ")
                try:
                    app_time = datetime.strptime(appointment_time, "%H:%M:%S").time()
                except ValueError:
                    raise ValueError("Invalid time format for Appointment Time. Please use HH:MM:SS.")
                appointment.set_appointment_time(app_time)
                appointment.set_status(input("Enter new Status (Scheduled/Completed/Canceled): "))
                appointment.set_symptoms(input("Enter new Symptoms: "))
                appointment.set_diagnosis(input("Enter new Diagnosis: "))
                if ReceptionmanagementLib.dao_service.update_appointment(appointment):
                    print("Appointment updated successfully.")
                else:
                    print("Failed to update appointment.")
            except Exception as e:
                print(f"Error updating appointment: {e}")

    # @staticmethod
    # def cancel_appointment():
    #     token_no = int(input("Enter Token Number: "))
    #     appointment = ReceptionmanagementLib.dao_service.get_appointment(token_no)
    #     if not appointment:
    #         print("Appointment not found.")
    #         return
    #     print(appointment)
    #     confirm = input("Do you want to delete this appointment? (y/n): ")
    #     if confirm.lower() != 'y':
    #         return
    #     if ReceptionmanagementLib.dao_service.delete_appointment(appointment):
    #         print("Appointment deleted successfully.")
    #     else:
    #         print("Failed to delete appointment.")

    @staticmethod
    def get_appointment():
        token_no = int(input("Enter Token Number: "))
        appointment = ReceptionmanagementLib.dao_service.get_appointment(token_no)
        if not appointment:
            print("Appointment not found.")
            return
        print(appointment)
