print("💰 Expense Tracker (v5.1: dictionaries with functions)")



def add_expense(expenses):
    """
    Add a new expense to the dictionary
    """
    amount = float(input("  Amount: "))
    category = input("  Category: ")
    date = input("  Date (YYYY-MM-DD): ")
    expense = {
        "amount": amount,
        "category": category,
        "date": date,
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
    expenses = []
    menu = """
What would you like to do?
  1) Add an expense
  2) List all expenses
  3) Show summary by category
  4) Quit
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
            print("👋 Goodbye!")
            break
        else:
            print("⚠️  Invalid choice, try again.")


if __name__ == "__main__":
    main()