
import json
import os
from datetime import date

FILE_NAME = "expenses.json"


def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return {"budget": 0, "expenses": []}


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_expense(data):
    print("\n--- Add New Expense ---")

    name = input("Enter expense name: ")
    category = input("Enter category: ")

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    expense = {
        "name": name,
        "category": category,
        "amount": amount,
        "date": str(date.today())
    }

    data["expenses"].append(expense)
    save_data(data)

    print("Expense added successfully!")


def view_expenses(data):
    print("\n--- All Expenses ---")

    if not data["expenses"]:
        print("No expenses recorded yet.")
        return

    for i, expense in enumerate(data["expenses"], start=1):
        print(f"\nExpense {i}")
        print("Name:", expense["name"])
        print("Category:", expense["category"])
        print("Amount: Rs.", expense["amount"])
        print("Date:", expense["date"])


def show_total(data):
    total = sum(
        expense["amount"] for expense in data["expenses"]
    )

    print("\nTotal Expenses: Rs.", round(total, 2))


def set_budget(data):
    try:
        budget = float(input("\nEnter your total budget: "))

        if budget < 0:
            print("Budget cannot be negative.")
            return

        data["budget"] = budget
        save_data(data)

        print("Budget saved successfully!")

    except ValueError:
        print("Please enter a valid amount.")


def show_balance(data):
    total = sum(
        expense["amount"] for expense in data["expenses"]
    )

    remaining = data["budget"] - total

    print("\n--- Budget Summary ---")
    print("Total Budget: Rs.", round(data["budget"], 2))
    print("Total Expenses: Rs.", round(total, 2))
    print("Remaining Balance: Rs.", round(remaining, 2))


def main():
    data = load_data()

    while True:
        print("\n===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. Set Budget")
        print("5. View Remaining Balance")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            add_expense(data)

        elif choice == "2":
            view_expenses(data)

        elif choice == "3":
            show_total(data)

        elif choice == "4":
            set_budget(data)

        elif choice == "5":
            show_balance(data)

        elif choice == "6":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
