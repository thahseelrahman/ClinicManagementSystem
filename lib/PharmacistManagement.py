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
