# 💸 Expense Tracker

A Python CLI expense tracker with category analytics and data visualization.

Log expenses, view them, get totals by category, and visualize spending with a bar chart — all from the terminal.

## Features

- ➕ Add an expense (name, amount, category, auto-dated)
- 📋 View all logged expenses
- 💰 See total amount spent
- 📊 Category-wise spending summary
- 📈 Bar chart of spending by category (saved as `expense_graph.png`)
- 🔄 Reset all expenses

## Categories

Food · Travel · Entertainment · College · Other

## Tech Stack

- Python 3
- `matplotlib` for charts
- JSON for local data storage

## Getting Started

### Prerequisites

```bash
pip install matplotlib
```

### Run

```bash
git clone https://github.com/mohamadnashath/expense-tracker.git
cd expense-tracker
python main.py
```

## Usage

You'll see a menu:

```
 EXPENSE TRACKER 
1. Add Expense
2. View Expense
3. Total Spent
4. Category Summary
5. Show Graph
6. Exit
7. Reset All Expenses
```

Pick a number and follow the prompts. Expenses are saved to `data.json` and persist between runs.

## Project Structure

```
expense-tracker/
├── main.py          # CLI menu and app loop
├── expenses.py      # add/view expense logic
├── storage.py        # load/save data.json
├── analytics.py      # totals, category summary, graph
└── data.json          # stored expenses
```

## Roadmap

- [ ] Edit/delete individual expenses
- [ ] Monthly filtering
- [ ] Export to CSV
- [ ] Switch `matplotlib` backend to be OS-independent

## License

MIT
