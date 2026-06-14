from datetime import date


def add_expense(expenses):
    name = input("enter name: ")
    amount = float(input("enter amount: "))
    today = str(date.today())
    print("1. Food")
    print("2. Travel")
    print("3. Entertainment")
    print("4. College")
    print("5. Other")
    cat_choice = input("Choose category: ")

    if cat_choice == "1":
        category = "Food"
    elif cat_choice == "2":
        category = "Travel"
    elif cat_choice == "3":
        category = "Entertainment"
    elif cat_choice == "4":
        category = "College"
    else:
        category = "Other"
    expense = {"name": name, "amount": amount,
               "category": category, "date": today}
    expenses.append(expense)
    print("expense added")


def view_expense(expenses):
    for expense in expenses:
        print("Name:", expense["name"], "| Amount:",
              expense["amount"], "| Category:", expense["category"], "| date:", expense["date"])
