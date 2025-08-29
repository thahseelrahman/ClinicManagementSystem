from dao.AdminAbstract import AdminAbstarct
from dao.AdminImple import Admindaosurvice
from models.admin import Staff,Credential,Doctor,Specialization
from datetime import datetime, date
class AdminManagementLib:
    dao_service: AdminAbstarct =Admindaosurvice()
    @staticmethod
    def display_all():
        staffs = AdminManagementLib.dao_service.display_staff()
        print("========================List of staff===========================")
        for staff in staffs:
            print(staff)
    @staticmethod
    def add_staff():
        print("========================Staff Details===========================")
        staff = Staff()
        while True:
            try:
                dept_id = int(input("Enter the Departmnet Id: "))
                if staff.set_dept_id(dept_id):
                    break
            except ValueError:
                print("Invalid input. Please enter a valid Department Id.")
                continue
        while True:
            try:
                first_name = input("Enter First Name of Staff: ")
                if staff.set_first_name(first_name.strip()):
                    break
            except ValueError:
                print("Invalid input. Please enter a valid First Name.")
                continue
        while True:
            try:
                last_name = input("Enter Last Name of Staff: ")
                if staff.set_last_name(last_name.strip()):
                    break
            except ValueError:
                print("Invalid input. Please enter a valid Last Name.")
                continue
        while True:
            try:
                role_id = int(input("Enter the Role id: "))
                if staff.set_role_id(role_id):
                    break
            except ValueError:
                print("Invalid input. Please enter a valid Role id.")
                continue
        while True:
            try:
                age = int(input("Enter the age: ")) 
                if staff.set_age(age):
                    break
            except ValueError:
                print("Invalid input. Please enter a valid age.")
                continue
        while True:
            try:
                gender = input("Enter the gender(M/F/O): ")
                if staff.set_gender(gender.strip()):
                    break
            except Exception as e:
                print("Invalid input. Please enter a valid gender.")
                continue
        while True:
            try:
                phone_no = input("Enter your phone no: ")
                if staff.set_phone_no(phone_no.strip()):
                    break
            except Exception as e:
                print("Invalid input. Please enter a valid phone number.")
                continue
        while True:
            try:
                email = input("Enter your email: ")
                if staff.set_email(email.strip()):
                    break
            except Exception as e:
                print("Invalid input. Please enter a valid email.")
                continue
        while True:
            try:
                address = input('Enter the address: ')
                if staff.set_address(address.strip()):
                    break
            except Exception as e:
                print("Invalid input. Please enter a valid address.")
                continue
        while True:
            try:
                date_of_join = input("enter the joining date(DD/MM/YYYY): ") or date.today()
                if isinstance(date_of_join,str):
                    util_date = datetime.strptime(date_of_join,"%d/%m/%Y")
                    conv_j_date = util_date.date()
                else:
                    conv_j_date = date_of_join
                if staff.set_date_of_join(conv_j_date):
                    break
            except Exception as e:
                print("Invalid input.",e)
                continue
        staff.set_is_active("Y")

        if AdminManagementLib.dao_service.add_staff(staff):
            while True:
                if age>24 and role_id == 4:
                    choice = input("Is he is a doctor?(y/n): ")
                    if choice.lower().strip() == "y":
                            staf:Staff = None
                            doctor = Doctor()
                            staf = AdminManagementLib.dao_service.display_staff_id()
                            doctor.set_staff_id(staf.get_staff_id())
                            try:
                                doctor.set_spec_id(input("Enter the Specialization Id: "))
                                if AdminManagementLib.dao_service.staff_specialization(doctor):
                                    print("successfully added...")
                                    break
                                else:
                                    print("not done yet")
                            except Exception as e:
                                print("Invalid input. Please enter a valid Specialization Id.")
                                continue
                    else:
                        break
                else:
                    break
            while True:
                choice = input("\nIs Staff need credential to access?(y/n)")
                if choice.lower().strip() == "y":
                    staf:Staff=None
                    credential = Credential()
                    while True:
                        try:
                            username = input("Enter Username: ")
                            if credential.set_username(username = username):
                                break
                        except Exception as e:
                            print("Invalid input. Please enter a valid Username.")
                            continue
                    while True:
                        try:
                            password = input("Enter Password: ")
                            if credential.set_password(password = password):
                                break
                        except Exception as e:
                            print("Invalid input. Please enter a valid Password.")
                            continue
                    staf = AdminManagementLib.dao_service.display_staff_id()
                    credential.set_staff_id(staf.get_staff_id())
                    credential.set_role_id(staf.get_role_id())
                    if AdminManagementLib.dao_service.add_credential(credential):
                        print("successfully added...")
                        break
                    else:
                        print("not done yet")
                elif choice.lower().strip() == "n":
                    break
                else:
                    print("invalid choice")
                print("successfully added...")
        else:
            print("not done yet")
        
    @staticmethod
    def add_specilization():
        pass
    @staticmethod
    def disable_staff():
        staff_id = input("Enter the staff id: ")
        if AdminManagementLib.dao_service.diable_staff(staff_id):
            print("successfully disabled...")
        else:
            print("not done yet")
    @staticmethod
    def update_staff():
        staf:Staff =None
        staff_id = input("Enter the staff_id: ")
        staf = AdminManagementLib.dao_service.search_by_id(staff_id)
        if staf:
            while True:
                print("\n1.Update Name\n2.Update Phone.no\n3.Update Email\n4.Update Address\n5.Exit")
                choice = int(input("\nEnter your choice (1/2/3/4/5): "))
                match choice:
                    case 1:
                        staf.set_first_name (input("\nEnter the first name: ") or staf.get_first_name())
                        staf.set_last_name(input("Enter the last name: ") or staf.get_last_name())
                    case 2:
                        staf.set_phone_no (input("Enter phone no: ") or staf.get_phone_no())
                    case 3:
                        staf.set_email (input("Enter the email: ") or staf.get_email())
                    case 4:
                        staf.set_address(input("Enter the address: ") or staf.get_address())
                    case 5:
                        break
                    case _:
                        print("Invalid option!!!!!\nTry again")
                if AdminManagementLib.dao_service.update_staff(staff_id,staf):
                    print("successfully updated")
                else:
                    print("something went wrong")
        else:
            print(f"No staff found!!!!")
    @staticmethod
    def search_staff():
        staf:Staff =None
        staff_id = input("Enter the staff_id: ")
        staf = AdminManagementLib.dao_service.search_by_id(staff_id)
        print("=======================Staff detail======================")
        print(staf)



            

