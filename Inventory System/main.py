"""
📦 Inventory Management System (CSV-Based)
Author: Uzair (SwatStormer)
Description:
A simple Python program to manage product inventory using CSV files.
Allows viewing, adding, searching, and calculating total inventory value.
"""

import csv
import os  # To check if file exists

# --- Constants ---
FILE_NAME = "inventory.csv"  # Name of the CSV file storing inventory
FIELDNAMES = ["Product", "Price", "Quantity"]  # Columns in the CSV file


# --- Function: View All Products ---
def view_all_products():
    """
    Reads the CSV file and displays all products with price and quantity.
    """
    try:
        with open(FILE_NAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            print("\n--- Product List ---")
            for row in reader:
                print(f"{row['Product']} costs ${row['Price']} and {row['Quantity']} items are in stock.")
    except FileNotFoundError:
        print("Inventory file not found.")


# --- Function: Add a New Product ---
def add_product():
    """
    Prompts user for product details and appends it to the CSV file.
    Creates the file with header if it doesn't exist.
    """
    name = input("Enter product name: ")
    try:
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
    except ValueError:
        print("Invalid input. Price must be a number, quantity must be an integer.")
        return

    new_product = {"Product": name, "Price": f"{price}", "Quantity": f"{quantity}"}

    # Check if file exists or is empty (to write header)
    file_exists = os.path.isfile(FILE_NAME)
    write_header = not file_exists or os.stat(FILE_NAME).st_size == 0

    # Append new product
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        if write_header:
            writer.writeheader()
        writer.writerow(new_product)

    print("✅ Product added successfully.")


# --- Function: Search for a Product by Name ---
def search_product():
    """
    Prompts user for a product name and searches it in the CSV file.
    Displays product details if found.
    """
    search = input("Enter product name to search: ").lower()
    found = False
    try:
        with open(FILE_NAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Product'].lower() == search:
                    print(f"{row['Product']} costs ${row['Price']} and {row['Quantity']} in stock.")
                    found = True
                    break
        if not found:
            print("⚠️ Product not found.")
    except FileNotFoundError:
        print("Inventory file not found.")


# --- Function: Calculate Total Inventory Value ---
def calculate_inventory_value():
    """
    Reads all products and calculates total inventory value: Price × Quantity for each item.
    """
    total_value = 0
    try:
        with open(FILE_NAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    price = float(row['Price'])
                    quantity = int(row['Quantity'])
                    total_value += price * quantity
                except ValueError:
                    # Skip invalid rows
                    continue
        print(f"💰 Total inventory value: ${total_value:.2f}")
    except FileNotFoundError:
        print("Inventory file not found.")


# --- Main Menu Loop ---
while True:
    print("\n📋 Menu:")
    print("1. View All Products")
    print("2. Add New Product")
    print("3. Search Product by Name")
    print("4. Calculate Total Inventory Value")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        view_all_products()
    elif choice == '2':
        add_product()
    elif choice == '3':
        search_product()
    elif choice == '4':
        calculate_inventory_value()
    elif choice == '5':
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please enter a number between 1 and 5.")
