# === Scalar types — one value each ===
amount = 12.50          # float
category = "food"       # str
date = "2026-05-12"     # str
is_recurring = False    # bool
notes = None            # NoneType

print(amount, category, date, is_recurring, notes)
print(type(amount), type(category), type(is_recurring), type(notes))

# === Collection types — many values ===
# A list: ordered and mutable. The natural "array" of Python.
tags = ["lunch", "weekday", "card-payment"]
print("First tag:", tags[0])
tags.append("urgent")
print("After append:", tags)

# A tuple: ordered but immutable — use it for fixed records.
expense_record = (12.50, "food", "2026-05-12")
print("Tuple:", expense_record)
print("Amount from tuple:", expense_record[0])

# A set: unordered and unique — duplicates disappear automatically.
unique_categories = {"food", "transport", "food", "rent", "food"}
print("Unique categories:", unique_categories)