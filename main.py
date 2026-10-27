
import json
import os
from datetime import date

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not read saved expenses.")
    return []


expenses = load_expenses()


def add_expense():
    description = input("Enter expense description: ").strip()
    category = input("Enter category (Food/Travel/Bills/Other): ").strip()

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    if not description or not category:
        print("Description and category cannot be empty.")
        return

    expenses.append({
        "description": description,
        "category": category.title(),
        "amount": round(amount, 2),
        "date": date.today().isoformat()
    })

    save_expenses()
    print("Expense added successfully!")


def save_expenses():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- Expense History ---")
    for number, item in enumerate(expenses, start=1):
        print(
            f"{number}. {item['date']} | {item['description']} | "
            f"{item['category']} | Rs. {item['amount']:.2f}"
        )


def show_summary():
    if not expenses:
        print("No expenses available.")
        return

    total = sum(item["amount"] for item in expenses)
    print(f"\nTotal expenses: Rs. {total:.2f}")

    print("\n--- Category Summary ---")
    categories = {}

    for item in expenses:
        category = item["category"]
        categories[category] = categories.get(category, 0) + item["amount"]

    for category, amount in categories.items():
        print(f"{category}: Rs. {amount:.2f}")


def main():
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Choose 1-4.")


if __name__ == "__main__":
    main()
