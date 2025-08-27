
from dao.ReceptionistAbstract import ReceptionistAbstract
from db.db_connection import DBConnection
from models.receptionist import Patient, Appointment

class ReceptionistImple(ReceptionistAbstract):
    'Implementation of ReceptionistAbstract methods'
    #queries
    DISPLAY_PATIENTS = "SELECT * FROM patient"
    DISPLAY_APPOINTMENTS = "SELECT * FROM appoinment"
    INSERT_PATIENT = "INSERT INTO patient (first_name, last_name, dob, blood_group, gender, phone_no, address, email, reg_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    UPDATE_PATIENT = "UPDATE patient SET first_name = %s, last_name = %s, dob = %s, blood_group = %s, gender = %s, phone_no = %s, address = %s, email = %s, reg_date = %s WHERE patient_id = %s"
    DELETE_PATIENT = "DELETE FROM patient WHERE patient_id = %s"
    GET_PATIENT = "SELECT * FROM patient WHERE patient_id = %s"
    INSERT_APPOINTMENT = "INSERT INTO appoinment (token_no, doc_id, patient_id, app_date, app_time, status, symptoms, diagnosis) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    UPDATE_APPOINTMENT = "UPDATE appoinment SET token_no = %s, doc_id = %s, patient_id = %s, app_date = %s, app_time = %s, status = %s, symptoms = %s, diagnosis = %s WHERE app_id = %s"
    CANCEL_APPOINTMENT = "DELETE FROM appoinment WHERE app_id = %s"
    GET_APPOINTMENT = "SELECT * FROM appoinment WHERE app_id = %s"

    def __init__(self):
        self.conn = DBConnection().get_connection()

    def add_patient(self, patient: Patient):
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.INSERT_PATIENT, (patient.get_first_name(), patient.get_last_name(), patient.get_dob(), patient.get_blood_group(), patient.get_gender(), patient.get_phone_no(), patient.get_address(), patient.get_email(), patient.get_reg_date()))
            self.conn.commit()
            return cursor.rowcount == 1
        except Exception as e:
            print(f"Error adding patient: {e}")
            return None
        finally:
            cursor.close()

    # def update_patient(self, patient:Patient,patient_id:int)->bool:
    #     try:
    #         cursor = self.conn.cursor(dictionary=True)
    #         cursor.execute(self.UPDATE_PATIENT, (patient.get_first_name(), patient.get_last_name(), patient.get_dob(), patient.get_blood_group(), patient.get_gender(), patient.get_phone_no(), patient.get_address(), patient.get_email(), patient.get_reg_date(), patient_id))
    #         self.conn.commit()
    #         return cursor.rowcount == 1
    #     except Exception as e:
    #         print(f"Error updating patient: {e}")
    #         return None
    #     finally:
    #         cursor.close()

    # def delete_patient(self, patient_id):
    #     cursor = self.conn.cursor()
    #     cursor.execute(self.DELETE_PATIENT, (patient_id,))
    #     self.conn.commit()
    #     cursor.close()

    # def get_patient(self, patient_id):
    #     cursor = self.conn.cursor()
    #     cursor.execute(self.GET_PATIENT, (patient_id,))
    #     patient = cursor.fetchone()
    #     cursor.close()
    #     return patient

    def get_all_patients(self)->list[Patient]:
        try:
            patients = []
            cursor = self.conn.cursor(dictionary = True)
            cursor.execute(self.DISPLAY_PATIENTS)
            rows = cursor.fetchall()
            for row in rows:
                patients.append(Patient(
                    patient_id=row['patient_id'],
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    dob=row['dob'],
                    blood_group=row['blood_group'],
                    gender=row['gender'],
                    phone_no=row['phone_no'],
                    address=row['address'],
                    email=row['email'],
                    reg_date=row['reg_date']
                ))
            return patients    
        except Exception as e:
            print(f"Error fetching all patients: {e}")
        finally:
            cursor.close()

    def schedule_appointment(self, appointment:Appointment):
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.INSERT_APPOINTMENT, (appointment.get_token_no(), appointment.get_patient_id(), appointment.get_doctor_id(), appointment.get_appointment_date(), appointment.get_appointment_time(), appointment.get_status(), appointment.get_symptoms(), appointment.get_diagnosis()))
            self.conn.commit()
            return cursor.rowcount == 1
        except Exception as e:
            print(f"Error scheduling appointment: {e}")
            return None
        finally:
            cursor.close()

    def get_all_appointments(self):
        try:
            appointments = []
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(self.DISPLAY_APPOINTMENTS)
            rows = cursor.fetchall()
            for row in rows:
                appointments.append(Appointment(
                    app_id=row['app_id'],
                    token_no=row['token_no'],
                    patient_id=row['patient_id'],
                    doctor_id=row['doc_id'],
                    appointment_date=row['app_date'],
                    appointment_time=row['app_time'],
                    status=row['status'],
                    symptoms=row['symptoms'],
                    diagnosis=row['diagnosis']
                ))
            return appointments
        except Exception as e:
            print(f"Error fetching all appointments: {e}")
            return None
        finally:
            cursor.close()

    # def update_appointment(self, appointment):
    #     cursor = self.conn.cursor()
    #     cursor.execute(self.UPDATE_APPOINTMENT, (appointment.get_token_no(), appointment.get_patient_id(), appointment.get_doctor_id(), appointment.get_appointment_date(), appointment.get_appointment_time(), appointment.get_status(), appointment.get_symptoms(), appointment.get_diagnosis(), appointment.get_app_id()))
    #     self.conn.commit()
    #     cursor.close()

    # def cancel_appointment(self, appointment_id):
    #     cursor = self.conn.cursor()
    #     cursor.execute(self.CANCEL_APPOINTMENT, (appointment_id,))
    #     self.conn.commit()
    #     cursor.close()

    # def get_appointment(self, appointment_id):
    #     cursor = self.conn.cursor()
    #     cursor.execute(self.GET_APPOINTMENT, (appointment_id,))
    #     appointment = cursor.fetchone()
    #     cursor.close()
    #     return appointment
