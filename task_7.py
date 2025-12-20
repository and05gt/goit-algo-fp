import random

def monte_carlo_dice_simulation(num_simulations=1000000):
    """Monte Carlo simulation of rolling two dice."""

    sum_counts = {total: 0 for total in range(2, 13)}

    for _ in range(num_simulations):
        number1 = random.randint(1, 6)
        number2 = random.randint(1, 6)
        total_sum = number1 + number2
        sum_counts[total_sum] += 1

    # Output results in table form
    print(f"{'-'*56}")
    print(f"{'Sum':<6} | {'Count':<12} | {'Probability (MC)':<16} | {'Theoretical':<10}")
    print(f"{'-'*56}")

    results = {}

    for total in range(2, 13):
        count = sum_counts[total]
        probability = (count / num_simulations) * 100

        # Theoretical probability for comparison
        theoretical_counts = {2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:5, 9:4, 10:3, 11:2, 12:1}
        theoretical_probability = (theoretical_counts[total] / 36) * 100

        results[total] = probability

        print(f"{total:<6} | {count:<12} | {probability:<15.2f}% | {theoretical_probability:5.2f}% ({theoretical_counts[total]}/36)")

    print(f"{'-'*56}")

    return results

if __name__ == "__main__":
    print("Starting Monte Carlo Dice Simulation...\n")
    monte_carlo_dice_simulation(1000000)
