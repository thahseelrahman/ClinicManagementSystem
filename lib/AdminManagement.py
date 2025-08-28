from dao.AdminAbstract import AdminAbstarct
from dao.AdminImple import Admindaosurvice
from models.admin import Staff,Credential
from datetime import datetime, date
class AdminManagementLib:
    dao_service: AdminAbstarct =Admindaosurvice()
    @staticmethod
    def display_all():
        staffs = AdminManagementLib.dao_service.display_staff()
        for staff in staffs:
            print(staff)
    @staticmethod
    def add_staff():
        staff = Staff()
        dept_id = int(input("Enter the departmnet id:"))
        staff.set_dept_id(dept_id)
        first_name = input("Enter first name of staff: ")
        staff.set_first_name(first_name)
        last_name = input("Enter last name of staff")
        staff.set_last_name(last_name)
        role_id = int(input("enter the role id: "))
        staff.set_role_id(role_id)
        age = int(input("Enter the age")) 
        staff.set_age(age)
        gender = input("Enter the gender(M/F/O)")
        staff.set_gender(gender)
        phone_no = input("Enter your phone no: ")
        staff.set_phone_no(phone_no)
        email = input("Enter your email:")
        staff.set_email(email)
        address = input('Enter the address: ')
        staff.set_address(address)
        date_of_join = input("enter the joining date(DD/MM/YYYY):") or date.today()
        if isinstance(date_of_join,str):
            util_date = datetime.strptime(date_of_join,"%d/%m/%Y")
            conv_j_date = util_date.date()
        else:
            conv_j_date = date_of_join
        staff.set_date_of_join(conv_j_date)
        staff.set_is_active("Y")

        if AdminManagementLib.dao_service.add_staff(staff):
            print("successfully added...")
        else:
            print("not done yet")
        choice = input("\nIs Staff need credential to access?(y/n)")
        if choice.lower().strip() == "y":
            staf:Staff=None
            credential = Credential()
            username = input("Enter Username: ")
            credential.set_username(username = username)
            password = input("Enter Password: ")
            credential.set_password(password = password)
            staf = AdminManagementLib.dao_service.display_staff_id()
            print(staf)
            credential.set_staff_id(staf.get_staff_id())
            credential.set_role_id(staf.get_role_id())
            if AdminManagementLib.dao_service.add_credential(credential):
                print("successfully added...")
            else:
                print("not done yet")

            

