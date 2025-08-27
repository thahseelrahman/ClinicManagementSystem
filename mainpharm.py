from lib.PharmacistManagement import PharmacistManagementLib

def main():
    pharm_lib = PharmacistManagementLib()


    while True:
        print("\n====== Pharmacist Management System ======")
        print("1. Add Medicine")
        print("2. List Medicines")
        print("3. Update Medicine")
        print("4. Delete Medicine")
        print("5. Update Stock")
        print("6. Add Bill")
        print("7. List Bills")
        print("8. Search Bill by ID")
        print("9. Update Bill")
        print("10. Delete Bill")
        print("11. Pay Bill")
        print("0. EXIT")
       

        choice = input("Enter your choice: ")

        if choice == "1":
            pharm_lib.add_medicine()
        elif choice == "2":
            pharm_lib.display_all_medicines()
 
        elif choice == "3":
            pharm_lib.update_medicine()
        elif choice == "4":
            pharm_lib.delete_medicine()

        elif choice == "0":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

