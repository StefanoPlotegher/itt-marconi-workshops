print("💰 Expense Tracker — add an expense")

amount_str = input("Amount: ")
amount = float(amount_str)

category = input("Category: ").strip()


date = input("Date: ")

print(f"You spent €{amount:.2f} on {category} on the {date}.")