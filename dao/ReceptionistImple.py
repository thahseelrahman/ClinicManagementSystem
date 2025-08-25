
from dao.ReceptionistAbstract import ReceptionistAbstract
from db.db_connection import DBConnection
from models.receptionist import Patient, Appointment

class ReceptionistImple(ReceptionistAbstract):
    'Implementation of ReceptionistAbstract methods'
    #queries
    DISPLAY_PATIENTS = "SELECT * FROM patient"
    DISPLAY_APPOINTMENTS = "SELECT * FROM appointment"
    INSERT_PATIENT = "INSERT INTO patient (first_name, last_name, dob, blood_group, gender, phone_no, address, email, reg_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    UPDATE_PATIENT = "UPDATE patient SET first_name = %s, last_name = %s, dob = %s, blood_group = %s, gender = %s, phone_no = %s, address = %s, email = %s, reg_date = %s WHERE patient_id = %s"
    DELETE_PATIENT = "DELETE FROM patient WHERE patient_id = %s"
    GET_PATIENT = "SELECT * FROM patient WHERE patient_id = %s"
    INSERT_APPOINTMENT = "INSERT INTO appointment (token_no, patient_id, doctor_id, appointment_date, appointment_time, status, symptoms, diagnosis) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    UPDATE_APPOINTMENT = "UPDATE appointment SET token_no = %s, patient_id = %s, doctor_id = %s, appointment_date = %s, appointment_time = %s, status = %s, symptoms = %s, diagnosis = %s WHERE app_id = %s"
    CANCEL_APPOINTMENT = "DELETE FROM appointment WHERE app_id = %s"
    GET_APPOINTMENT = "SELECT * FROM appointment WHERE app_id = %s"

    def __init__(self):
        self.conn = DBConnection().get_connection()

    def add_patient(self, patient):
        cursor = self.conn.cursor()
        cursor.execute(self.INSERT_PATIENT, (patient.get_first_name(), patient.get_last_name(), patient.get_dob(), patient.get_blood_group(), patient.get_gender(), patient.get_phone_no(), patient.get_address(), patient.get_email(), patient.get_reg_date()))
        self.conn.commit()
        cursor.close()

    def update_patient(self, patient):
        cursor = self.conn.cursor()
        cursor.execute(self.UPDATE_PATIENT, (patient.get_first_name(), patient.get_last_name(), patient.get_dob(), patient.get_blood_group(), patient.get_gender(), patient.get_phone_no(), patient.get_address(), patient.get_email(), patient.get_reg_date(), patient.get_patient_id()))
        self.conn.commit()
        cursor.close()

    def delete_patient(self, patient_id):
        cursor = self.conn.cursor()
        cursor.execute(self.DELETE_PATIENT, (patient_id,))
        self.conn.commit()
        cursor.close()

    def get_patient(self, patient_id):
        cursor = self.conn.cursor()
        cursor.execute(self.GET_PATIENT, (patient_id,))
        patient = cursor.fetchone()
        cursor.close()
        return patient
    
    def schedule_appointment(self, appointment):
        cursor = self.conn.cursor()
        cursor.execute(self.INSERT_APPOINTMENT, (appointment.get_token_no(), appointment.get_patient_id(), appointment.get_doctor_id(), appointment.get_appointment_date(), appointment.get_appointment_time(), appointment.get_status(), appointment.get_symptoms(), appointment.get_diagnosis()))
        self.conn.commit()
        cursor.close()

    def update_appointment(self, appointment):
        cursor = self.conn.cursor()
        cursor.execute(self.UPDATE_APPOINTMENT, (appointment.get_token_no(), appointment.get_patient_id(), appointment.get_doctor_id(), appointment.get_appointment_date(), appointment.get_appointment_time(), appointment.get_status(), appointment.get_symptoms(), appointment.get_diagnosis(), appointment.get_app_id()))
        self.conn.commit()
        cursor.close()

    def cancel_appointment(self, appointment_id):
        cursor = self.conn.cursor()
        cursor.execute(self.CANCEL_APPOINTMENT, (appointment_id,))
        self.conn.commit()
        cursor.close()

    def get_appointment(self, appointment_id):
        cursor = self.conn.cursor()
        cursor.execute(self.GET_APPOINTMENT, (appointment_id,))
        appointment = cursor.fetchone()
        cursor.close()
        return appointment
