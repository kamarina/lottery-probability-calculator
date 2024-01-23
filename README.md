# Lottery Probability Calculator

This Python script calculates the probability of winning a lottery, taking into account the total number of tickets, the number of winning tickets, and the number of tickets sold.

## Features

- Calculate the chance that a winning ticket is not sold.
- Determine the probability of winning when buying a specific number of tickets.
- User-friendly command-line interface for input and interaction.

## How It Works
The script consists of three main functions:

1. *calculate_lottery_probability*
This function calculates the probability of winning the lottery based on the provided parameters:

total_tickets: Total number of tickets in the lottery.
winning_tickets: Number of winning tickets in the lottery.
tickets_bought: Number of tickets the user plans to purchase.
If any of these values are non-positive, the function returns 0.0. If the user plans to purchase all tickets, the probability is set to 100%. If the user plans to purchase more tickets than the remaining non-winning tickets, the probability is set to 0%. Otherwise, the function calculates the probability using the binomial coefficient formula.

2. *calculate_lottery_chance*
This function calculates the probability that any winning ticket is not sold. It takes the same parameters as calculate_lottery_probability and returns the probability_not_sold. If all tickets are sold, it raises a ValueError since the probability cannot be calculated in this scenario.

3. *main*
The main function serves as the entry point to the program. It welcomes the user to the Lottery Probability Calculator and prompts them to enter the total number of tickets, the number of winning tickets, and the number of tickets they plan to purchase. It then calculates and displays the chance that a winning ticket is not sold and the probability of winning with the specified number of tickets.

## How to Use

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/lottery-probability-calculator.git
    cd lottery-probability-calculator
    ```

2. **Run the Script:**

    ```bash
    python lottery.py
    ```

3. **Follow the Prompts:**

    - Enter the total number of tickets.
    - Enter the number of winning tickets.
    - Enter the number of tickets you plan to purchace.

4. **Interact with the Program:**

    - The program will provide information on the chance that a winning ticket is not sold.
    - Enter the number of tickets you are considering buying (enter 0 to exit).
    - The program will display the probability of winning when buying a specific number of tickets.
    - Choose to re-enter values, change the number of tickets, or exit the program.

## Requirements

- Python 3.x

## Example

```bash
Welcome to the Lottery Probability Calculator!
Enter the total number of tickets in the lottery: 10
Enter the number of winning tickets: 5
Enter the number of tickets you plan to purchase: 4

The chance that a winning ticket is not sold is: 0.8333 or 83.33%
The probability of winning with 4 tickets is: 2.38%

```
# Contributing
If you'd like to contribute to the project, please follow these guidelines:

* Fork the repository.
* Create a new branch for your feature or bug fix.
* Make your changes and submit a pull request.
