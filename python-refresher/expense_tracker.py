print("💰 Expense Tracker")

# Pre-fill some data so we have something to list
expenses = [
    [12.50, "food", "2026-05-10"],
    [45.00, "transport", "2026-05-11"],
    [8.00, "food", "2026-05-12"],
]

menu = """
What would you like to do?
  1) Add an expense
  2) List all expenses
  3) Total spent
  4) Quit
"""

while True:
    print(menu)
    choice = input("Choice: ")

    if choice == "1":
        amount = float(input("  Amount: "))
        category = input("  Category: ")
        date = input("  Date (YYYY-MM-DD): ")
        expenses.append([amount, category, date])
        print(f"  ✅ Added.")

    elif choice == "2":
        print(f"  You have {len(expenses)} expenses:")
        for e in expenses:
            print(f"{e[2]:<12}{e[1]:<12}{e[0]:.2f}")
    
    elif choice == "3":
        tot = 0
        for e in expenses:
            tot += e[0]
        
        print(f"You have spent {tot:.2f}€")

    elif choice == "4":
        print("👋 Goodbye!")
        break

    else:
        print("  ⚠️  Invalid choice, try again.")