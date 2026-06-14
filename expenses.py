def add_expense(expenses):
    name = input("enter name: ")
    amount = float(input("enter amount: "))
    category = input("Enter category (Food/Travel/Entertainment/Other): ")
    expense = {"name": name, "amount": amount, "category": category}
    expenses.append(expense)
    print("expense added")


def view_expense(expenses):
    for expense in expenses:
        print("Name:", expense["name"], "| Amount:",
              expense["amount"], "| Category:", expense["category"])
