import math

def calculate_lottery_chance(total_tickets, winning_tickets, tickets_bought):
    """
    Calculate the chance that a winning ticket is not sold.
    """
    # Check if the input is valid
    if not (0 <= tickets_bought <= total_tickets):
        raise ValueError("Number of tickets bought must be between 0 and the total number of tickets.")

    # Calculate the chance that a winning ticket is not sold
    unsold_tickets = total_tickets - tickets_bought

    # Check if there are unsold tickets
    if unsold_tickets <= 0:
        raise ValueError("All tickets are sold; cannot calculate the probability of not selling a winning ticket.")

    # Calculate the probability
    probability_not_sold = unsold_tickets / total_tickets

    return probability_not_sold

def calculate_winning_chance(bought_tickets, winning_tickets, total_tickets, tickets_bought):
    """
    Calculate the probability of winning when buying a specific number of tickets.
    """
    # Check if the input is valid
    if not (0 <= bought_tickets <= total_tickets) or bought_tickets > total_tickets - tickets_bought + 1:
        raise ValueError("Invalid number of tickets to buy.")

    # Check if there are unsold tickets
    unsold_tickets = total_tickets - tickets_bought

    # Calculate the probability of winning when buying a specific number of tickets
    probability_sold = bought_tickets / unsold_tickets

    return max(0.0, probability_sold)  # Ensure the probability is not negative

def get_user_input():
    """
    Get input from the user for total tickets, winning tickets, and tickets sold.
    """
    try:
        total_tickets = int(input("Enter the total number of tickets: "))
        winning_tickets = int(input("Enter the number of winning tickets: "))
        tickets_bought = int(input("Enter the number of tickets sold: "))
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid integer.")

    if total_tickets <= 0 or winning_tickets <= 0 or tickets_bought < 0:
        raise ValueError("Total tickets and winning tickets must be greater than 0, and tickets bought must be non-negative.")

    if winning_tickets > total_tickets:
        raise ValueError("Winning tickets cannot exceed the total number of tickets.")

    return total_tickets, winning_tickets, tickets_bought

def main():
    """
    Main function to execute the lottery program.
    """
    # Initial input from the user
    total_tickets, winning_tickets, tickets_bought = get_user_input()

    while True:
        # Calculate and display the chance that a winning ticket is not sold
        try:
            probability_not_sold = calculate_lottery_chance(total_tickets, winning_tickets, tickets_bought)
            print(
                f"\nThe chance that a winning ticket is not sold is: {probability_not_sold:.4f} or "
                f"{probability_not_sold * 100:.2f}%"
            )
        except ValueError as ve:
            print(f"Error: {ve}")

        # Calculate and display the probability of winning when buying a specific number of tickets
        try:
            bought_tickets = int(input("Enter the number of tickets you consider buying (enter 0 to exit): "))
            if bought_tickets == 0:
                print("Exiting the program.")
                break
            elif bought_tickets < 0 or bought_tickets > total_tickets - tickets_bought + 1:
                raise ValueError(
                    "Number of tickets to buy must be greater than or equal "
                    "to zero and not exceed available unsold tickets."
                )

            probability_sold = calculate_winning_chance(
                tickets_bought + bought_tickets, winning_tickets, total_tickets, tickets_bought
            )
            print(
                f"Probability of winning when buying {bought_tickets} ticket(s) is: {probability_sold:.4f} or "
                f"{probability_sold * 100:.2f}%"
            )
        except ValueError as ve:
            print(f"Error: {ve}")

        # Ask the user if they want to re-enter all values, change the number of tickets, or exit the program
        user_choice = input("Do you want to (R)e-enter all values, (C)hange the number of tickets, or (E)xit? ").upper()
        if user_choice == 'R':
            total_tickets, winning_tickets, tickets_bought = get_user_input()
        elif user_choice == 'C':
            # Use the current value of bought_tickets
            try:
                probability_sold = calculate_winning_chance(
                    tickets_bought + bought_tickets, winning_tickets, total_tickets, tickets_bought
                )
                print(
                    f"Probability of winning when buying {bought_tickets} ticket(s) is: {probability_sold:.4f} or "
                    f"{probability_sold * 100:.2f}%"
                )
            except ValueError as ve:
                print(f"Error: {ve}")
        elif user_choice == 'E':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Exiting the program.")
            break

if __name__ == "__main__":
    main()
