import math

def calculate_lottery_probability(total_tickets, winning_tickets, tickets_bought):
    """
    Calculate the probability of winning the lottery.

    Parameters:
    - total_tickets: Total number of tickets in the lottery.
    - winning_tickets: Number of winning tickets in the lottery.
    - tickets_bought: Number of tickets the user plans to purchase.

    Returns:
    - Probability of winning.
    """
    if total_tickets <= 0 or winning_tickets <= 0 or tickets_bought <= 0:
        return 0.0

    # If user plans to purchase all tickets, probability is 100%
    if tickets_bought == total_tickets:
        return 1.0

    # If user plans to purchase more tickets than the remaining non-winning tickets, probability is 0%
    remaining_non_winning_tickets = total_tickets - winning_tickets
    if tickets_bought > remaining_non_winning_tickets:
        return 0.0

    # Calculate the number of combinations for total tickets and winning tickets
    total_combinations = math.comb(total_tickets, tickets_bought)
    winning_combinations = math.comb(winning_tickets, tickets_bought)

    # Calculate the probability of winning
    probability = winning_combinations / total_combinations
    return probability

def main():
    print("Welcome to the Lottery Probability Calculator!")

    # Get user input
    total_tickets = int(input("Enter the total number of tickets in the lottery: "))
    winning_tickets = int(input("Enter the number of winning tickets: "))
    tickets_bought = int(input("Enter the number of tickets you plan to purchase: "))

    # Calculate and display the probability
    probability = calculate_lottery_probability(total_tickets, winning_tickets, tickets_bought)
    print(f"The probability of winning with {tickets_bought} tickets is: {round(probability * 100, 2):.2f}%")

if __name__ == "__main__":
    main()
