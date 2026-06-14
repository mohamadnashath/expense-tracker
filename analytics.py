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
    for category, total in categories.items():
        print(f"{category}: ₹{total}")


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
    plt.bar(labels, values)
    plt.title("Expense by category")
    plt.xlabel("Category")
    plt.ylabel("Amount (₹)")
    plt.show()
