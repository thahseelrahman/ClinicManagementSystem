
from dao.ReceptionistAbstract import ReceptionistAbstract
from db.db_connection import DBConnection
from models.receptionist import Patient, Appointment

class ReceptionistImple(ReceptionistAbstract):
    'Implementation of ReceptionistAbstract methods'
    #queries
    DISPLAY_PATIENTS = "SELECT * FROM patients"
    DISPLAY_APPOINTMENTS = "SELECT * FROM appointments"
    INSERT_PATIENT = "INSERT INTO patients (first_name, last_name, dob, blood_group, gender, phone_no, address, email, reg_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    UPDATE_PATIENT = "UPDATE patients SET first_name = %s, last_name = %s, dob = %s, blood_group = %s, gender = %s, phone_no = %s, address = %s, email = %s, reg_date = %s WHERE patient_id = %s"
    DELETE_PATIENT = "DELETE FROM patients WHERE patient_id = %s"
    GET_PATIENT = "SELECT * FROM patients WHERE patient_id = %s"
    INSERT_APPOINTMENT = "INSERT INTO appointments (token_no, patient_id, doctor_id, appointment_date, appointment_time, status, symptoms, diagnosis) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    UPDATE_APPOINTMENT = "UPDATE appointments SET token_no = %s, patient_id = %s, doctor_id = %s, appointment_date = %s, appointment_time = %s, status = %s, symptoms = %s, diagnosis = %s WHERE app_id = %s"
    CANCEL_APPOINTMENT = "DELETE FROM appointments WHERE app_id = %s"
    GET_APPOINTMENT = "SELECT * FROM appointments WHERE app_id = %s"

    def __init__(self):
        self.conn = DBConnection().get_connection()

    def add_patient(self, patient):
        cursor = self.conn.cursor()
        cursor.execute(self.INSERT_PATIENT, (patient.first_name, patient.last_name, patient.dob, patient.blood_group, patient.gender, patient.phone_no, patient.address, patient.email, patient.reg_date))
        self.conn.commit()
        cursor.close()

    def update_patient(self, patient):
        cursor = self.conn.cursor()
        cursor.execute(self.UPDATE_PATIENT, (patient.first_name, patient.last_name, patient.dob, patient.blood_group, patient.gender, patient.phone_no, patient.address, patient.email, patient.reg_date, patient.patient_id))
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
        cursor.execute(self.INSERT_APPOINTMENT, (appointment.token_no, appointment.patient_id, appointment.doctor_id, appointment.appointment_date, appointment.appointment_time, appointment.status, appointment.symptoms, appointment.diagnosis))
        self.conn.commit()
        cursor.close()

    def update_appointment(self, appointment):
        cursor = self.conn.cursor()
        cursor.execute(self.UPDATE_APPOINTMENT, (appointment.token_no, appointment.patient_id, appointment.doctor_id, appointment.appointment_date, appointment.appointment_time, appointment.status, appointment.symptoms, appointment.diagnosis, appointment.app_id))
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
