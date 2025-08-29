from lib.PharmacistManagement import PharmacistManagementLib


def pharmamain():
    pharm_lib = PharmacistManagementLib()

    while True:
        print("\n====== Pharmacist Management System ======")
        print("1. Add Medicine")
        print("2. List Medicines")
        print("3. Update Medicine")
        print("4. Delete Medicine")
        # print("5. Add Bill")
        # print("6. List Bills")
        # print("7. Search Bill by ID")
        # print("8. Update Bill")
        # print("9. Delete Bill")
        # print("10. Pay Bill")
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

        # elif choice == "5": 
        #     BillingManagementLib.add_bill()

        # elif choice == "6":
        #     BillingManagementLib.list_bills()
        # elif choice == "7":
        #     BillingManagementLib.search_bill()
        # elif choice == "8":
        #     BillingManagementLib.update_bill()
        # elif choice == "9":
        #     BillingManagementLib.delete_bill()
        # elif choice == "10":
        #     BillingManagementLib.pay_bill()
        

        elif choice == "0":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

