from lib.AdminManagement import AdminManagementLib
def adminmain():

    while True:
        print("\n==============product management menu=================")
        print("1.add staff")
        print("2.display staff")
        print("3.update staff")
        print("4.search staff by id")
        print("5.disable staff")
        print("6.exit")
        choice = int(input("enter your choice"))
        if choice == 1:
            AdminManagementLib.add_staff()
        elif choice == 2:
            AdminManagementLib.display_all()
        # elif choice == 3:
        #     AdminManagementLib.update_staff()
        # elif choice == 4:
        #     AdminManagementLib.search_staff()
        # elif choice == 5:
        #     AdminManagementLib.disable_staff()
        elif choice == 6:
            break