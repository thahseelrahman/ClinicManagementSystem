from lib.DoctorManagement import DoctorManagement

def doctormain():
    while True:
        print("\n=== Doctor Management Menu ===")
        print("1. Display all Appointments for a Doctor")
        print("2. Find Appointment by ID")
        print("3. Update Appointment Notes")
        print("4. Create Prescription")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                DoctorManagement.display_appointments()
                again = input("Do you want to display appointments again? (y/n): ").strip().lower()
                if again != 'y':
                    break
        elif choice == '2':
            while True:
                DoctorManagement.find_appointment_by_id()
                again = input("Do you want to find another appointment? (y/n): ").strip().lower()
                if again != 'y':
                    break
        elif choice == '3':
            while True:
                DoctorManagement.update_appointment_notes()
                again = input("Do you want to update another appointment? (y/n): ").strip().lower()
                if again != 'y':
                    break
        elif choice == '4':
            while True:
                DoctorManagement.create_prescription()
                again = input("Do you want to create another prescription? (y/n): ").strip().lower()
                if again != 'y':
                    break
        elif choice == '5':
            print("Exiting Doctor Management... ✅")
            break
        else:
            print("❌ Invalid choice, try again.")