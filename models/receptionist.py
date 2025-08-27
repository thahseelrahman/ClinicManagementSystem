import re
from datetime import date,time,datetime
#Patient class for getting and setting patient informations
class Patient:
    'Python OOPs applied'
    def __init__(self,patient_id = None,first_name = None,last_name = None,dob = None,blood_group = None,gender = None,phone_no = None,address = None,email = None,reg_date = None):
        self.__patient_id = patient_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__dob = dob
        self.__blood_group = blood_group
        self.__gender = gender
        self.__phone_no = phone_no
        self.__address = address
        self.__email = email
        self.__reg_date = reg_date

    #getters and setters

    #patient id
    def get_patient_id(self):
        return self.__patient_id

    def set_patient_id(self, patient_id):
        self.__patient_id = patient_id

    #first name
    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        'validate first name'
        pattern = re.compile(r"^[A-Za-z]+$")
        if pattern.match(first_name):
            self.__first_name = first_name
        else:
            raise ValueError("Invalid first name. Only alphabetic characters are allowed.")

    #last name
    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        'validate last name'
        pattern = re.compile(r"^[A-Za-z]+$")
        if pattern.match(last_name):
            self.__last_name = last_name
        else:
            raise ValueError("Invalid lastname name. Only alphabetic characters are allowed.")

    #date of birth
    def get_dob(self):
        return self.__dob

    def set_dob(self, dob):
        if isinstance(dob,date):
            self.__dob = dob
        else:
            raise ValueError("Invalid date of birth. Please provide a valid date.")

    #blood group
    def get_blood_group(self):
        return self.__blood_group

    def set_blood_group(self, blood_group):
        groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
        if blood_group in groups:
            self.__blood_group = blood_group
        else:
            raise ValueError("Invalid blood group. Please provide a valid blood group.")

    #gender
    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender in ["M", "F", "O"]:
            self.__gender = gender
        else:
            raise ValueError("Invalid gender. Please provide a valid gender.")

    #phone number
    def get_phone_no(self):
        return self.__phone_no
 
    def set_phone_no(self, phone_no):
        #integer with 10 digits
        if isinstance(phone_no, str) and phone_no.isdigit() and len(phone_no) == 10:
            self.__phone_no = phone_no
        else:
            raise ValueError("Invalid phone number. Please provide a valid phone number.")

    #address
    def get_address(self):
        return self.__address

    def set_address(self, address):
        pattern = re.compile(r"^[A-Za-z0-9\s,.-]+$")
        if pattern.match(address):
            self.__address = address
        else:
            raise ValueError("Invalid address. Please provide a valid address.")

    #email
    def get_email(self):
        return self.__email

    def set_email(self, email):
        pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        if pattern.match(email):
            self.__email = email
        else:
            raise ValueError("Invalid email address. Please provide a valid email address.")

    #registration date
    def get_reg_date(self):
        return self.__reg_date

    def set_reg_date(self, reg_date):
        #date cant be in the past
        if isinstance(reg_date,date):
            if reg_date < date.today():
                raise ValueError("Invalid registration date. Registration date cannot be in the past.")
            self.__reg_date = reg_date
        else:
            raise ValueError("Invalid registration date. Please provide a valid date.")

    def __str__(self):
        return f"=====PATIENTS LIST=======\n------------------\nPatient Id: {self.__patient_id}\nFirst Name: {self.__first_name}\nLast Name: {self.__last_name}\nDate of Birth: {self.__dob}\nBlood Group: {self.__blood_group}\nGender: {self.__gender}\nPhone No: {self.__phone_no}\nAddress: {self.__address}\nEmail: {self.__email}\nRegistration Date: {self.__reg_date}\n=========================="

#patient class created successfully

#appointment class
class Appointment:
    def __init__(self, app_id=None, token_no=None, patient_id=None, doctor_id=None, appointment_date=None, appointment_time=None, status=None, symptoms=None, diagnosis=None):
        self.__app_id = app_id
        self.__token_no = token_no
        self.__patient_id = patient_id
        self.__doctor_id = doctor_id
        self.__appointment_date = appointment_date
        self.__appointment_time = appointment_time
        self.__status = status
        self.__symptoms = symptoms
        self.__diagnosis = diagnosis
        self.__status = status

    #getters and setters

    #appointment id
    def get_appointment_id(self):
        return self.__app_id

    def set_appointment_id(self, app_id):
        self.__app_id = app_id

    #token number
    def get_token_no(self):
        return self.__token_no

    def set_token_no(self, token_no):
        #sequence for token number 
        if isinstance(token_no, int) and token_no > 0:
            self.__token_no = token_no
        else:
            raise ValueError("Invalid token number. Please provide a valid token number.")

    #patient id
    def get_patient_id(self):
        return self.__patient_id

    def set_patient_id(self, patient_id):
        self.__patient_id = patient_id

    #doctor id
    def get_doctor_id(self):
        return self.__doctor_id

    def set_doctor_id(self, doctor_id):
        self.__doctor_id = doctor_id

    #appointment date
    def get_appointment_date(self):
        return self.__appointment_date

    def set_appointment_date(self, appointment_date):
        #date cant be in the past
        if appointment_date < date.today():
            raise ValueError("Invalid appointment date. Appointment date cannot be in the past.")
        if isinstance(appointment_date, date):
            self.__appointment_date = appointment_date
        else:
            raise ValueError("Invalid appointment date. Please provide a valid date.")

    #appointment time
    def get_appointment_time(self):
        return self.__appointment_time

    def set_appointment_time(self, appointment_time):
        #time should not be in the past
        if appointment_time < datetime.now().time():
            raise ValueError("Invalid appointment time. Please provide a valid time.")
        if isinstance(appointment_time, time):
            self.__appointment_time = appointment_time
        else:
            raise ValueError("Invalid appointment time. Please provide a valid time.")

    #status
    def get_status(self):
        return self.__status

    def set_status(self, status):
        if status in ["Scheduled", "Completed", "Cancelled"]:
            self.__status = status
        else:
            raise ValueError("Invalid status. Please provide a valid status.")
        
    #symptoms
    def get_symptoms(self):
        return self.__symptoms

    def set_symptoms(self, symptoms):
        self.__symptoms = symptoms

    #diagnosis
    def get_diagnosis(self):
        return self.__diagnosis

    def set_diagnosis(self, diagnosis):
        self.__diagnosis = diagnosis

    def __str__(self):
        return f"====APPOINTMENTS====\n-----------------------\nAppointment Id: {self.__app_id}\nToken No: {self.__token_no}\nPatient Id: {self.__patient_id}\nDoctor Id: {self.__doctor_id}\nAppointment Date: {self.__appointment_date}\nAppointment Time: {self.__appointment_time}\nStatus: {self.__status}\nSymptoms: {self.__symptoms}\nDiagnosis: {self.__diagnosis}\n-----------------------"
