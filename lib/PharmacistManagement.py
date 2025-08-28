from dao.PharmacistImple import PharmacistDaoImplementation
from dao.PharmacistAbstract import PharmacistDaoService
from models.pharmacist import Pharmacist
from datetime import datetime

class PharmacistManagementLib:
    """Handles CRUD logic for Medicines"""
    dao_service: PharmacistDaoService = PharmacistDaoImplementation()

    @staticmethod
    def display_all_medicines():
        medicines = PharmacistManagementLib.dao_service.display_all_medicines()
        if not medicines:
            print("No medicines found.")
            return
        print("------ ALL MEDICINES ------")
        print(f"{'S.No':<5} {'ID':<5} {'Name':<20} {'Generic':<20} {'Manufacturer':<20} {'Price':<10} {'Stock':<6} {'Expiry Date':<12}")
        print("-" * 110)
        for idx, med in enumerate(medicines, start=1):
            print(f"{idx:<5} {med.get_med_id():<5} {med.get_med_name():<20} {med.get_generic_name():<20} "
              f"{med.get_manufacturer():<20} {med.get_unit_rate():<10} {med.get_stock():<6} {med.get_expiry_date()}")
        print("-" * 110)


    @staticmethod
    def add_medicine():
        medicine = Pharmacist()

        medicine.set_med_name(input("Enter Medicine Name: "))
        medicine.set_generic_name(input("Enter Generic Name: "))
        medicine.set_manufacturer(input("Enter Manufacturer: "))
        medicine.set_unit_rate(float(input("Enter Unit Price: ")))
        medicine.set_stock(int(input("Enter Stock Quantity: ")))

        exp_date = input("Enter Expiry Date (dd/MM/yyyy): ")
        util_date = datetime.strptime(exp_date, "%d/%m/%Y")
        medicine.set_expiry_date(util_date.date())

        if PharmacistManagementLib.dao_service.add_medicine(medicine):
            print("Medicine inserted successfully...")
        else:
            print("Something went wrong while inserting medicine.")

    @staticmethod
    def update_medicine():
        search_id = int(input("Enter Medicine ID to update: "))
        medicine = PharmacistManagementLib.dao_service.search_medicines(search_id)
        if not medicine:
            print("Medicine not found")
            return

        print("Current Medicine Details:")
        print(medicine)
        
        if input("Do you want to edit this medicine? (y/n): ").lower() != 'y':
            return

   
        print("\nWhich field do you want to update?")
        print("1. Medicine Name")
        print("2. Generic Name")
        print("3. Manufacturer")
        print("4. Unit Price")
        print("5. Stock")
        print("6. Expiry Date")
        
        choice = input("Enter your choice (1-6): ")
        updated = False
        if choice == "1":
            new_name = input("Enter new Medicine Name: ")
            updated = PharmacistManagementLib.dao_service.update_single_field(search_id, "name", new_name)
        elif choice == "2":
            new_generic = input("Enter new Generic Name: ")
            updated = PharmacistManagementLib.dao_service.update_single_field(search_id, "generic", new_generic)
            
        elif choice == "3":
            new_manufacturer = input("Enter new Manufacturer: ")
            updated = PharmacistManagementLib.dao_service.update_single_field(search_id, "manufacturer", new_manufacturer)
            
        elif choice == "4":
            new_price = float(input("Enter new Unit Price: "))
            updated = PharmacistManagementLib.dao_service.update_single_field(search_id, "price", new_price)
            
        elif choice == "5":
            new_stock = int(input("Enter new Stock: "))
            updated = PharmacistManagementLib.dao_service.update_single_field(search_id, "stock", new_stock)
            
        elif choice == "6":
            exp_date = input("Enter new Expiry Date (dd/MM/yyyy): ")
            util_date = datetime.strptime(exp_date, "%d/%m/%Y")
            updated = PharmacistManagementLib.dao_service.update_single_field(search_id, "expiry", util_date.date())
            
        else:
            print("Invalid choice!")
            
        if updated:
            print("Medicine updated successfully...")
        else:
            print("Something went wrong while updating medicine.")


    @staticmethod
    def delete_medicine():
        search_id = int(input("Enter Medicine ID to delete: "))
        medicine = PharmacistManagementLib.dao_service.search_medicines(search_id)
        if not medicine:
            print("Medicine not found")
            return
        print(medicine)

        if input("Do you really want to delete this medicine? (y/n): ").lower() == 'y':
            if PharmacistManagementLib.dao_service.delete_medicine(search_id):
                print("Medicine deleted successfully...")
            else:
                print("Something went wrong while deleting medicine.")
  