import re
from datetime import date
# Department class created
class Department:
    'class for getting and setting department'
    def __init__(self,dept_id:None,dept_name:None,description:None):
        self.__dept_id = dept_id
        self.__dept_name = dept_name
        self.__description = description

    #get department id function created
    def get_dept_id(self):
        return self.__dept_id
    #set department id function created
    def set_dept_id(self,dept_id):
        self.__dept_id = dept_id

    #get department name function created
    def get_dept_name(self):
        return self.__dept_name
    #set department name function created
    def set_dept_id(self,dept_name):
        self.__dept_name = dept_name

    #get department description function created
    def get_description (self):
        return self.__description
    #set department description function created
    def set_dept_id(self,description):
        self.__description = description
#________________________________________________________________________________________________
# Staff class created
class Staff:
    'class for getting and setting staff information'
    def __init__(self,staff_id=None,dept_id=None,first_name=None,last_name=None,role_id=None,age=None,gender=None,phone_no=None,email=None,address=None,date_of_join=None,is_active=None):
        self.__staff_id = staff_id
        self.__dept_id = dept_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__role_id = role_id
        self.__age = age
        self.__gender = gender
        self.__phone_no = phone_no
        self.__email = email
        self.__address = address
        self.__date_of_join = date_of_join
        self.__is_active = is_active
    #getter for staff id
    def get_staff_id(self):
        return self.__staff_id
    #setter for staff id
    def set_staff_id(self,staff_id):
        self.__staff_id = staff_id
    #getter for department id     
    def get_dept_id(self):
        return self.__dept_id
    #setter for department id
    def set_dept_id(self,dept_id):
        self.__dept_id = dept_id
    #getter for first name
    def get_first_name(self):
        return self.__first_name
    #setter for first name
    def set_first_name(self,first_name):
        pattern = re.compile("^[A-Za-z]+$")
        if pattern.match(first_name):
            self.__first_name = first_name
        else:
            raise ValueError("Invalid first name")
    #getter for last name
    def get_last_name(self):
        return self.__last_name
    #setter for last name
    def set_last_name(self,last_name):
        pattern = re.compile("^[A-Za-z]+$")
        if pattern.match(last_name):
            self.__last_name = last_name
        else:
            raise ValueError("Invalid last name")
    #getter for role
    def get_role_id(self):
        return self.__role_id
    #setter for role
    def set_role_id(self,role_id:int):
        self.__role_id = role_id
    #getter for age
    def get_age(self):
        return self.__age
    #setter for age
    def set_age(self,age:int):
        if age > 17:
            self.__age = age
        else:
            raise ValueError("Invalid age")
    #getter for gender
    def get_gender(self):
        return self.__gender
    #setter for gender
    def set_gender(self,gender):
        genders = ["M","F","O"]
        if gender in genders:
            self.__gender = gender
        else:
            raise ValueError("Invalid gender")
    #getter for phone number
    def get_phone_no(self):
        return self.__phone_no
    #setter for phone number
    def set_phone_no(self,phone_no):
        pattern = re.compile("^[0-9]{10}$")
        if not pattern.match(phone_no):
            raise ValueError("Invalid phone number")
        self.__phone_no = phone_no
    #getter for email
    def get_email(self):
        return self.__email
    #setter for email
    def set_email(self,email):
        pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        if not pattern.match(email):
            raise ValueError("Invalid email format")
        self.__email = email
    #getter for address
    def get_address(self):
        return self.__address
    #setter for address
    def set_address(self,address):
        if len(address) < 10:
            raise ValueError("Address too short")
        if not isinstance(address, str):
            raise ValueError("Invalid address format")
        self.__address = address
    #getter for date of joining
    def get_date_of_join(self):
        return self.__date_of_join
    #setter for date of joining
    def set_date_of_join(self,date_of_join):
        if not isinstance(date_of_join,date):
            raise ValueError("Invalid date format")
        self.__date_of_join = date_of_join
    #getter for is_active
    def get_is_active(self):
        return self.__is_active
    #setter for is_active
    def set_is_active(self,is_active):
        self.__is_active = is_active
    
    def __str__(self):
        return f"\nStaff Id: {self.get_staff_id()}\nDepartment Id: {self.get_dept_id()}\nFirst Name: {self.get_first_name()}\nLast Name: {self.get_last_name()}\nRole id: {self.get_role_id()}\nAge {self.get_age()}\nGender: {self.get_gender()}\nPhone No: {self.get_phone_no()}\nEmail: {self.get_email()}\nAddress: {self.get_address()}\nDate of join: {self.get_date_of_join()}\nActive: {self.get_is_active()}"
