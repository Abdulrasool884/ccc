import tkinter as tk
from tkinter import messagebox


# ---------- GREEDY (FRACTIONAL KNAPSACK) ----------
def fractional_knapsack(weights, values, capacity):
    items = list(zip(weights, values))
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0.0

    for weight, value in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
        else:
            total_value += value * (capacity / weight)
            break

    return round(total_value, 2)


# ---------- DP (0/1 KNAPSACK) ----------
def zero_one_knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# ---------- SOLVE FUNCTION ----------
def solve():
    try:
        weights = list(map(int, weight_entry.get().split()))
        values = list(map(int, value_entry.get().split()))
        capacity = int(capacity_entry.get())

        if len(weights) != len(values):
            messagebox.showerror("Error", "Weights and Values must be same length!")
            return

        if capacity <= 0:
            messagebox.showerror("Error", "Capacity must be positive!")
            return

        greedy_result = fractional_knapsack(weights, values, capacity)
        dp_result = zero_one_knapsack(weights, values, capacity)

        result_label.config(
            text=f"Result:\n\nGreedy (Fractional): {greedy_result}\n0/1 Knapsack (DP): {dp_result}"
        )

    except:
        messagebox.showerror("Error", "Please enter valid numbers!")


# ---------- GUI DESIGN ----------
root = tk.Tk()
root.title("Knapsack Solver")
root.geometry("420x380")
root.resizable(False, False)

# Title
tk.Label(root, text="Knapsack Solver", font=("Arial", 16, "bold")).pack(pady=10)

# Inputs
tk.Label(root, text="Weights (space separated)").pack()
weight_entry = tk.Entry(root, width=40)
weight_entry.pack(pady=5)

tk.Label(root, text="Values (space separated)").pack()
value_entry = tk.Entry(root, width=40)
value_entry.pack(pady=5)

tk.Label(root, text="Capacity").pack()
capacity_entry = tk.Entry(root, width=20)
capacity_entry.pack(pady=5)

# Button
tk.Button(root, text="Solve", command=solve, bg="lightblue", width=15).pack(pady=15)

# Output
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run GUI
root.mainloop()