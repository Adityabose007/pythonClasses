import numpy as np

# Expenses over 7 days: [Food, Travel, Others]
expenses = np.array([
    [120, 50, 30],
    [100, 60, 40],
    [130, 45, 25],
    [110, 70, 20],
    [115, 65, 35],
    [140, 55, 45],
    [125, 60, 30]
])

# 1. Total spent in each category
total_per_category = np.sum(expenses, axis=0)
print("Total spent per category:")
print(f"Food: ₹{total_per_category[0]}")
print(f"Travel: ₹{total_per_category[1]}")
print(f"Others: ₹{total_per_category[2]}")

# 2. Daily total expenses
daily_totals = np.sum(expenses, axis=1)
print("\nDaily total expenses:")
for i, total in enumerate(daily_totals):
    print(f"Day {i+1}: ₹{total}")

# 3. Average spent per category
average_per_category = np.mean(expenses, axis=0)
print("\nAverage spent per category:")
print(f"Food: ₹{average_per_category[0]:.2f}")
print(f"Travel: ₹{average_per_category[1]:.2f}")
print(f"Others: ₹{average_per_category[2]:.2f}")

# 4. Day with highest total expense
max_day_index = np.argmax(daily_totals)
print(f"\nDay with highest spending: Day {max_day_index+1} (₹{daily_totals[max_day_index]})")

# 5. Overall weekly total
overall_total = np.sum(expenses)
print(f"\nTotal expenses for the week: ₹{overall_total}")
