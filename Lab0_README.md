# Python Refresher — Build Your First Real App

### Hands-on Workshop · Eleventh Training

> **Level:** Beginner / refresher &nbsp;·&nbsp; **Duration:** 2 hours (core) / 2h 30min (full) &nbsp;·&nbsp; **Language:** English &nbsp;·&nbsp; **Format:** Code-along

---

## What you'll build

You'll build a **Personal Expense Tracker** — a small command-line application in pure Python that lets you:

- Add expenses (amount, category, date)
- List them in a nice table
- See a summary grouped by category
- Save them to a file so they survive when you quit

We'll build it **incrementally**, one Python concept at a time.
At every task you'll add a new feature using a new piece of Python — the program grows in your hands as your knowledge grows.

By the end of the 2 hours, you'll have a fully working CLI app and a refreshed grip on:

- Running Python scripts and using `print` / `input`
- Variables, numbers, strings, booleans
- Lists and dictionaries
- `if` / `for` / `while`
- Functions
- Modules from the standard library (`json`, `datetime`, `pathlib`)
- Reading and writing files
- Basic error handling with `try` / `except`

---

## Setup before we start (10 min)

You need:

- **Python 3.10 or newer** installed locally
 Check with: `python3 --version`
 If missing, install from [python.org/downloads](https://www.python.org/downloads/) or use [Anaconda](https://www.anaconda.com/download).
- **A text editor** — VS Code is recommended ([code.visualstudio.com](https://code.visualstudio.com/)) with the Python extension. Any editor works.
- **A terminal** — Terminal on macOS/Linux, PowerShell or Windows Terminal on Windows.

### Create a workshop folder

```bash
mkdir python-refresher
cd python-refresher
code . # opens VS Code in the current folder (optional)
```

### Create a virtual environment

A **virtual environment** (or *venv*) is an isolated copy of Python that lives inside your project folder. It lets each project have its own libraries at their own versions, without polluting your system Python. It's the universal first step of any serious Python project — get used to creating one every time.

```bash
# Create the venv (folder named .venv inside your project)
python3 -m venv .venv

# Activate it
# macOS / Linux:
source .venv/bin/activate
# Windows PowerShell:
.venv\Scripts\Activate.ps1
```

Once active, your prompt should change to something like `(.venv) $`.
Check you're using the right Python:

```bash
which python # macOS/Linux — should point inside .venv
where python # Windows
python --version # should be 3.10+
```

To leave the venv when you're done: `deactivate`.

### Declare your dependencies in `requirements.txt`

A `requirements.txt` file is the **shopping list** for `pip`. It pins every external library your project needs, so anyone (including future-you on another machine) can recreate the environment in one command.

For this workshop we only use the standard library — so the file is **empty for now**. Create it anyway:

```bash
# macOS/Linux
touch requirements.txt
# Windows
type nul > requirements.txt
```

Even though it's empty, you'll learn the workflow. The day you `import requests` or `import pandas`, here's what you'd do:

```bash
# Install a library inside the venv (NOT globally)
pip install requests

# Freeze everything you installed into the requirements file
pip freeze > requirements.txt
```

Anyone else who clones your project then runs:

```bash
python3 -m venv .venv
source .venv/bin/activate # or .venv\Scripts\Activate.ps1 on Windows
pip install -r requirements.txt
```

…and they have an identical environment in seconds.

> **No internet?** No problem. We use only the Python standard library throughout this workshop — `requirements.txt` will stay empty, but the *habit* of creating it is what matters.

> **Common pitfall:** if you forget to activate the venv, `pip install` will install **globally**, polluting your system Python. Always check the prompt shows `(.venv)` before running `pip`.

> **References used in this workshop:**
> [The Python Tutorial](https://docs.python.org/3/tutorial/) ·
> [Python Standard Library](https://docs.python.org/3/library/) ·
> [venv module](https://docs.python.org/3/library/venv.html) ·
> [pip user guide](https://pip.pypa.io/en/stable/user_guide/) ·
> [Real Python tutorials](https://realpython.com/) ·
> [PEP 8 style guide](https://peps.python.org/pep-0008/)

---

## Workshop tasks

| # | Title | Concept introduced | Time |
|----|----------------------------------------------|----------------------------------|-------|
| 0 | Hello, Python | Running a script, `print` | 10 min |
| 1 | Storing a single expense | Data types and collections | 15 min |
| 2 | Talking to the user | `input`, strings, f-strings | 15 min |
| 3 | Tracking many expenses | Lists | 15 min |
| 4 | A menu that keeps running | `while`, `if`, `for` | 20 min |
| 5 | Expenses with structure | Dictionaries | 15 min |
| 6 | Clean code: functions | Functions, parameters, returns | 20 min |
| 7 | Save and load with JSON | Modules and file I/O | 15 min |
| 8 | The `json` library in depth | `dumps`/`loads`, external JSON | 15 min |
| 9 | Bonus — Handle the unexpected | `try` / `except` | optional |

> **Tip:** every task includes the **starter code** to paste, the **task** to complete, a **checkpoint** to confirm it works, and a **key takeaway**.
> If you fall behind, just open the next task's starter and keep going — every task is self-contained.

> **Time budget:** the tasks above sum to ~2h 30min including a 10-min setup. If you're tight on the original 2 hours, Task 8 and Task 9 are optional — Tasks 0-7 alone form a complete working program.

---

# Task 0 — Hello, Python 10 min

## Concept

A Python program is just a text file with the `.py` extension.
You run it from the terminal with `python3`.

## Starter code

Create a file called `expense_tracker.py` with **this single line**:

```python
print(" Expense Tracker v0 — hello!")
```

## Your task

1. Save the file.
2. Open your terminal in the workshop folder.
3. Run: `python3 expense_tracker.py`
4. Add a second `print` call below the first that prints your name.
5. Run again.

## Checkpoint

You should see something like:

```
 Expense Tracker v0 — hello!
My name is Paolo
```

If you get `command not found: python3`, try `python` instead (on Windows) or check that Python is on your PATH.

## Key takeaway

- A `.py` file is a script. Lines are executed top to bottom.
- `print(...)` is the simplest way to show output.
- Strings can be wrapped in single `'...'` or double `"..."` quotes — pick one and stick with it.

 [print() docs](https://docs.python.org/3/library/functions.html#print) · [Running Python](https://docs.python.org/3/tutorial/interpreter.html)

---

# Task 1 — Storing a single expense 15 min

## Concept

Python has two families of built-in types you need to know cold.

### Scalar (primitive) types — hold one value

| Type | Example | What it represents |
|---------|------------------|--------------------------|
| `int` | `42` | Whole numbers |
| `float` | `12.50` | Decimal numbers |
| `str` | `"food"` | Text |
| `bool` | `True`, `False` | Yes/no values |
| `None` | `None` | "Nothing here" |

### Collection types — hold many values

| Type | Example | Key property |
|---------|------------------------------------------|---------------------------------|
| `list` | `[1, 2, 3]` | Ordered, **mutable**, duplicates OK |
| `tuple` | `(1, 2, 3)` | Ordered, **immutable**, duplicates OK |
| `set` | `{1, 2, 3}` | Unordered, mutable, **unique** values |
| `dict` | `{"name": "Paolo", "age": 40}` | Key → value mapping (Task 5) |

> **Pythonic note:** there's no separate "array" type for general use — `list` *is* Python's array. (A specialized `array.array` module exists for tight numeric arrays, and `numpy.array` for scientific computing, but for everyday code you reach for `list`.)

Variables are created by assignment: `name = value`. You **don't declare types** — Python figures them out at runtime.

## Starter code

Replace your current code with:

```python
# === Scalar types — one value each ===
amount = 12.50 # float
category = "food" # str
date = "2026-05-12" # str
is_recurring = False # bool
notes = None # NoneType

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
```

## Your task

1. Run the script and observe the output of each section.
2. Try `tags[0] = "dinner"` — does it work? It should: lists are mutable.
3. Now try `expense_record[0] = 99.99` — what error do you get? **Tuples are immutable**: once built, you can't change them.
4. Add a string `"food"` again to `unique_categories` with `unique_categories.add("food")`. Print the set. How many items?
5. Add `len(...)` calls to print the length of `tags`, `expense_record`, and `unique_categories`.
6. **Bonus:** create a tuple with **a single element** — try `(5)` and then `(5,)`. Use `type()` to see the difference. (This is a classic Python gotcha.)

## Checkpoint

```
12.5 food 2026-05-12 False None
<class 'float'> <class 'str'> <class 'bool'> <class 'NoneType'>
First tag: lunch
After append: ['lunch', 'weekday', 'card-payment', 'urgent']
Tuple: (12.5, 'food', '2026-05-12')
Amount from tuple: 12.5
Unique categories: {'food', 'transport', 'rent'} # order may vary
```

When you try `expense_record[0] = 99.99` you should see:
```
TypeError: 'tuple' object does not support item assignment
```

## Key takeaway

- Python is **dynamically typed**: a variable's type comes from the value you assign to it.
- **Scalar types** hold one value; **collection types** hold many.
- Choose your collection by **intent**:
 - `list` → an ordered sequence you'll grow/change → 90% of cases.
 - `tuple` → a small fixed record (a returned pair, a coordinate, a config row).
 - `set` → uniqueness or membership tests (`"food" in cats`) — extremely fast.
 - `dict` → a record with named fields → coming in Task 5.
- Use `type(x)` and `len(x)` while learning; both are your best friends.

 [Built-in types](https://docs.python.org/3/library/stdtypes.html) ·
[Data structures tutorial](https://docs.python.org/3/tutorial/datastructures.html) ·
[Variables in Python (Real Python)](https://realpython.com/python-variables/) ·
[Sets in Python](https://docs.python.org/3/tutorial/datastructures.html#sets)

---

# Task 2 — Talking to the user 15 min

## Concept

Two essentials of any CLI app:

- **`input(prompt)`** — reads a line of text the user types and returns it as a `str`.
- **f-strings** — the modern, readable way to format strings: `f"Hello, {name}!"`.

 `input()` always returns a **string**. If you want a number, convert it with `float(...)` or `int(...)`.

## Starter code

Replace your code with:

```python
print(" Expense Tracker — add an expense")

amount_str = input("Amount: ")
amount = float(amount_str)

category = input("Category: ")

print(f"You spent €{amount:.2f} on {category}.")
```

## Your task

1. Run the script and add an expense (try `12.50` and `food`).
2. Notice the `{amount:.2f}` syntax — this forces **2 decimal digits**. Try changing it to `:.0f` or `:.4f` and re-run.
3. Add a prompt for `date` and include it in the final message.
4. Add a confirmation line at the bottom:
 ```
 Recorded: €12.50 — food — 2026-05-12
 ```
5. **Bonus:** strip whitespace from `category` with `.strip()` (try typing ` food ` with spaces — what happens before and after `.strip()`?).

## Checkpoint

Example session:

```
 Expense Tracker — add an expense
Amount: 12.50
Category: food
Date: 2026-05-12
Recorded: €12.50 — food — 2026-05-12
```

## Key takeaway

- `input()` reads strings; **convert** with `float()` / `int()` when you need numbers.
- f-strings let you embed expressions and **format numbers** (e.g. `:.2f`) directly inside the string.
- String methods like `.strip()`, `.upper()`, `.lower()` are how you clean user input.

 [Input and Output](https://docs.python.org/3/tutorial/inputoutput.html) · [f-string mini-language](https://docs.python.org/3/library/string.html#formatspec) · [String methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

---

# Task 3 — Tracking many expenses 15 min

## Concept

One expense is boring. We need a collection.

A **list** is an ordered, mutable sequence:

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("date") # add at end
fruits[0] # "apple" — indexing starts at 0
len(fruits) # 4
```

For now, we'll store each expense as a simple **3-tuple-like list**: `[amount, category, date]`.
(We'll upgrade to dictionaries in Task 5 — for now, lists are enough.)

## Starter code

```python
print(" Expense Tracker — bulk add")

# A list of expenses; each expense is a list of [amount, category, date]
expenses = []

# Add three hardcoded expenses for now
expenses.append([12.50, "food", "2026-05-10"])
expenses.append([45.00, "transport", "2026-05-11"])
expenses.append([8.00, "food", "2026-05-12"])

print(f"Total expenses recorded: {len(expenses)}")
print(f"First expense: {expenses[0]}")
print(f"Last expense: {expenses[-1]}")
print(f"All expenses: {expenses}")
```

## Your task

1. Run the script and observe the output.
2. Add a fourth expense to the list using `.append(...)`.
3. Print the **second** expense using its index.
4. Print the **amount** of the third expense (hint: nested indexing — `expenses[2][0]`).
5. **Bonus:** use **slicing** to print the **first two** expenses with `expenses[:2]`.

## Checkpoint

```
Total expenses recorded: 4
First expense: [12.5, 'food', '2026-05-10']
Last expense: [<your fourth expense>]
```

## Key takeaway

- A **list** holds many items, in order. Index with `[i]`; negative indices count from the end.
- `.append(x)` adds to the end. `len(...)` gives the count.
- Lists can hold **anything** — including other lists.

 [Lists tutorial](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) · [Sequence operations](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)

---

# Task 4 — A menu that keeps running 20 min

## Concept

Real CLI apps don't run once and quit — they show a menu and **keep looping until the user wants to quit**.

Three control-flow tools:

- **`if` / `elif` / `else`** — branch on a condition
- **`while`** — repeat as long as a condition is true
- **`for`** — iterate over a collection

## Starter code

Replace your script with this. It's bigger — read it carefully before running.

```python
print(" Expense Tracker")

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
 3) Quit
"""

while True:
 print(menu)
 choice = input("Choice: ")

 if choice == "1":
 amount = float(input(" Amount: "))
 category = input(" Category: ")
 date = input(" Date (YYYY-MM-DD): ")
 expenses.append([amount, category, date])
 print(f" Added.")

 elif choice == "2":
 print(f" You have {len(expenses)} expenses:")
 for expense in expenses:
 print(f" - {expense}")

 elif choice == "3":
 print(" Goodbye!")
 break

 else:
 print(" Invalid choice, try again.")
```

## Your task

1. Run the script. Try options 1, 2, and 3 in different orders.
2. Add a **fourth menu option** `4) Show total` that uses a `for` loop to sum the `amount` of every expense and prints it.

 Hint — the loop you need:

```python
total = 0
for expense in expenses:
 total = total + expense[0] # amount is at index 0
print(f"Total spent: €{total:.2f}")
```

3. Improve the listing in option 2 to print one expense per line in a nice format:

 ```
 2026-05-10 food €12.50
 ```

 You'll need an f-string with field widths like `f"{date:<12}{category:<12}€{amount:.2f}"`.
4. **Bonus:** what does the `else` branch do if the user types nothing and just presses Enter? Try it.

## Checkpoint

A full session should look like:

```
 Expense Tracker

What would you like to do?
 1) Add an expense
 2) List all expenses
 3) Show total
 4) Quit

Choice: 3
Total spent: €65.50
```

## Key takeaway

- `while True:` + `break` is the standard pattern for "loop until told to stop".
- `for item in collection:` reads every element, in order.
- `if` / `elif` / `else` branches — and **comparison uses `==`** (a single `=` is assignment).
- Indentation matters: every block is defined by indentation, not braces.

 [Control flow](https://docs.python.org/3/tutorial/controlflow.html) · [Boolean operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)

---

# Task 5 — Expenses with structure 15 min

## Concept

Using `expense[0]` for "amount" is fragile — what if you add a field? You'd have to renumber everything.

A **dictionary** maps named keys to values:

```python
expense = {
 "amount": 12.50,
 "category": "food",
 "date": "2026-05-10",
}

expense["amount"] # 12.5
expense["notes"] = "Lunch" # add a new key
list(expense.keys()) # ['amount', 'category', 'date', 'notes']
```

Dictionaries make code **self-documenting**: `expense["amount"]` is obvious; `expense[0]` is not.

## Starter code

Refactor your `expenses` list to use dictionaries:

```python
print(" Expense Tracker (v5: dictionaries)")

expenses = [
 {"amount": 12.50, "category": "food", "date": "2026-05-10"},
 {"amount": 45.00, "category": "transport", "date": "2026-05-11"},
 {"amount": 8.00, "category": "food", "date": "2026-05-12"},
]

# Print every expense by its named fields
for e in expenses:
 print(f" {e['date']:<12}{e['category']:<12}€{e['amount']:.2f}")
```

## Your task

1. Adapt your **menu code from Task 4** to build dictionaries in option 1, like this:

```python
expense = {
 "amount": amount,
 "category": category,
 "date": date,
}
expenses.append(expense)
```

2. Adapt the **total** calculation to use `e["amount"]` instead of `e[0]`.
3. Adapt the **listing** to use named keys (`e["date"]`, `e["category"]`, `e["amount"]`).
4. Add a new menu option `4) Summary by category`. For each category, print the total spent.

 Hint — the totals pattern:

```python
totals = {}
for e in expenses:
 cat = e["category"]
 totals[cat] = totals.get(cat, 0) + e["amount"]

for cat, amount in totals.items():
 print(f" {cat:<12} €{amount:.2f}")
```

## Checkpoint

The "Summary by category" should look like:

```
 food €20.50
 transport €45.00
```

## Key takeaway

- A **dict** is `{key: value}`. Access with `dict[key]` or the safer `dict.get(key, default)`.
- `.items()` gives `(key, value)` pairs for iteration.
- Dictionaries are the natural representation of a "record" / "object" in Python — you'll see them everywhere (JSON, configs, API responses).

 [Dictionaries tutorial](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) · [dict methods](https://docs.python.org/3/library/stdtypes.html#dict)

---

# Task 6 — Clean code: functions 20 min

## Concept

Your script is getting big. **Functions** let you give a name to a piece of logic and reuse it.

```python
def greet(name):
 """Return a friendly greeting."""
 return f"Hello, {name}!"

message = greet("World")
print(message)
```

Why use functions?

- **Reuse:** write once, call many times.
- **Naming:** `add_expense(...)` is clearer than 12 lines of input/append.
- **Testability:** a function is something you can verify in isolation.
- **Readability:** `main` becomes a clean list of high-level steps.

## Starter code

This is a **refactored skeleton** of the program. Your job is to fill in the functions using logic you already wrote in tasks 4 and 5.

```python
def add_expense(expenses):
 """Prompt the user for one expense and append it to the list."""
 # TODO: ask for amount, category, date; build a dict; append it.
 pass


def list_expenses(expenses):
 """Print all expenses in a formatted table."""
 # TODO: loop and print each expense like in task 5.
 pass


def show_summary(expenses):
 """Print total spent per category, plus an overall total."""
 # TODO: build a totals dict, then print it.
 pass


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
 print(" Goodbye!")
 break
 else:
 print(" Invalid choice, try again.")


if __name__ == "__main__":
 main()
```

## Your task

1. **Fill in `add_expense`** using your code from Task 5 (input + build dict + append).
2. **Fill in `list_expenses`** using your formatted print from Task 5.
3. **Fill in `show_summary`** using your category totals from Task 5. Add an **overall total** line at the bottom.
4. Run the program end-to-end.
5. **Bonus:** add a `def total_by_category(expenses) -> dict:` helper function that **returns** the totals dictionary (no printing), and have `show_summary` call it. Notice how separating "compute" from "display" makes both pieces simpler.

## Checkpoint

A clean run should look like:

```
What would you like to do?
 1) Add an expense
 2) List all expenses
 3) Show summary by category
 4) Quit

Choice: 3
 food €20.50
 transport €45.00
 TOTAL €65.50
```

## Key takeaway

- `def name(args):` defines a function; `return value` sends a result back.
- Functions that take a **list** (or dict) modify the same object in memory — caller sees the changes. No need to return.
- `if __name__ == "__main__":` is Python's idiom for "only run `main()` when this file is executed directly", not when it's imported.
- A good function does **one thing**, has a clear name, and ideally a docstring.

 [Defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) · [Type hints](https://docs.python.org/3/library/typing.html) · [Real Python: defining functions](https://realpython.com/defining-your-own-python-function/)

---

# Task 7 — Save and load with JSON 15 min

## Concept

Right now your expenses vanish when you quit. Let's fix that using two **standard library modules**:

- **`json`** — read and write Python data structures as JSON text
- **`pathlib`** — modern way to work with file paths
- **`datetime`** — handle dates properly (no more typing them by hand)

A **module** is just another `.py` file that exposes functions. You bring it in with `import`.

```python
import json
from datetime import datetime
from pathlib import Path
```

## Starter code

Add these helpers to the top of your script (above your other functions):

```python
import json
from datetime import datetime
from pathlib import Path


DATA_FILE = Path("expenses.json")


def load_expenses():
 """Load expenses from disk; return [] if the file doesn't exist."""
 if not DATA_FILE.exists():
 return []
 with DATA_FILE.open("r", encoding="utf-8") as f:
 return json.load(f)


def save_expenses(expenses):
 """Write all expenses to disk as pretty JSON."""
 with DATA_FILE.open("w", encoding="utf-8") as f:
 json.dump(expenses, f, indent=2)
```

## Your task

1. In `main()`, replace `expenses = []` with `expenses = load_expenses()`.
 Print something like `"Loaded N expenses"` so the user sees the count.
2. Change menu option `4` from `Quit` to `Save and quit`, and call `save_expenses(expenses)` before breaking.
3. In `add_expense`, **stop asking** for the date manually — use `datetime` to fill it in automatically. Replace the `"date": date,` line in your expense dict with:

```python
"date": datetime.now().strftime("%Y-%m-%d"),
```
4. **Run the program**, add a couple of expenses, choose "Save and quit".
5. **Open `expenses.json`** in your editor — see how your data is stored.
6. **Run the program again** — your previous expenses should reload automatically.

## Checkpoint

Two consecutive runs should look like:

```
$ python3 expense_tracker.py
 Expense Tracker — loaded 0 existing expenses
... add a couple, save and quit ...

$ python3 expense_tracker.py
 Expense Tracker — loaded 2 existing expenses
```

And `expenses.json` should contain something like:

```json
[
 {
 "amount": 12.5,
 "category": "food",
 "date": "2026-05-12"
 }
]
```

## Key takeaway

- **The standard library is huge.** `import` a module, call its functions.
- `json.dump(obj, file)` writes; `json.load(file)` reads. Python data structures (`dict`, `list`, `str`, `int`, `float`, `bool`, `None`) map cleanly to JSON.
- `with open(...) as f:` is the right way to open files — it closes them automatically.
- `pathlib.Path` is the modern alternative to messy string-based paths.
- `datetime.now().strftime(...)` formats the current date/time as a string.

 [json module](https://docs.python.org/3/library/json.html) · [pathlib](https://docs.python.org/3/library/pathlib.html) · [datetime](https://docs.python.org/3/library/datetime.html) · [Reading and writing files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

---

# Task 8 — The `json` library in depth 15 min

## Concept

In Task 7 we used `json.load` and `json.dump` to read and write our expenses file. The `json` module does **more than that**, and you'll need it constantly when working with APIs, configs, log files, and almost anything that crosses a boundary between two systems.

The module has **four core functions**, all built around the same idea — converting between **Python objects** and **JSON text**:

| Function | Direction | Works with |
|----------------|----------------------------|----------------|
| `json.dumps` | Python → JSON **string** | An in-memory string |
| `json.loads` | JSON **string** → Python | An in-memory string |
| `json.dump` | Python → JSON **file** | An open file object |
| `json.load` | JSON **file** → Python | An open file object |

The `s` suffix means **"string"**. The functions without `s` work directly with files.

### Python ↔ JSON type mapping

| Python | JSON |
|-------------------------|--------------|
| `dict` | object |
| `list`, `tuple` | array |
| `str` | string |
| `int`, `float` | number |
| `True` / `False` | true / false |
| `None` | null |

> **Watch out:** `datetime`, `set`, custom classes are **not** JSON-serializable out of the box — you'll get `TypeError`. Convert them to strings, lists, or dicts first. That's why in Task 7 we stored the date as `"2026-05-12"` (a string), not a `datetime` object.

## Starter code — work in a separate file

This task isn't about extending the tracker — it's about getting comfortable with the `json` library on its own. Create a new file `json_practice.py` next to your tracker, then paste this:

```python
import json

# === 1) Python object → JSON string with dumps ===
expense = {
 "amount": 12.50,
 "category": "food",
 "date": "2026-05-12",
 "tags": ["lunch", "weekday"],
 "is_recurring": False,
 "notes": None,
}

# Compact (default): single line, minimal whitespace
compact = json.dumps(expense)
print("Compact JSON:")
print(compact)
print()

# Pretty-printed: easy to read for humans
pretty = json.dumps(expense, indent=2, sort_keys=True)
print("Pretty JSON:")
print(pretty)
print()

# === 2) JSON string → Python object with loads ===
raw_text = '{"name": "Paolo", "score": 42, "active": true, "tags": ["py", "ml"]}'
parsed = json.loads(raw_text)

print("Parsed type :", type(parsed))
print("Parsed value:", parsed)
print("Name field :", parsed["name"])
print("First tag :", parsed["tags"][0])
```

## Your task

1. **Run the script** and study the output carefully.
 Notice that the compact form puts `null`/`true`/`false` (JSON spelling), not `None`/`True`/`False` (Python spelling). The `json` module did the translation for you.

2. **Round-trip test.** Convert `expense` to a string with `dumps`, then back to a dict with `loads`. Assert they're equal:

```python
text = json.dumps(expense)
restored = json.loads(text)
assert restored == expense, "Round-trip failed!"
print(" Round-trip OK")
```

3. **Save and reload a list.** Build a list of three expense dicts, write it to `practice.json` with `json.dump`, then in a fresh `with open(...)` read it back with `json.load` and print how many items you got.

4. **Read an external JSON file.** Save the following as `sample_input.json` in your folder (you can copy/paste this from the workshop doc), then write Python to load it and print the highest score:

```json
{
 "users": [
 {"name": "Alice", "score": 87},
 {"name": "Bob", "score": 92},
 {"name": "Carla", "score": 78}
 ],
 "timestamp": "2026-05-12T09:30:00"
}
```

 Hint:

```python
with open("sample_input.json", "r", encoding="utf-8") as f:
 data = json.load(f)

print("Loaded", len(data["users"]), "users")
top = max(data["users"], key=lambda u: u["score"])
print(f"Top scorer: {top['name']} with {top['score']}")
```

5. **Provoke a real error.** Try `json.dumps({1, 2, 3})` (a set). What `TypeError` do you get? This is the most common JSON pitfall in practice.

6. **Bonus — non-ASCII characters.** Try this:

```python
data = {"city": "Café Roma", "owner": "Józef"}
print(json.dumps(data)) # default: escapes accents
print(json.dumps(data, ensure_ascii=False)) # preserves accents
```

 The second form is usually what you want for human-readable output.

## Checkpoint

Your script should print something like:

```
Compact JSON:
{"amount": 12.5, "category": "food", "date": "2026-05-12", "tags": ["lunch", "weekday"], "is_recurring": false, "notes": null}

Pretty JSON:
{
 "amount": 12.5,
 "category": "food",
 ...
}

Parsed type : <class 'dict'>
Top scorer: Bob with 92
```

And `json.dumps({1, 2, 3})` should fail with:
```
TypeError: Object of type set is not JSON serializable
```

## Key takeaway

- The `json` module is **the bridge between Python and the outside world**. Configs, APIs, log files, browser data — everything uses JSON.
- Four functions, one rule: **`s` for strings, no `s` for files**. `dumps`/`loads` and `dump`/`load`.
- Always pass `indent=2` (or `4`) when writing JSON for humans to read. Use the compact form for files machines will read.
- JSON only knows a small set of types. Anything fancier (`datetime`, `set`, custom objects) must be **converted to a JSON-friendly form first**.
- Use `ensure_ascii=False` if your data has accents or non-Latin characters — otherwise JSON escapes them with `\uXXXX`.

 [json module](https://docs.python.org/3/library/json.html) ·
[json.dumps options](https://docs.python.org/3/library/json.html#json.dumps) ·
[Python ↔ JSON type table](https://docs.python.org/3/library/json.html#py-to-json-table) ·
[Real Python: Working with JSON Data](https://realpython.com/python-json/) ·
[JSON spec (json.org)](https://www.json.org/)

---

# Task 9 — Bonus: Handle the unexpected optional

## Concept

What happens right now if the user types `"abc"` when asked for an amount? Your program crashes.

A robust CLI handles bad input gracefully with **`try` / `except`**:

```python
try:
 amount = float(input("Amount: "))
except ValueError:
 print(" That's not a valid number — try again.")
 return
```

## Your task

1. Wrap the `float(input(...))` in `add_expense` with `try` / `except ValueError`.
 On failure, print a friendly message and **return early** (don't append).
2. In `load_expenses`, handle the case where `expenses.json` exists but is **corrupted** (not valid JSON). Wrap the `json.load(f)` call like this:

```python
try:
 return json.load(f)
except json.JSONDecodeError:
 print(" Couldn't read expenses file — starting fresh.")
 return []
```
3. **Test it!** Open `expenses.json` in your editor, type some garbage, save, and re-run.
4. **Bonus:** validate that `amount > 0` and reject negative or zero amounts with a helpful message.

## Key takeaway

- `try` / `except` lets your program **survive errors** instead of crashing.
- Catch **specific exceptions** (`ValueError`, `FileNotFoundError`, …) — not the bare `except:` (which hides real bugs).
- Validating input at the boundary is the easiest way to keep the rest of the code clean.

 [Errors and exceptions](https://docs.python.org/3/tutorial/errors.html) · [Built-in exceptions](https://docs.python.org/3/library/exceptions.html)

---

# Wrap-up

In about 2 to 2½ hours you built a real CLI application, set up a clean Python environment, and refreshed the entire core of the language:

| What you used | Where it appeared |
|----------------------------------------|--------------------------------------------------|
| Virtual environment + `requirements.txt` | Setup |
| Running a script | Task 0 |
| Scalar types, collection types (list/tuple/set), `type()` | Task 1 |
| `input()`, f-strings, formatting | Task 2 |
| Lists, indexing, slicing | Task 3 |
| `while`, `for`, `if/elif/else` | Task 4 |
| Dictionaries, `.get()`, `.items()` | Task 5 |
| Functions, `def`, `return` | Task 6 |
| Modules (`json`, `datetime`, `pathlib`), file I/O with `with open(...)` | Task 7 |
| `json.dumps`/`loads`, pretty-printing, external JSON files | Task 8 |
| `try` / `except` | Task 9 |

## Where to go next

- **Comprehensions:** `[e["amount"] for e in expenses if e["category"] == "food"]` — Python's expressive one-liners.
 → [List comprehensions tutorial](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- **Classes and objects:** turn your `expense` dict into an `Expense` class.
 → [Classes tutorial](https://docs.python.org/3/tutorial/classes.html)
- **Testing:** write `test_expense_tracker.py` with `pytest` and verify `total_by_category` works.
 → [pytest getting started](https://docs.pytest.org/en/stable/getting-started.html)
- **Packaging:** turn your script into something you can `pip install`.
 → [Python packaging guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- **A CLI library:** rewrite the menu with [Typer](https://typer.tiangolo.com/) or [Click](https://click.palletsprojects.com/) for proper command-line flags.

---

## Resources

| Topic | Link |
|------------------------|----------------------------------------------------------------------------|
| Official tutorial | [docs.python.org/3/tutorial](https://docs.python.org/3/tutorial/) |
| Standard library | [docs.python.org/3/library](https://docs.python.org/3/library/) |
| venv module | [docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html) |
| pip user guide | [pip.pypa.io](https://pip.pypa.io/en/stable/user_guide/) |
| Style guide (PEP 8) | [peps.python.org/pep-0008](https://peps.python.org/pep-0008/) |
| Real Python | [realpython.com](https://realpython.com/) |
| Python cheatsheet | [python-cheatsheet.readthedocs.io](https://python-cheatsheet.readthedocs.io/) |
| f-string mini-language | [docs.python.org/3/library/string.html#formatspec](https://docs.python.org/3/library/string.html#formatspec) |
| JSON module | [docs.python.org/3/library/json.html](https://docs.python.org/3/library/json.html) |
| pathlib | [docs.python.org/3/library/pathlib.html](https://docs.python.org/3/library/pathlib.html) |
| pytest | [docs.pytest.org](https://docs.pytest.org/) |

---

## What to hand in

If the workshop is graded or reviewed, hand in:

- Your final `expense_tracker.py` (with the Task 9 error-handling additions if you completed them).
- A sample `expenses.json` produced by your program.
- Your `json_practice.py` from Task 8 (if completed).
- Your `requirements.txt` (even if empty — it shows you set up the venv properly).
- A short paragraph (in `notes.md`) on **the concept that felt most unclear** and one thing you'd like to deepen next.

> **Great job!** You now have a working Python app, a refreshed mental model of the language, and a clear path forward. Keep the file — you'll want to extend it.
