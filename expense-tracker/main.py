import csv
from datetime import date
from collections import defaultdict

FILE_NAME = "expenses.csv"


def add_expense():
    expense_date = date.today().isoformat()
    name = input("Enter expense name: ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: ₹"))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow(["Date", "Name", "Category", "Amount"])

        writer.writerow([expense_date, name, category, amount])

    print("Expense added successfully!")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)
            expenses = list(reader)

        if not expenses:
            print("No expenses recorded.")
            return

        print("\n--- Your Expenses ---")

        total = 0

        for expense in expenses:
            print(
                f"{expense['Date']} | "
                f"{expense['Name']} | "
                f"{expense['Category']} | "
                f"₹{expense['Amount']}"
            )

            total += float(expense["Amount"])

        print("----------------------------")
        print(f"Total Expenses: ₹{total:.2f}")

    except FileNotFoundError:
        print("No expenses recorded yet.")


def category_summary():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)
            expenses = list(reader)

        if not expenses:
            print("No expenses recorded.")
            return

        categories = defaultdict(float)

        for expense in expenses:
            categories[expense["Category"]] += float(expense["Amount"])

        print("\n--- Category Summary ---")

        for category, amount in categories.items():
            print(f"{category}: ₹{amount:.2f}")

    except FileNotFoundError:
        print("No expenses recorded yet.")


while True:
    print("\n==============================")
    print("       EXPENSE TRACKER")
    print("==============================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Category Summary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        category_summary()

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")