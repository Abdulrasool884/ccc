# Knapsack Project (Clean Version)

def fractional_knapsack(weights, values, capacity):
    items = list(zip(weights, values))
    items.sort(key=lambda x: x[1]/x[0], reverse=True)

    total_value = 0.0
    selected = []

    for weight, value in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
            selected.append((weight, value, 1))
        else:
            fraction = capacity / weight
            total_value += value * fraction
            selected.append((weight, value, round(fraction, 2)))
            break

    return total_value, selected


def zero_one_knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0]*(capacity+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w],
                               values[i-1] + dp[i-1][w - weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    # Backtracking to find selected items
    w = capacity
    selected = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append((weights[i-1], values[i-1]))
            w -= weights[i-1]

    return dp[n][capacity], selected[::-1]


def display_items(weights, values):
    print("\nItems:")
    print("Index | Weight | Value | Ratio")
    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        print(f"{i+1:^5} | {weights[i]:^6} | {values[i]:^5} | {ratio:.2f}")


# MAIN PROGRAM
print("===== KNAPSACK PROJECT =====")

n = int(input("Enter number of items: "))
weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))
capacity = int(input("Enter capacity: "))

display_items(weights, values)

# Greedy
g_value, g_items = fractional_knapsack(weights, values, capacity)

# DP
dp_value, dp_items = zero_one_knapsack(weights, values, capacity)

print("\n--- Fractional Knapsack (Greedy) ---")
print("Max Value:", round(g_value, 2))
print("Selected Items (weight, value, fraction):")
for item in g_items:
    print(item)

print("\n--- 0/1 Knapsack (DP) ---")
print("Max Value:", dp_value)
print("Selected Items (weight, value):")
for item in dp_items:
    print(item)

print("\n--- Comparison ---")
print(f"Greedy Value = {round(g_value,2)} | DP Value = {dp_value}")