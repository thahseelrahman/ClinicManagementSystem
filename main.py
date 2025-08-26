from dao.AdminAbstract import AdminAbstarct
from dao.AdminImple import Admindaosurvice
from models.admin import Staff,Credential
from datetime import datetime, date
from adminmain import adminmain
from mainpharm import pharmamain
def main():
    dao_service: AdminAbstarct =Admindaosurvice()
    while True:
        print("\n------------------login-----------------------------")
        username = input("Enter the username: ") 
        password = input("Enter the password: ")  
        if dao_service.check_username(username)['role_name'] == dao_service.check_password(password)['role_name']:
            match dao_service.check_username(username)['role_name']:
                case "admin":
                    adminmain()
                case "receptionist":
                    # receptmenudrive()
                    pass
                case "doctor":
                    # doctormenudrive()
                    pass
                case "pharmasist":
                    pharmamain()
                case "labtechnicion":
                    # labtechmenudrive()
                    pass
                case _:
                    print("something occured when searching username")

if __name__ == "__main__":
    main()