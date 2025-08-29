from datetime import date
import re
class Pharmacist:
    
    def __init__(self, med_id=None, med_name=None, generic_name=None,
                 manufacturer=None, unit_rate=None, stock=None, expiry_date=None):
          self.__med_id = med_id
          self.__med_name = med_name
          self.__generic_name = generic_name
          self.__manufacturer = manufacturer
          self.__unit_rate = unit_rate
          self.__stock = stock
          self.__expiry_date = expiry_date


    def get_med_id(self): 
        return self.__med_id
    
    def set_med_id(self, med_id):
        if med_id is not None and med_id <= 0:
            raise ValueError("Medicine ID must be positive")
        self.__med_id = med_id


    def get_med_name(self):
        return self.__med_name

    def set_med_name(self, med_name):
        if not isinstance(med_name, str):
            raise ValueError("Medicine name must be a string")
        if len(med_name) < 2:
            raise ValueError("Medicine name must be at least 2 characters long")

        if not re.fullmatch(r"[A-Za-z\- ]+", med_name):
            raise ValueError("Medicine name must only contain letters, spaces, or hyphens")

      
        if not re.search(r"[A-Za-z]", med_name):
            raise ValueError("Medicine name must contain at least one letter")

    
        self.__med_name = med_name.strip()

    def get_generic_name(self):
        return self.__generic_name

    def set_generic_name(self, generic_name):
        if generic_name is None or not str(generic_name).strip():
            raise ValueError("Generic name cannot be empty")
        if not re.match(r"^[A-Za-z\s]+$", generic_name):
            raise ValueError("Generic name must only contain letters and spaces")
        self.__generic_name = generic_name.strip()

    def get_manufacturer(self):
        return self.__manufacturer

    def set_manufacturer(self, manufacturer):
        if manufacturer is None or not str(manufacturer).strip():
            raise ValueError("Manufacturer cannot be empty")
        if not re.match(r"^[A-Za-z\s]+$", manufacturer):
            raise ValueError("Manufacturer must only contain letters and spaces")
        self.__manufacturer = manufacturer.strip()

    def get_unit_rate(self):
        return self.__unit_rate

    def set_unit_rate(self, unit_rate):
        if unit_rate is None:
            raise ValueError("Unit rate cannot be empty")
        if float(unit_rate) <= 0:
            raise ValueError("Unit rate must be greater than 0")
        self.__unit_rate = float(unit_rate)
    def get_stock(self):
        return self.__stock

    def set_stock(self, stock):
        if stock is None:
            raise ValueError("Stock cannot be empty")
        if int(stock) < 0:
            raise ValueError("Stock cannot be negative")
        self.__stock = int(stock)

    def get_expiry_date(self):
        return self.__expiry_date

    def set_expiry_date(self, expiry_date):
        if expiry_date is None:
            self.__expiry_date = None
            return
        if not isinstance(expiry_date, date):
            raise ValueError("Expiry date must be a valid date object")
        if expiry_date <= date.today():
            raise ValueError("Expiry date must be in the future")
        self.__expiry_date = expiry_date

    def __str__(self):
        return f"[{self.__med_id}] {self.__med_name} ({self.__generic_name}) - {self.__manufacturer},"f"Price:{self.__unit_rate} , Stock: {self.__stock} , Exp: {self.__expiry_date}"


# class Bill:
#     def __init__(self,bill_id=None,bill_type=None,patient_id=None,ref_id=None,total_amount=0.0,status="UNPAID",bill_date=None):
#         self.__bill_id = bill_id
#         self.__bill_type = bill_type
#         self.__patient_id = patient_id
#         self.__ref_id = ref_id
#         self.__total_amount = total_amount
#         self.__status = status
#         self.__bill_date = bill_date

    # def __init__(self, bill_id=None, bill_type=None, patient_id=None, ref_id=None, items=None, total_amount=0.0, status="UNPAID", bill_date=None):
    #     self.bill_id = bill_id
    #     self.bill_type = bill_type
    #     self.patient_id = patient_id
    #     self.ref_id = ref_id
    #     self.items = items if items else []
    #     self.total_amount = total_amount
    #     self.status = status
    #     self.bill_date = bill_date

#     def get_bill_id(self):
#         return self.__bill_id
#     def set_bill_id(self, bill_id):
#         self.__bill_id = bill_id

#     def get_bill_type(self):
#         return self.__bill_type
#     def set_bill_type(self, bill_type):
#         self.__bill_type = bill_type

#     def get_patient_id(self):
#         return self.__patient_id
#     def set_patient_id(self, patient_id):
#         self.__patient_id = patient_id

#     def get_ref_id(self):
#         return self.__ref_id
#     def set_ref_id(self, ref_id):
#         self.__ref_id = ref_id

#     def get_total_amount(self):
#         return self.__total_amount
#     def set_total_amount(self, total_amount):
#         self.__total_amount = total_amount

#     def get_status(self):
#         return self.__status
#     def set_status(self, status):
#         self.__status = status

#     def get_bill_date(self):
#         return self.__bill_date
#     def set_bill_date(self, bill_date):
#         self.__bill_date = bill_date

#     def __str__(self):
#         return f"Bill[ID={self.__bill_id}], Type={self.__bill_type}, PatientID={self.__patient_id}, RefID={self.__ref_id}, Total={self.__total_amount}, Status={self.__status}, Date={self.__bill_date}"

