print("💰 Expense Tracker (v7: dictionaries with functions and libraries)")
import json
from datetime import datetime
from pathlib import Path


DATA_FILE = Path("expenses.json")


def load_expenses():
    """Load expenses from disk; return [] if the file doesn't exist."""
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print("⚠️  Couldn't read expenses file — starting fresh.")
            return []


def save_expenses(expenses):
    """Write all expenses to disk as pretty JSON."""
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=2)


def add_expense(expenses):
    """
    Add a new expense to the dictionary
    """
    try:
        amount = float(input("Amount: "))
        if(amount<=0):
            raise ValueError
    except ValueError:
        print("❌ That's not a valid number — try again.")
        return
    category = input("  Category: ")
    expense = {
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d"),
    }
    expenses.append(expense)


def list_expenses(expenses):
    """
    Show all expenses
    """
    print(f"  You have {len(expenses)} expenses:")
    for e in expenses:
        print(f"  {e['date']:<12}{e['category']:<12}€{e['amount']:.2f}")

def show_summary(expenses):
    """
    Show all the money spent by category and the overall total
    """
    tot, totByCat = totByCategory(expenses)
    for cat, amount in totByCat.items():
        print(f" {cat:<12} {amount:.2f}€")
    print(f"{"Total":<12} {tot:.2f}€")

def totByCategory(expenses):
    """
    Calculate all the totals spent by category
    """
    totByCat = {}
    tot = 0
    for e in expenses:
        cat = e["category"]
        totByCat[cat] = totByCat.get(cat, 0) + e["amount"]
        tot += e["amount"]
    return tot, totByCat



def main():
    expenses = load_expenses()
    print(f"Loaded {len(expenses)} expenses")
    menu = """
What would you like to do?
  1) Add an expense
  2) List all expenses
  3) Show summary by category
  4) Save and Quit
"""
    while True:
        print(menu)
        choice = input("Choice: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            save_expenses(expenses)
            print("👋 Goodbye!")
            break
        else:
            print("⚠️  Invalid choice, try again.")


if __name__ == "__main__":
    main()