from dao.PharmacistImple import PharmacistDaoImplementation
from dao.PharmacistAbstract import PharmacistDaoService
from models.pharmacist import Pharmacist, Bill
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

    @staticmethod
    def update_stock():
        search_id = int(input("Enter Medicine ID to update stock: "))
        new_stock = int(input("Enter new stock value: "))

        if PharmacistManagementLib.dao_service.update_stock(search_id, new_stock):
            print("Stock updated successfully...")
        else:
            print("Something went wrong while updating stock.")


class BillingManagementLib:
    """Handles billing operations for pharmacy"""
    dao_service: PharmacistDaoService = PharmacistDaoImplementation()

    @staticmethod
    def add_bill():
        bill_items = []
        total_amount = 0
        while True:
            med_id = int(input("Enter Medicine ID to add to bill (0 to finish): "))
            if med_id == 0:
                break

            medicine: Pharmacist = BillingManagementLib.dao_service.search_medicines(med_id)
            if not medicine:
                print("Medicine not found.")
                continue

            print(f"{medicine.get_med_name()} - Available stock: {medicine.get_stock()} - Unit Price: {medicine.get_unit_rate()}")
            qty = int(input("Enter quantity to purchase: "))
            if qty > medicine.get_stock():
                print("Not enough stock.")
                continue

            BillingManagementLib.dao_service.update_stock(med_id, medicine.get_stock() - qty)
            amount = qty * medicine.get_unit_rate()
            total_amount += amount
            bill_items.append({
                "med_id": med_id,
                "med_name": medicine.get_med_name(),
                "quantity": qty,
                "unit_price": medicine.get_unit_rate(),
                "amount": amount
            })
            print(f"Added {qty} x {medicine.get_med_name()} to bill. Subtotal: {amount}")

        if not bill_items:
            print("No items in the bill.")
            return

        bill_obj = Bill()
        bill_obj.set_items(bill_items)
        bill_obj.set_total_amount(total_amount)
        bill_obj.set_bill_date(datetime.now())

        if BillingManagementLib.dao_service.add_bill(bill_obj):
            print("Bill created successfully.")
            print("---- BILL SUMMARY ----")
            for item in bill_items:
                print(f"{item['med_name']} | Qty: {item['quantity']} | Unit: {item['unit_price']} | Amount: {item['amount']}")
            print(f"Total Amount: {total_amount}")
        else:
            print("Failed to create bill.")

    @staticmethod
    def list_bills():
        bills = BillingManagementLib.dao_service.list_bills()  # must be implemented in DAO
        if not bills:
            print("No bills found.")
            return
        for bill in bills:
            print(f"Bill ID: {bill.get_bill_id()} | Date: {bill.get_bill_date()} | Total Amount: {bill.get_total_amount()}")
            print("Items:")
            for item in bill.get_items():
                print(f"  {item['med_name']} - Qty: {item['quantity']} - Unit Price: {item['unit_price']} - Amount: {item['amount']}")
            print("---------------------------")

    @staticmethod
    def search_bill():
        bill_id = int(input("Enter Bill ID to search: "))
        bill = BillingManagementLib.dao_service.search_bill(bill_id)
        if not bill:
            print("Bill not found.")
            return
        print(f"Bill ID: {bill.get_bill_id()} | Date: {bill.get_bill_date()} | Total Amount: {bill.get_total_amount()}")
        print("Items:")
        for item in bill.get_items():
            print(f"  {item['med_name']} - Qty: {item['quantity']} - Unit Price: {item['unit_price']} - Amount: {item['amount']}")
