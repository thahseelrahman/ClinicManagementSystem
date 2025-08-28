import mysql.connector
from datetime import datetime

# ---------------- Model Class ----------------
class Appointment:
    def __init__(self, app_id=None, patient_id=None, first_name=None, last_name=None, dob=None, app_date=None, gender=None):
        self.__app_id = app_id
        self.__patient_id = patient_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__dob = dob
        self.__app_date = app_date
        self.__gender = gender
        self.__age = self.calculate_age() if dob and app_date else None

    # --------- Getters ----------
    def get_app_id(self): return self.__app_id
    def get_patient_id(self): return self.__patient_id
    def get_first_name(self): return self.__first_name
    def get_last_name(self): return self.__last_name
    def get_dob(self): return self.__dob
    def get_app_date(self): return self.__app_date
    def get_gender(self): return self.__gender
    def get_age(self): return self.__age

    # --------- Setters ----------
    def set_app_id(self, app_id): self.__app_id = app_id
    def set_patient_id(self, patient_id): self.__patient_id = patient_id
    def set_first_name(self, first_name): self.__first_name = first_name
    def set_last_name(self, last_name): self.__last_name = last_name
    def set_dob(self, dob): self.__dob = dob
    def set_app_date(self, app_date): self.__app_date = app_date
    def set_gender(self, gender): self.__gender = gender
    def set_age(self, age): self.__age = age

    def calculate_age(self):
        try:
            dob_dt = datetime.strptime(str(self.__dob), '%Y-%m-%d')
            app_dt = datetime.strptime(str(self.__app_date), '%Y-%m-%d')
            age = app_dt.year - dob_dt.year - ((app_dt.month, app_dt.day) < (dob_dt.month, dob_dt.day))
            return age
        except Exception:
            return None

    # --------- Display ----------
    def display_patient_details(self):
        details = (
            f"Appointment ID: {self.__app_id}, "
            f"Patient ID: {self.__patient_id}, "
            f"Name: {self.__first_name} {self.__last_name}"
        )
        if self.__gender is not None:
            details += f", Gender: {self.__gender}"
        if self.__age is not None:
            #age should be greater than 0
            if self.__age > 0:
                details += f", Age: {self.__age}"
            else:
                details += ", Age: N/A"
        print(details)


