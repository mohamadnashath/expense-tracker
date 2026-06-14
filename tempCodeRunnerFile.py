from expenses import add_expense, view_expense
from storage import load_data, save_data


def main():
    expenses = load_data()
    while True:
        print("\n   EXPENSE TRACKER   ")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Total Spent")
        print("4. Category Summary")
        print("5. Show Graph")
        print("6. Exit")
        choice = input("Enter Choice: ")
        print(repr(choice))

        if choice == "6":
            save_data(expenses)
            break

        if choice == "1":
            print("calling")
            add_expense(expenses)
        elif choice == "2":
            view_expense(expenses)


main()
