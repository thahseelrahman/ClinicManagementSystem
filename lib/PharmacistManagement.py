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
        print(f"{'ID':<5} {'Name':<20} {'Generic':<20} {'Manufacturer':<20} {'Price':<10} {'Stock':<6} {'Expiry Date':<12}")
        print("-" * 100)
        for med in medicines:
            print(f"{med.get_med_id():<5} {med.get_med_name():<20} {med.get_generic_name():<20} "
                  f"{med.get_manufacturer():<20} {med.get_unit_rate():<10} {med.get_stock():<6} {med.get_expiry_date()}")
        print("-" * 100)

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
        print(medicine)

        if input("Do you want to edit this medicine? (y/n): ").lower() == 'y':
            medicine.set_med_name(input("Enter new Medicine Name: "))
            medicine.set_generic_name(input("Enter new Generic Name: "))
            medicine.set_manufacturer(input("Enter new Manufacturer: "))
            medicine.set_unit_rate(float(input("Enter new Unit Price: ")))
            medicine.set_stock(int(input("Enter new Stock: ")))

            exp_date = input("Enter new Expiry Date (dd/MM/yyyy): ")
            util_date = datetime.strptime(exp_date, "%d/%m/%Y")
            medicine.set_expiry_date(util_date.date())

            if PharmacistManagementLib.dao_service.update_medicine(medicine, search_id):
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
  
