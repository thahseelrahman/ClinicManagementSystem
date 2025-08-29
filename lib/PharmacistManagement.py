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
        print(f"{'S.No':<5} {'ID':<5} {'Name':<20} {'Generic':<20} {'Manufacturer':<20} {'Price':<10} {'Stock':<6} {'Expiry Date':<12}")
        print("-" * 110)
        for idx, med in enumerate(medicines, start=1):
            print(f"{idx:<5} {med.get_med_id():<5} {med.get_med_name():<20} {med.get_generic_name():<20} "
              f"{med.get_manufacturer():<20} {med.get_unit_rate():<10} {med.get_stock():<6} {med.get_expiry_date()}")
        print("-" * 110)
    @staticmethod
    def add_medicine():
        medicine = Pharmacist()
        while True:
            med_name = input("Enter Medicine Name: ").strip()
            try:
                medicine.set_med_name(med_name)
                break
            except ValueError as e:
                print(f"Error: {e}. Please try again.")


        while True:
            generic_name = input("Enter Generic Name: ").strip()
            try:
                medicine.set_generic_name(generic_name)
                break
            except ValueError as e:
                print(f"Error: {e}. Please try again.")


        while True:
            manufacturer = input("Enter Manufacturer: ").strip()
            try:
                medicine.set_manufacturer(manufacturer)
                break
            except ValueError as e:
                print(f"Error: {e}. Please try again.")


        while True:
            try:
                unit_price = float(input("Enter Unit Price: "))
                if unit_price <= 0:
                    print("Unit price must be greater than 0. Please try again.")
                    continue
                medicine.set_unit_rate(unit_price)
                break
            except ValueError:
                print("Invalid input. Unit price must be a number. Please try again.")

        while True:
            try:
                stock_qty = int(input("Enter Stock Quantity: "))
                if stock_qty < 0:
                    print("Stock quantity cannot be negative. Please try again.")
                    continue
                medicine.set_stock(stock_qty)
                break
            except ValueError:
                print("Invalid input. Stock must be an integer. Please try again.")

  
        while True:
            exp_date = input("Enter Expiry Date (dd/MM/yyyy): ").strip()
            try:
                util_date = datetime.strptime(exp_date, "%d/%m/%Y")
                if util_date.date() <= datetime.today().date():
                    print("Expiry date must be in the future. Please try again.")
                    continue
                medicine.set_expiry_date(util_date.date())
                break
            except ValueError:
                print("Invalid date format. Please use dd/MM/yyyy.")

 
        if PharmacistManagementLib.dao_service.add_medicine(medicine):
            print("Medicine inserted successfully...")
        else:
            print("Something went wrong while inserting medicine.")


    @staticmethod
    def update_medicine():
        try:
            med_id = int(input("Enter Medicine ID: "))
        except ValueError:
            print("Invalid ID. Please enter a valid integer.")
            return

        medicine = PharmacistManagementLib.dao_service.search_medicines(med_id)
        if not medicine:
            print(f"No medicine found with ID {med_id}.")
            return

        while True:
            print("\n====== Update Medicine ======")
            print("1. Update Medicine Name")
            print("2. Update Generic Name")
            print("3. Update Manufacturer")
            print("4. Update Unit Price")
            print("5. Update Stock")
            print("6. Update Expiry Date")
            print("7. Exit")

            try:
                choice = int(input("\nEnter your choice (1-7): "))
            except ValueError:
                print("Invalid choice. Please enter a number between 1 and 7.")
                continue

            if choice == 1:
                while True:
                    new_name = input("Enter new Medicine Name (leave blank to keep current): ").strip()
                    if not new_name:
                        break
                    try:
                        medicine.set_med_name(new_name)
                        break
                    except ValueError as e:
                        print(f"Error: {e}. Please try again.")

            elif choice == 2:
                while True:
                    new_generic = input("Enter new Generic Name (leave blank to keep current): ").strip()
                    if not new_generic:
                        break
                    try:
                        medicine.set_generic_name(new_generic)
                        break
                    except ValueError as e:
                        print(f"Error: {e}. Please try again.")

            elif choice == 3:
                while True:
                    new_manufacturer = input("Enter new Manufacturer (leave blank to keep current): ").strip()
                    if not new_manufacturer:
                        break
                    try:
                        medicine.set_manufacturer(new_manufacturer)
                        break
                    except ValueError as e:
                        print(f"Error: {e}. Please try again.")

            elif choice == 4:
                while True:
                    new_price = input("Enter new Unit Price (leave blank to keep current): ").strip()
                    if not new_price:
                        break
                    try:
                        new_price = float(new_price)
                        if new_price <= 0:
                            print("Unit price must be greater than 0.")
                            continue
                        medicine.set_unit_rate(new_price)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

            elif choice == 5:
                while True:
                    new_stock = input("Enter new Stock (leave blank to keep current): ").strip()
                    if not new_stock:
                        break
                    try:
                        new_stock = int(new_stock)
                        if new_stock < 0:
                            print("Stock cannot be negative.")
                            continue
                        medicine.set_stock(new_stock)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid integer.")

            elif choice == 6:
                while True:
                    exp_date = input("Enter new Expiry Date (dd/MM/yyyy) (leave blank to keep current): ").strip()
                    if not exp_date:
                        break
                    try:
                        util_date = datetime.strptime(exp_date, "%d/%m/%Y")
                        if util_date.date() <= datetime.today().date():
                            print("Expiry date must be in the future.")
                            continue
                        medicine.set_expiry_date(util_date.date())
                        break
                    except ValueError:
                        print("Invalid date format. Please use dd/MM/yyyy.")

            elif choice == 7:
                print("Exiting update menu...")
                break
            else:
                print("Invalid option! Try again.")
                continue

            # Save update
            if PharmacistManagementLib.dao_service.update_medicine(med_id, medicine):
                print("Medicine updated successfully!")
            else:
                print("Something went wrong while updating medicine.")
    @staticmethod
    def delete_medicine():
        try:
            search_id = int(input("Enter Medicine ID to delete: ").strip())
        except ValueError:
            print(" Invalid ID. Please enter a valid integer.")
            return

        medicine = PharmacistManagementLib.dao_service.search_medicines(search_id)
        if not medicine:
            print(f" No medicine found with ID {search_id}.")
            return

  
        print("\n====== Medicine Details ======")
        try:
            print(f"ID: {medicine.get_med_id()}")
            print(f"Name: {medicine.get_med_name()}")
            print(f"Generic: {medicine.get_generic_name()}")
            print(f"Manufacturer: {medicine.get_manufacturer()}")
            print(f"Unit Price: {medicine.get_unit_rate()}")
            print(f"Stock: {medicine.get_stock()}")
            print(f"Expiry Date: {medicine.get_expiry_date()}")
        except Exception as e:
            print(f" Error while displaying medicine details: {e}")


        confirm = input("\nDo you really want to delete this medicine? (y/n): ").strip().lower()
        if confirm == 'y':
            if PharmacistManagementLib.dao_service.delete_medicine(search_id):
                print(" Medicine deleted successfully.")
            else:
                print("❌ Something went wrong while deleting medicine.")
        elif confirm == 'n':
            print("ℹDeletion cancelled by user.")
        else:
            print("❌ Invalid input. Please type 'y' or 'n'.")



    # @staticmethod
    # def delete_medicine():
    #     search_id = int(input("Enter Medicine ID to delete: "))
    #     medicine = PharmacistManagementLib.dao_service.search_medicines(search_id)
    #     if not medicine:
    #         print("Medicine not found")
    #         return
    #     print(medicine)

    #     if input("Do you really want to delete this medicine? (y/n): ").lower() == 'y':
    #         if PharmacistManagementLib.dao_service.delete_medicine(search_id):
    #             print("Medicine deleted successfully...")
    #         else:
    #             print("Something went wrong while deleting medicine.")


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



        try:
            # Prompt for bill type or set default
            bill_type = input("Enter Bill Type (default: PHARMACY): ").strip()
            if not bill_type:
                bill_type = "PHARMACY"

            # Patient ID validation
            patient_id_input = input("Enter Patient ID: ").strip()
            if not patient_id_input.isdigit():
                print("Invalid Patient ID. Setting to 1.")
                patient_id = 1
            else:
                patient_id = int(patient_id_input)

            # Ref ID validation
            ref_id_input = input("Enter Reference ID (optional, press Enter to skip): ").strip()
            if ref_id_input and not ref_id_input.isdigit():
                print("Invalid Reference ID. Setting to None.")
                ref_id = None
            else:
                ref_id = int(ref_id_input) if ref_id_input else None

            # Status validation
            status = input("Enter Bill Status (default: UNPAID): ").strip().upper()
            if not status:
                status = "UNPAID"
            elif status not in ["UNPAID", "PAID"]:
                print("Invalid status. Setting to UNPAID.")
                status = "UNPAID"

            # Bill date
            bill_date = datetime.now()

            bill_obj = Bill()
            bill_obj.set_bill_type(bill_type)
            bill_obj.set_patient_id(patient_id)
            bill_obj.set_ref_id(ref_id)
            bill_obj.items = bill_items
            bill_obj.set_total_amount(total_amount)
            bill_obj.set_status(status)
            bill_obj.set_bill_date(bill_date)

            if BillingManagementLib.dao_service.add_bill(bill_obj):
                print("Bill created successfully.")
                print("---- BILL SUMMARY ----")
                for item in bill_items:
                    print(f"{item['med_name']} | Qty: {item['quantity']} | Unit: {item['unit_price']} | Amount: {item['amount']}")
                print(f"Total Amount: {total_amount}")
            else:
                print("Failed to create bill.")
        except Exception as e:
            print(f"Error creating bill: {e}")
            print("Failed to create bill.")

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
        bills = BillingManagementLib.dao_service.list_bills()
        if not bills:
            print("No bills found.")
            return

        print("------ ALL BILLS ------")
        print(f"{'S.No':<5} {'Bill ID':<8} {'Type':<10} {'Patient ID':<12} {'Ref ID':<8} {'Total':<10} {'Status':<10} {'Date':<20}")
        print("-" * 90)
        for idx, bill in enumerate(bills, start=1):
            print(f"{idx:<5} {bill.get_bill_id():<8} {bill.get_bill_type():<10} {bill.get_patient_id():<12} "
                  f"{bill.get_ref_id():<8} {bill.get_total_amount():<10} {bill.get_status():<10} {bill.get_bill_date()}")
        print("-" * 90)

  
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


    @staticmethod
    def update_bill():
        bill_id = int(input("Enter Bill ID to update: "))
        bill = BillingManagementLib.dao_service.search_bill(bill_id)
        if not bill:
            print("Bill not found.")
            return

        print("Current Bill:")
        for item in bill.get_items():
            print(f"{item['med_name']} | Qty: {item['quantity']} | Unit Price: {item['unit_price']} | Amount: {item['amount']}")

        # allow user to change or add new items
        bill_items = bill.get_items()
        total_amount = bill.get_total_amount()

        while True:
            choice = input("Do you want to (a)dd, (u)pdate qty, (r)emove item, or (f)inish? ").lower()
            if choice == 'f':
                break
            elif choice == 'a':
                med_id = int(input("Enter new Medicine ID: "))
                medicine: Pharmacist = BillingManagementLib.dao_service.search_medicines(med_id)
                if not medicine:
                    print("Medicine not found.")
                    continue
                qty = int(input("Enter quantity: "))
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
            elif choice == 'u':
                med_id = int(input("Enter Medicine ID to update quantity: "))
                for item in bill_items:
                    if item["med_id"] == med_id:
                        new_qty = int(input("Enter new quantity: "))
                        medicine = BillingManagementLib.dao_service.search_medicines(med_id)
                        if not medicine:
                            print("Medicine not found.")
                            continue
                        if new_qty > medicine.get_stock():
                            print("Not enough stock.")
                            continue
                        # adjust stock and amount
                        BillingManagementLib.dao_service.update_stock(med_id, medicine.get_stock() - new_qty)
                        total_amount -= item["amount"]
                        item["quantity"] = new_qty
                        item["amount"] = new_qty * item["unit_price"]
                        total_amount += item["amount"]
                        break
            elif choice == 'r':
                med_id = int(input("Enter Medicine ID to remove: "))
                for item in bill_items:
                    if item["med_id"] == med_id:
                        total_amount -= item["amount"]
                        bill_items.remove(item)
                        break

        bill.set_items(bill_items)
        bill.set_total_amount(total_amount)

        if BillingManagementLib.dao_service.update_Bill(bill, bill_id):
            print("Bill updated successfully.")
        else:
            print("Failed to update bill.")

    @staticmethod
    def delete_bill():
        bill_id = int(input("Enter Bill ID to delete: "))
        bill = BillingManagementLib.dao_service.search_bill(bill_id)
        if not bill:
            print("Bill not found.")
            return

        confirm = input("Are you sure you want to delete this bill? (y/n): ").lower()
        if confirm == 'y':
            if BillingManagementLib.dao_service.delete_Bill(bill_id):
                print("Bill deleted successfully.")
            else:
                print("Something went wrong while deleting bill.")

    @staticmethod
    def pay_bill():
        bill_id = int(input("Enter Bill ID to pay: "))
        bill = BillingManagementLib.dao_service.search_bill(bill_id)
        if not bill:
            print("Bill not found.")
            return

        print(f"Bill Total: {bill.get_total_amount()}")
        confirm = input("Confirm payment? (y/n): ").lower()
        if confirm == 'y':
            if BillingManagementLib.dao_service.pay_Bill(bill_id):
                print("Bill marked as paid.")
            else:
                print("Failed to mark bill as paid.")
