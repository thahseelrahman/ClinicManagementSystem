from lib.AdminManagement import AdminManagementLib
def adminmain():

    while True:
        print("\n==============staff management menu=================")
        print("1.add staff")
        print("2.display staff")
        print("3.update staff")
        print("4.search staff by id")
        print("5.disable staff")
        print("6.exit")
        try:
            choice = int(input("enter your choice: "))
            if choice == 1:
                try:
                    AdminManagementLib.add_staff()
                except Exception as e:
                    print("Error happened in adding staff",e)
            elif choice == 2:
                try:
                    AdminManagementLib.display_all()
                except Exception as e:
                    print("Error happened in display staff",e)
            elif choice == 3:
                try:
                    AdminManagementLib.update_staff()
                except Exception as e:
                    print("Error happened in update staff",e)
            elif choice == 4:
                try:
                    AdminManagementLib.search_staff()
                except Exception as e:
                    print("staff not found!!!")
            elif choice == 5:
                try:
                    AdminManagementLib.disable_staff()
                except Exception as e:
                    print("Error happened in disabling staff",e)
            elif choice == 6:
                break
            else:
                print("invalid choice!!")
        except Exception as e:
            print("Error happened in admin menu", e)
            continue