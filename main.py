

from lib.DoctorManagement import DoctorManagement

def doctor_menu():
    while True:
        print("\n=== Doctor Management Menu ===")
        print("1. Display all Appointments for a Doctor")
        print("2. Find Appointment by ID")
        print("3. Update Appointment Notes")
        print("4. Create Prescription")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            DoctorManagement.display_appointments()
        elif choice == '2':
            DoctorManagement.find_appointment_by_id()
        elif choice == '3':
            DoctorManagement.update_appointment_notes()
        elif choice == '4':
            DoctorManagement.create_prescription()  
            print("Exiting Doctor Management... ✅")
            break
        else:
            print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    doctor_menu()
