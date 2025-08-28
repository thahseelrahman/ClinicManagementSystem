from dao.AdminAbstract import AdminAbstarct
from dao.AdminImple import Admindaosurvice
from models.admin import Staff,Credential
from datetime import datetime, date
from adminmain import adminmain
from mainpharm import pharmamain
from receptionistmain import receptionmain
def main():
    dao_service: AdminAbstarct =Admindaosurvice()
    while True:
        print("\n------------------login-----------------------------")
        username = input("Enter the username: ") 
        password = input("Enter the password: ")  
        try:
            if dao_service.check_username(username)['role_name'] == dao_service.check_password(password)['role_name']:
                match dao_service.check_username(username)['role_name']:
                    case "admin":
                        adminmain()
                    case "receptionist":
                        receptionmain()
                    case "doctor":
                        # doctormenudrive(dao_service.check_doc_id(username)['doc_id'])
                        pass
                    case "pharmasist":
                        pharmamain()
                    case "labtechnicion":
                        # labtechmenudrive()
                        pass
                    case _:
                        print("something occured when searching username")
        except Exception as e:
            print("Worng username or password!!!")

if __name__ == "__main__":
    main()
