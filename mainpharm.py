from lib.PharmacistManagement import PharmacistManagementLib

def pharmamain():
    pharm_lib = PharmacistManagementLib()

    while True:
        print("\n====== Pharmacist Management System ======")
        print("1. Add Medicine")
        print("2. List Medicines")
        print("3. Search Medicine by ID")
        print("4. Update Medicine")
        print("5. Delete Medicine")
        print("6. Update Stock")
        print("7. Add Bill")
        print("8. List Bills")
        print("9. Search Bill by ID")
        print("10. Update Bill")
        print("0. EXIT")
       

        choice = input("Enter your choice: ")

        if choice == "1":
            pharm_lib.add_medicine()
        elif choice == "2":
            pharm_lib.display_all_medicines()
        # elif choice == "3":
        #     pharm_lib.search_medicines()  
        # elif choice == "4":
        #     pharm_lib.update_medicine()
        # elif choice == "5":
        #     pharm_lib.delete_medicine()
        # elif choice == "6":
        #     pharm_lib.update_stock()
        # elif choice == "7":
        #     bill_lib.add_bill()
        # elif choice == "8":
        #     bill_lib.list_bills()
        # elif choice == "9":
        #     bill_lib.search_bill()
        # elif choice == "10":
        #     bill_lib.update_bill()
        elif choice == "0":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

