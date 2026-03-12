#!/usr/bin/python3

class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """Deposits a positive amount into the checkbook balance."""
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """Withdraws a positive amount from the checkbook balance if funds are sufficient."""
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Prints the current checkbook balance."""
        print("Current Balance: ${:.2f}".format(self.balance))


def get_amount(prompt):
    """
    Prompts the user for a numeric dollar amount, retrying on invalid input.

    Parameters:
        prompt (str): The message displayed to the user.

    Returns:
        float: A valid positive numeric value entered by the user.
    """
    while True:
        try:
            amount = float(input(prompt))
            return amount
        except ValueError:
            print("Invalid input. Please enter a numeric value (e.g., 10 or 10.50).")


def main():
    cb = Checkbook()
    while True:
        action = input("\nWhat would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            print("Goodbye!")
            break
        elif action == 'deposit':
            amount = get_amount("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = get_amount("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
