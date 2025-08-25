from db.db_connection import DBConnection
from lib.ReceptionistManagement import ReceptionmanagementLib
def main():
    while True:
        # db = DBConnection()
        # conn = db.get_connection()
        print("\n==========PATIENT MANAGEMENT MENU==========")
        print("1. ADD PATIENT")
        print("2. GET PATIENT")
        print("3. UPDATE PATIENT")
        print("4. DELETE PATIENT")
        print("\n========APPOINTMENT MANAGEMENT========")
        print("5. SCHEDULE APPOINTMENT")
        print("6. EDIT APPOINTMENT")
        print("7. CANCEL APPOINTMENT")
        print("8. GET APPOINTMENT")
        print("9. EXIT")
        choice = input("Enter your choice : ")
        if choice == "1":
            ReceptionmanagementLib.add_patient()
        elif choice == "2":
            ReceptionmanagementLib.get_patient()
        elif choice == "3":
            ReceptionmanagementLib.update_patient()
        elif choice == "4":
            ReceptionmanagementLib.delete_patient()
        elif choice == "5":
            ReceptionmanagementLib.schedule_appointment()
        elif choice == "6":
            ReceptionmanagementLib.update_appointment()
        elif choice == "7":
            ReceptionmanagementLib.cancel_appointment()
        elif choice == "8":
            ReceptionmanagementLib.get_appointment()
        elif choice == "9":
            break
        else:
            print("Invalid choice!! Try again!!")
        
if __name__ == "__main__":
    main()
