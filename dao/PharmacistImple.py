from dao.PharmacistAbstract import PharmacistDaoService
from db.db_connection import DBConnection
from models.pharmacist import Pharmacist
from typing import List

class PharmacistDaoImplementation(PharmacistDaoService):
    """Implementation for abstract PharmacistDaoService"""

    DISPLAY_ALL_MEDICINES = "SELECT * FROM Medicine"
    INSERT_MEDICINE = """INSERT INTO Medicine(med_name, generic_name, manufacturer, unit_rate, stock, expiry_date) 
                         VALUES (%s, %s, %s, %s, %s, %s)"""
    FIND_MEDICINE_BY_ID = "SELECT * FROM Medicine WHERE med_id=%s"
    UPDATE_MEDICINE = """UPDATE Medicine SET med_name = %s,generic_name = %s,manufacturer = %s,unit_rate = %s,
    stock = %s,expiry_date = %s WHERE med_id = %s"""


    DELETE_MEDICINE = "DELETE FROM Medicine WHERE med_id=%s"
    UPDATE_STOCK = "UPDATE Medicine SET stock=%s WHERE med_id=%s"


    INSERT_BILL = """INSERT INTO bill (bill_type, patient_id, ref_id, total_amount, status, bill_date) 
                     VALUES (%s, %s, %s, %s, %s, %s)"""
    FIND_BILL_BY_ID = "SELECT * FROM bills WHERE bill_id=%s"
    UPDATE_BILL = """UPDATE bill 
                     SET bill_type=%s, patient_id=%s, ref_id=%s, total_amount=%s, status=%s, bill_date=%s 
                     WHERE bill_id=%s"""
    DELETE_BILL = "DELETE FROM bill WHERE bill_id=%s"
    LIST_BILLS = "SELECT * FROM bill"
    PAY_BILL = "UPDATE bill SET status='PAID' WHERE bill_id=%s"

    def __init__(self):
        self.conn = DBConnection().get_connection()

    def add_medicine(self, medicine: Pharmacist) -> bool:
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.INSERT_MEDICINE, (
                medicine.get_med_name(),
                medicine.get_generic_name(),
                medicine.get_manufacturer(),
                medicine.get_unit_rate(),
                medicine.get_stock(),
                medicine.get_expiry_date()
            ))
            self.conn.commit()
            return cursor.rowcount == 1
        except Exception as e:
            print("Error inserting medicine:", e)
            return False
        finally:
            cursor.close()
    def search_medicines(self, med_id: int):
        medicine = None
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(self.FIND_MEDICINE_BY_ID, (med_id,))
            row = cursor.fetchone()
            if row:
                medicine = Pharmacist(
                    med_id=row["med_id"],
                    med_name=row["med_name"],
                    generic_name=row["generic_name"],
                    manufacturer=row["manufacturer"],
                    unit_rate=row["unit_rate"],
                    stock=row["stock"],
                    expiry_date=row["expiry_date"]
                )
        except Exception as e:
            print("Error fetching medicine:", e)
        finally:
            cursor.close()
        return medicine

    def update_medicine(self, med_id: int, medicine: Pharmacist) -> bool:
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.UPDATE_MEDICINE,(
                medicine.get_med_name(),
                medicine.get_generic_name(),
                medicine.get_manufacturer(),
                medicine.get_unit_rate(),
                medicine.get_stock(),
                medicine.get_expiry_date(),
                med_id
            )
        )
            self.conn.commit()
            return cursor.rowcount == 1
        except Exception as e:
            print("Error updating medicine:", e)
            return False
        finally:
            cursor.close()


    def delete_medicine(self, med_id: int) -> bool:
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.DELETE_MEDICINE, (med_id,))
            self.conn.commit()
            return cursor.rowcount == 1
        except Exception as e:
            print("Error deleting medicine:", e)
            return False
        finally:
            cursor.close()

    def display_all_medicines(self) -> List[Pharmacist]:
        medicines = []
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(self.DISPLAY_ALL_MEDICINES)
            rows = cursor.fetchall()
            for row in rows:
                medicines.append(Pharmacist(
                    med_id=row["med_id"],
                    med_name=row["med_name"],
                    generic_name=row["generic_name"],
                    manufacturer=row["manufacturer"],
                    unit_rate=row["unit_rate"],
                    stock=row["stock"],
                    expiry_date=row["expiry_date"]
                ))
        except Exception as e:
            print("Error listing medicines:", e)
        finally:
            cursor.close()
        return medicines
