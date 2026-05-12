print("💰 Expense Tracker — bulk add")

# A list of expenses; each expense is a list of [amount, category, date]
expenses = []

# Add three hardcoded expenses for now
expenses.append([12.50, "food", "2026-05-10"])
expenses.append([45.00, "transport", "2026-05-11"])
expenses.append([8.00, "food", "2026-05-12"])
expenses.append([100000.00, "sneaky stuff", "13-12-2029"])

print(f"Total expenses recorded: {len(expenses)}")
print(f"First expense: {expenses[0]}")
print(f"Last expense:  {expenses[-1]}")
print(f"All expenses:  {expenses}")

expenses.append([100000.00, "sneaky stuff", "13-12-2029"])
print(f"Second expense: {expenses[1]}")
print(f"Ampount of third expense: {expenses[2][0]}")
print(f"First two expenses: {expenses[:2]}")

