from expenses import add_expense, view_expense
from storage import load_data, save_data
from analytics import show_total, show_category_total, show_graph


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
        print("7. Reset All Expenses")
        choice = input("Enter Choice: ")

        if choice == "6":
            save_data(expenses)
            break

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expense(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            show_category_total(expenses)
        elif choice == "5":
            show_graph(expenses)
        elif choice == "7":
            expenses = []
            save_data(expenses)
            print("All expenses cleared!")


main()
