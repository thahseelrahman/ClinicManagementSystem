from db.db_connection import DBConnection
from dao.AdminAbstract import AdminAbstarct
from typing import List
from models.admin import Staff,Credential,Doctor,Specialization

class Admindaosurvice(AdminAbstarct):
    DISPLAY_ALL = "SELECT * FROM staff"
    INSERT_STAFF = "INSERT INTO staff(dept_id,first_name,last_name,role_id,age,gender,phone_no,email,address,date_of_join,is_active) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    INSERT_CREDENTIAL = "INSERT INTO credentials(user_name,password,staff_id,role_id) VALUES (%s,%s,%s,%s)"
    DISPLAY_STAFF = "SELECT * FROM clinic_db.staff where staff_id = (SELECT max(staff_id) FROM clinic_db.staff)"
    DISPLAY_ROLE = "SELECT r.role_name FROM role r JOIN credentials c ON c.role_id = r.role_id WHERE user_name = %s"
    DISPLAY_ROLES = "SELECT r.role_name FROM role r JOIN credentials c ON c.role_id = r.role_id WHERE password = %s"
    INSERT_DOC = "INSERT INTO doctor(staff_id,spec_id,consultation_fee,availability) VALUES (%s,%s,%s,%s)"
    INSERT_SPEC = "INSERT INTO specialization(specialization) VALUES (%s)"
    SEARCH_BY_ID = "SELECT * FROM staff WHERE staff_id = %s"
    UPDATE_STAFF = "UPDATE staff SET first_name = %s,last_name = %s,phone_no = %s,email = %s,address = %s WHERE staff_id = %s"
    DISPLAY_DOC_ID = "SELECT d.doc_id FROM role r JOIN credentials c ON c.role_id = r.role_id JOIN doctor d ON c.staff_id = d.staff_id WHERE c.user_name = %s"
    DISABLE_STAFF = "UPDATE staff SET is_active = %s WHERE staff_id = %s"
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
    def check_username(self, username):
        row =None
        try:
            cursor = self.conn.cursor(dictionary = True)
            cursor.execute(self.DISPLAY_ROLE,(username,))
            row = cursor.fetchone()
            # for row in rows:
            #     staff = (Credential(username = row))
        except Exception as e:
            print("Error fetching products:",e)    
        finally:
            cursor.close()
        return row
    def check_password(self, password):
        row =None
        try:
            cursor = self.conn.cursor(dictionary = True)
            cursor.execute(self.DISPLAY_ROLES,(password,))
            row = cursor.fetchone()
            # for row in rows:
            #     staff = (Credential(username = row))
        except Exception as e:
            print("Error fetching products:",e)    
        finally:
            cursor.close()
        return row
    def staff_specialization(self,doctor:Doctor):
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.INSERT_DOC,(doctor.get_staff_id(),doctor.get_spec_id(),doctor.get_consultation_fee(),doctor.get_availability()))
            self.conn.commit()
            return cursor.rowcount == 1
        except Exception as e:
            print("Error inserting product:",e)
            return False
        finally:
            cursor.close()
    def specialization(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.INSERT_SPEC,(Specialization.get_specification(),))
            self.conn.commit()
            return cursor.rowcount == 1
        except Exception as e:
            print("Error specialization:",e)
            return False
        finally:
            cursor.close()
    def diable_staff(self,staff_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.DISABLE_STAFF,("N",staff_id))
            self.conn.commit()
            return cursor.rowcount == 1
        except Exception as e:
            print("Error disabling staff :",e)
            return False
        finally:
            cursor.close()
    def update_staff(self,staff_id,staf:Staff):
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.UPDATE_STAFF,(staf.get_first_name(),
                                                staf.get_last_name(),
                                                staf.get_phone_no(),
                                                staf.get_email(),
                                                staf.get_address(),
                                                staff_id))
            self.conn.commit()
            return cursor.rowcount == 1
        except Exception as e:
            print("Error updating staff :",e)
            return False
        finally:
            cursor.close()
    def search_by_id(self,staff_id):
        try:
            cursor = self.conn.cursor(dictionary = True)
            cursor.execute(self.SEARCH_BY_ID,(staff_id,))
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
    def check_doc_id(self, username):
        row =None
        try:
            cursor = self.conn.cursor(dictionary = True)
            cursor.execute(self.DISPLAY_DOC_ID,(username,))
            row = cursor.fetchone()
            # for row in rows:
            #     staff = (Credential(username = row))
        except Exception as e:
            print("Error fetching products:",e)    
        finally:
            cursor.close()
        return row
        
    

