from typing import List, Dict, Optional
from dao.DoctorAbstract import DoctorDaoService
from db.db_connection import DBConnection
from models.doctor import Appointment


class DoctorDaoImplementation(DoctorDaoService):
    """DAO Implementation for Doctor role operations."""

    # SQL Queries
    #get app_id,first_name,last_name, age,gender by joining patient tabel and appointment table
    
    DISPLAY_APPOINTMENTS = """
        SELECT a.app_id, a.app_date, a.app_time, a.status,
               p.patient_id, p.first_name, p.last_name, p.dob, p.gender
        FROM appoinment a
        JOIN patient p ON a.patient_id = p.patient_id
        WHERE a.doc_id = %s
    """

    FIND_BY_APP_ID = """
        SELECT a.app_id, a.app_date, a.app_time, a.status,
               p.patient_id, p.first_name, p.last_name, p.dob, p.gender
        FROM appoinment a
        JOIN patient p ON a.patient_id = p.patient_id
        WHERE a.app_id = %s
    """
    UPDATE_APPOINTMENT_NOTES = """
        UPDATE appoinment
        SET notes = %s,
            symptoms = %s,
            diagnosis = %s
        WHERE app_id = %s
    """
    
    FETCH_MEDICINES = """
        SELECT med_id, med_name, description, price, stock
        FROM medicine
    """

    CREATE_PRESCRIPTION = """
        INSERT INTO med_prescription (pre_id,patient_id,doc_id,med_id,dosage,duration,pre_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    
    
    
    def update_appointment_notes(self, app_id: int, notes: str, symptoms: str, diagnosis: str) -> bool:
        """Update notes, symptoms, and diagnosis for an appointment"""
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.UPDATE_APPOINTMENT_NOTES, (notes, symptoms, diagnosis, app_id))
            self.conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print("❌ Error updating appointment notes:", e)
            return False
        finally:
            if cursor:
                cursor.close()
                

    def __init__(self):
        self.conn = DBConnection().get_connection()

    def display_appointments(self, doc_id: int) -> List[Appointment]:
        """Fetch all appointments for a specific doctor by doctor ID"""
        appointments: List[Appointment] = []
        cursor = None
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(self.DISPLAY_APPOINTMENTS, (doc_id,))
            rows = cursor.fetchall()

            for row in rows:
                appointments.append(
                    Appointment(
                        app_id=row["app_id"],
                        patient_id=row["patient_id"],
                        first_name=row["first_name"],
                        last_name=row["last_name"],
                        dob=row["dob"],
                        app_date=row["app_date"],
                        gender=row["gender"]
                    )
                )
        except Exception as e:
            print("❌ Error fetching appointments:", e)
        finally:
            if cursor:
                cursor.close()
        return appointments

    def find_by_app_id(self, app_id: int) -> Optional[Appointment]:
        """Find a single appointment by appointment ID"""
        appointment: Optional[Appointment] = None
        cursor = None
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(self.FIND_BY_APP_ID, (app_id,))
            row = cursor.fetchone()

            if row:
                appointment = Appointment(
                    app_id=row["app_id"],
                    patient_id=row["patient_id"],
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                    dob=row["dob"],
                    app_date=row["app_date"],
                    gender=row["gender"]
                )
        except Exception as e:
            print("❌ Error finding appointment:", e)
        finally:
            if cursor:
                cursor.close()
        return appointment
    
    def fetch_medicines(self) -> List[Dict]:
        """Fetch all medicines from the medicine table"""
        medicines: List[Dict] = []
        cursor = None
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(self.FETCH_MEDICINES)
            medicines = cursor.fetchall()
        except Exception as e:
            print("❌ Error fetching medicines:", e)
        finally:
            if cursor:
                cursor.close()
        return medicines

    def create_prescription(self, pre_id: int, patient_id: int, doc_id: int, med_id: int, dosage: str, duration: str, pre_date: str) -> bool:
        """Insert a prescription record into med_prescription"""
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.CREATE_PRESCRIPTION, (pre_id, patient_id, doc_id, med_id, dosage, duration, pre_date))
            self.conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print("❌ Error creating prescription:", e)
            return False
        finally:
            if cursor:
                cursor.close()

