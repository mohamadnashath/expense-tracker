import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt


def show_total(expenses):
    total = 0
    for expense in expenses:
        total = total+expense["amount"]
    print("Total amount spent: ₹", total)


def show_category_total(expenses):
    categories = {}
    for expense in expenses:
        category = expense['category']
        if category in categories:
            categories[category] = categories[category]+expense["amount"]
        else:
            categories[category] = expense["amount"]
    print("\n--- Category Summary ---")
    for category, total in categories.items():
        print(f"{category}: ₹{total}")
    print("------------------------")


def show_graph(expenses):
    categories = {}
    for expense in expenses:
        category = expense["category"]
        if category in categories:
            categories[category] = categories[category]+expense["amount"]
        else:
            categories[category] = expense["amount"]
    labels = list(categories.keys())
    values = list(categories.values())
    plt.bar(labels, values, color=['red','blue','green','orange','purple'])
    plt.title("Expense by category")
    plt.xlabel("Category")
    plt.ylabel("Amount (₹)")
    plt.tight_layout()
    plt.savefig("expense_graph.png")
    plt.show()
