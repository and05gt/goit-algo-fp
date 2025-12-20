def greedy_algorithm(items, budget):
    """Selects dishes with the highest calorie-to-cost ratio."""

    item_list = []
    for name, details in items.items():
        cost = details['cost']
        calories = details['calories']
        ratio = calories / cost if cost > 0 else 0
        item_list.append({'name': name, 'cost': cost, 'calories': calories, 'ratio': ratio})

    item_list.sort(key=lambda x: (x['ratio'], x['calories']), reverse=True)

    total_cost = 0
    total_calories = 0
    selected_items = []

    for item in item_list:
        if total_cost + item['cost'] <= budget:
            selected_items.append(item['name'])
            total_cost += item['cost']
            total_calories += item['calories']

    return selected_items, total_calories, total_cost

def dynamic_programming_algorithm(items, budget):
    """Finds the optimal set of dishes to maximize calorie intake within a budget"""

    names = list(items.keys())
    costs = [items[name]['cost'] for name in names]
    calories = [items[name]['calories'] for name in names]
    n = len(names)  

    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            cost = costs[i - 1]
            cal = calories[i - 1]

            if cost <= w:
                dp[i][w] = max(cal + dp[i - 1][w - cost], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = budget
    total_calories = dp[n][budget]

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_name = names[i - 1]
            selected_items.append(item_name)
            w -= costs[i - 1]

    selected_items.reverse()

    total_cost = sum(items[item]['cost'] for item in selected_items)

    return selected_items, total_calories, total_cost

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget_limit = 70
print(f"Budget: {budget_limit}\n")

# Greedy Algorithm
greedy_items, greedy_calories, greedy_cost = greedy_algorithm(items, budget_limit)
print(f"--- Greedy Algorithm ---")
print(f"Selected items: {greedy_items}")
print(f"Total calories: {greedy_calories}")
print(f"Total cost: {greedy_cost}\n")

# Dynamic Programming Algorithm
dp_items, dp_calories, dp_cost = dynamic_programming_algorithm(items, budget_limit)
print(f"--- Dynamic Programming Algorithm ---")
print(f"Selected items: {dp_items}")
print(f"Total calories: {dp_calories}")
print(f"Total cost: {dp_cost}")
