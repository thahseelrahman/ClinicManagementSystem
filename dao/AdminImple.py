from db.db_connection import DBConnection
from dao.AdminAbstract import AdminAbstarct
from typing import List
from models.admin import Staff,Credential

class Admindaosurvice(AdminAbstarct):
    DISPLAY_ALL = "SELECT * FROM staff"
    INSERT_STAFF = "INSERT INTO staff(dept_id,first_name,last_name,role_id,age,gender,phone_no,email,address,date_of_join,is_active) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    INSERT_CREDENTIAL = "INSERT INTO credentials(user_name,password,staff_id,role_id) VALUES (%s,%s,%s,%s)"
    DISPLAY_STAFF = "SELECT * FROM clinic_db.staff where staff_id = (SELECT max(staff_id) FROM clinic_db.staff)"
    # FIND_BY_ID = "SELECT * FROM products WHERE productid = %s"
    # UPDATE_PRODUCT = "UPDATE products SET productname = %s,unitprice = %s WHERE productid = %s"
    # FIND_BY_NAME = "SELECT * FROM products WHERE productname = %s"
    # DISABLE_PRODUCT = "UPDATE products SET isactive = %s WHERE productname = %s"
    def __init__(self):
        self.conn = DBConnection().get_connection()
    def add_staff(self,staff:Staff):
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.INSERT_STAFF,(staff.get_dept_id(),staff.get_first_name(),staff.get_last_name(),staff.get_role_id(),staff.get_age(),staff.get_gender(),staff.get_phone_no(),staff.get_email(),staff.get_address(),staff.get_date_of_join(),staff.get_is_active()))
            self.conn.commit()
            return cursor.rowcount == 1
        except Exception as e:
            print("Error inserting product:",e)
            return False
        finally:
            cursor.close()
    def display_staff(self)->List[Staff]:
        Staffs = []
        try:
            cursor = self.conn.cursor(dictionary = True)
            cursor.execute(self.DISPLAY_ALL)
            rows = cursor.fetchall()
            for row in rows:
                Staffs.append(Staff(staff_id = row["staff_id"],
                                        dept_id = row["dept_id"],
                                        first_name = row["first_name"],
                                        last_name= row["last_name"],
                                        role_id = row["role_id"],
                                        age= row["age"],
                                        gender= row["gender"],
                                        phone_no =  row["phone_no"],
                                        email = row["email"],
                                        address= row["address"],
                                        date_of_join = row["date_of_join"],
                                        is_active = row["is_active"]))
        except Exception as e:
            print("Error fetching products:",e)    
        finally:
            cursor.close()
        return Staffs
    def add_credential(self,credential:Credential):
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.INSERT_CREDENTIAL,(credential.get_username(),credential.get_password(),credential.get_staff_id(),credential.get_role_id()))
            self.conn.commit()
            return cursor.rowcount == 1
        except Exception as e:
            print("Error inserting product:",e)
            return False
        finally:
            cursor.close()
    def display_staff_id(self)->Staff:
        try:
            cursor = self.conn.cursor(dictionary = True)
            cursor.execute(self.DISPLAY_STAFF)
            rows = cursor.fetchall()
            for row in rows:
                staff = (Staff(staff_id = row["staff_id"],
                                        dept_id = row["dept_id"],
                                        first_name = row["first_name"],
                                        last_name= row["last_name"],
                                        role_id = row["role_id"],
                                        age= row["age"],
                                        gender= row["gender"],
                                        phone_no =  row["phone_no"],
                                        email = row["email"],
                                        address= row["address"],
                                        date_of_join = row["date_of_join"],
                                        is_active = row["is_active"]))
        except Exception as e:
            print("Error fetching products:",e)    
        finally:
            cursor.close()
        return staff