#-----------------------------------------------------------------------------------------------
#created role class 
class Role:
    'class for getting and setting roles of staffs'
    def __init__(self,role_id=None,role=None):
        self.__role_id = role_id
        self.__role = role
    #getter for role_id
    def get_role_id(self):
        return self.__role_id
    #setter for role_id
    def set_role_id(self,role_id:int):
        self.__role_id = role_id
    #getter for role name
    def get_role_name(self):
        return self.__role
    #setter for role name
    def set_role_name(self,role):
        self.__role = role
    # def __str__(self):
    #     return f"\nStaff Id: {self.get_staff_id}\nDepartment Id: {self.get_dept_id}\nFirst Name: {self.get_first_name}\nLast Name: {self.get_last_name}\nRole id: {self.get_role_id}\nAge {self.get_age}\nGender: {self.get_gender}\nPhone No: {self.get_phone_no}\nEmail: {self.get_email}\nAddress: {self.get_address}\nDate of join: {self.get_date_of_join}\nActive: {self.get_is_active}"
#---------------------------------------------------------------------------------------------------------
#create credential class
class Credential:
    def __init__(self,username=None,password=None,staff_id=None,role_id=None):
        self.__username = username
        self.__password = password
        self.__staff_id = staff_id
        self.__role_id = role_id
    #getter for username
    def get_username(self):
        return self.__username
    #setter for username
    def set_username(self,username):
        pattern = re.compile(r'^[a-zA-Z0-9]{6,}$')
        if not pattern.match(username):
            raise ValueError("Invalid username should be include alphabets and digits and contain minimum 6 digit ")
        self.__username = username
    #getter for password
    def get_password(self):
        return self.__password
    #setter for password
    def set_password(self,password):
        pattern = re.compile(r'^[a-zA-Z0-9._%+-]{6,}$')
        if not pattern.match(password):
            raise ValueError("Invalid username should be include alphabets and special character and contain minimum 6 digit ")
        self.__password = password
    #getter for staff id
    def get_staff_id(self):
        return self.__staff_id
    #setter for staff id
    def set_staff_id(self,staff_id):
        self.__staff_id = staff_id
    #getter for role id 
    def get_role_id(self):
        return self.__role_id
    #setter for role id
    def set_role_id(self,role_id):
        self.__role_id = role_id
#create doctor class
class Doctor:
    def __init__(self,doc_id=None,staff_id=None,spec_id=None,consultation_fee=None,availability=None):
        self.__doc_id = doc_id
        self.__staff_id = staff_id
        self.__spec_id = spec_id
        self.__consultation_fee = consultation_fee
        self.__availability = availability
    #getter for doctor id
    def get_doc_id(self):
        return self.__doc_id
    #setter for doctor id
    def set_doc_id(self,doc_id):
        self.__doc_id = doc_id
    #getter for staff id
    def get_staff_id(self):
        return self.__staff_id
    #setter for staff id
    def set_staff_id(self,staff_id):
        self.__staff_id = staff_id
    #getter for specification
    def get_spec_id(self):
        return self.__spec_id
    #setter for specification
    def set_spec_id(self,spec_id):
        self.__spec_id = spec_id
    #getter for consultation fee 
    def get_consultation_fee(self):
        return self.__consultation_fee
    #setter for consultation fee
    def set_consultation_fee(self,consultation_fee):
        self.__consultation_fee = consultation_fee
    #getter for availability
    def get_availability(self):
        return self.__availability
    #setter for availability
    def set_availability(self,availability):
        self.__availability = availability
#create specification class
class Specialization:
    def __init__(self,spec_id=None,specialization = None):
        self.__spec_id = spec_id
        self.__specialization = specialization
    #getter for specificatio id
    def get_spec_id(self):
        return self.__spec_id
    # setter for specification id
    def set_spec_id(self,spec_id):
        self.__spec_id = spec_id
    #getter for specificatio name
    def get_specification(self):
        return self.__specialization
    # setter for specification name
    def set_specification(self,specialization):
        self.__specialization = specialization



    
        

    
