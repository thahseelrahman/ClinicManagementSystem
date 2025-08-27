from db.db_connection import DBConnection
from lib.ReceptionistManagement import ReceptionmanagementLib
def receptionmain():
    while True:
        # db = DBConnection()
        # conn = db.get_connection()
        print("\n==========PATIENT MANAGEMENT MENU==========")
        print("1. ADD PATIENT")
        print("2. GET ALL PATIENTS")
        # print("3. GET PATIENT")
        # print("4. UPDATE PATIENT")
        # print("5. DELETE PATIENT")
        print("\n========APPOINTMENT MANAGEMENT========")
        print("6. SCHEDULE APPOINTMENT")
        print("7. GET ALL APPOINTMENTS")
        # print("8. EDIT APPOINTMENT")
        # print("9. CANCEL APPOINTMENT")
        # print("10. GET APPOINTMENT")
        print("11. EXIT")
        choice = input("Enter your choice : ")
        if choice == "1":
            ReceptionmanagementLib.add_patient()
        elif choice == "2":
            ReceptionmanagementLib.get_all_patients()
        elif choice == "3":
            # ReceptionmanagementLib.get_patient()
            pass
        elif choice == "4":
            # ReceptionmanagementLib.update_patient()
            pass
        elif choice == "5":
            # ReceptionmanagementLib.delete_patient()
            pass
        elif choice == "6":
            ReceptionmanagementLib.schedule_appoinment()
        elif choice == "7":
            ReceptionmanagementLib.get_all_appointments()
        elif choice == "8":
            # ReceptionmanagementLib.update_appointment()
            pass
        elif choice == "9":
            # ReceptionmanagementLib.cancel_appointment()
            pass
        elif choice == "10":
            # ReceptionmanagementLib.get_appointment()
            pass
        elif choice == "11":
            break
        else:
            print("Invalid choice!! Try again!!")