print("================================")
print("       EXPENSE TRACKER")
print("================================")

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: ₹"))

        expenses.append({
            "name": name,
            "amount": amount
        })

        print("Expense added successfully!")

    elif choice == "2":
        print("\n--- Your Expenses ---")

        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            total = 0

            for expense in expenses:
                print(f"{expense['name']} : ₹{expense['amount']}")
                total += expense["amount"]

            print("---------------------")
            print(f"Total: ₹{total}")

    elif choice == "3":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")