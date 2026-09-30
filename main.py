import json
import os
from datetime import datetime

DATA_FILE = "cafe_data.json"
BILL_FILE = "bills.txt"

# This deafult menu is used when there is no saved menu.
default_menu = {
    1: {"name": "Tea", "price": 15, "stock": 20},
    2: {"name": "Coffee", "price": 30, "stock": 15},
    3: {"name": "Sandwich", "price": 60, "stock": 10},
    4: {"name": "Cake", "price": 40, "stock": 8}
}

sgst_rate = 2.5
cgst_rate = 2.5


def load_menu():
    """Load the menu from a file if one exists."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            saved_menu = json.load(file)

        menu_from_file = {}
        for number in saved_menu:
            menu_from_file[int(number)] = saved_menu[number]
        return menu_from_file

    return default_menu.copy()


menu = load_menu()


def save_menu():
    with open(DATA_FILE, "w") as file:
        json.dump(menu, file, indent=4)


def show_menu():
    print("\n--- CAFE MENU ---")
    for number in menu:
        item = menu[number]
        print(number, "-", item["name"], "| Price: Rs.", item["price"], "| Stock:", item["stock"])


def add_item():
    print("\n--- ADD A MENU ITEM ---")
    name = input("Enter item name: ").strip()

    if name == "":
        print("Item name cannot be empty.")
        return

    price_text = input("Enter item price: ")
    stock_text = input("Enter stock quantity: ")

    if not price_text.isdigit() or not stock_text.isdigit():
        print("Enter whole numbers for price and stock.")
        return

    price = int(price_text)
    stock = int(stock_text)

    if price <= 0 or stock < 0:
        print("Price must be above zero and stock cannot be negative.")
        return

    new_number = max(menu) + 1
    menu[new_number] = {"name": name, "price": price, "stock": stock}
    save_menu()
    print(name, "has been added and saved.")


def update_stock():
    show_menu()
    choice = input("\nEnter the item number to update: ")

    if not choice.isdigit() or int(choice) not in menu:
        print("That item number is not on the menu.")
        return

    item_number = int(choice)
    quantity_text = input("Enter the new stock quantity: ")

    if not quantity_text.isdigit():
        print("Enter a whole number for stock.")
        return

    new_stock = int(quantity_text)
    menu[item_number]["stock"] = new_stock
    save_menu()
    print(menu[item_number]["name"], "stock updated to", new_stock)


def create_bill():
    order = []

    while True:
        show_menu()
        print("G - Generate bill")
        choice = input("Enter an item number or G: ").strip().lower()

        if choice == "g":
            break

        if not choice.isdigit() or int(choice) not in menu:
            print("Choose a valid item number or enter G.")
            continue

        item_number = int(choice)
        item = menu[item_number]
        quantity_text = input("Enter quantity: ")

        if not quantity_text.isdigit() or int(quantity_text) <= 0:
            print("Enter a quantity greater than zero.")
            continue

        quantity = int(quantity_text)

        already_ordered = 0
        for ordered_item in order:
            if ordered_item["item_number"] == item_number:
                already_ordered = already_ordered + ordered_item["quantity"]

        available_stock = item["stock"] - already_ordered
        if quantity > available_stock:
            print("Sorry, only", available_stock, "more are available.")
            continue

        order_item = {
            "item_number": item_number,
            "name": item["name"],
            "price": item["price"],
            "quantity": quantity
        }
        order.append(order_item)
        print(quantity, item["name"], "added to the order.")

    if len(order) == 0:
        print("No items were ordered. No bill was created.")
        return

    # Calculate each item's total and the bill subtotal.
    subtotal = 0
    for item in order:
        item["total"] = item["price"] * item["quantity"]
        subtotal = subtotal + item["total"]

    sgst = subtotal * sgst_rate / 100
    cgst = subtotal * cgst_rate / 100
    grand_total = subtotal + sgst + cgst

    bill_number = datetime.now().strftime("B%Y%m%d%H%M%S")
    bill_date = datetime.now().strftime("%d-%m-%Y %H:%M")

    print("\n========== CAFE BILL ==========")
    print("Bill number:", bill_number)
    print("Date:", bill_date)
    print("--------------------------------")

    for item in order:
        print(item["name"], "x", item["quantity"], "= Rs.", item["total"])

    print("--------------------------------")
    print("Subtotal: Rs.", round(subtotal, 2))
    print("SGST:", sgst_rate, "% = Rs.", round(sgst, 2))
    print("CGST:", cgst_rate, "% = Rs.", round(cgst, 2))
    print("Grand total: Rs.", round(grand_total, 2))
    print("================================")

    # Remove sold item's stock and update the deafult menu
    for item in order:
        item_number = item["item_number"]
        menu[item_number]["stock"] = menu[item_number]["stock"] - item["quantity"]
    save_menu()

    # Add this bill to the bills file.
    with open(BILL_FILE, "a") as file:
        file.write("Bill number: " + bill_number + "\n")
        file.write("Date: " + bill_date + "\n")

        for item in order:
            file.write(item["name"] + " x " + str(item["quantity"]))
            file.write(" = Rs. " + str(item["total"]) + "\n")

        file.write("Subtotal: Rs. " + str(round(subtotal, 2)) + "\n")
        file.write("SGST: Rs. " + str(round(sgst, 2)) + "\n")
        file.write("CGST: Rs. " + str(round(cgst, 2)) + "\n")
        file.write("Grand total: Rs. " + str(round(grand_total, 2)) + "\n")
        file.write("------------------------------\n")

    print("Bill saved in system")
    print("Updated stock saved in menu")


def show_saved_bill():
    wanted_number = input("Enter bill number: ").strip()

    try:
        with open(BILL_FILE, "r") as file:
            all_bills = file.read()
    except FileNotFoundError:
        print("No bills have been saved yet.")
        return

    saved_bills = all_bills.split("------------------------------")
    for bill in saved_bills:
        if "Bill number: " + wanted_number in bill:
            print("\n--- BILL FOUND ---")
            print(bill)
            return

    print("No bill found with that number.")


#These are the option program repeatdely ask until user entered G.
while True:
    print("\n--- CAFE BILLING SYSTEM ---")
    print("1. Create a new bill")
    print("2. Search for a bill")
    print("3. Add a menu item")
    print("4. Show menu")
    print("5. Update stock")
    print("6. Exit")

    option = input("Choose an option: ").strip()

    if option == "1":
        create_bill()
    elif option == "2":
        show_saved_bill()
    elif option == "3":
        add_item()
    elif option == "4":
        show_menu()
    elif option == "5":
        update_stock()
    elif option == "6":
        print("Thank you!")
        break
    else:
        print("Choose a number from 1 to 6.")
