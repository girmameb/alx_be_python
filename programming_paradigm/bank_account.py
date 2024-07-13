# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize a new BankAccount instance with an optional initial balance.

        :param initial_balance: The initial amount to deposit into the account, default is 0.
        """
        self._account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.

        :param amount: The amount to deposit.
        :return: None
        """
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited: ${amount:.1f}")  # Print formatted to one decimal place
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account if sufficient funds are available.

        :param amount: The amount to withdraw.
        :return: True if the withdrawal was successful, otherwise False.
        """
        if amount > 0:
            if amount <= self._account_balance:
                self._account_balance -= amount
                print(f"Withdrew: ${amount:.1f}")  # Print formatted to one decimal place
                return True
            else:
                raise ValueError("Insufficient funds.")
        else:
            raise ValueError("Withdrawal amount must be positive.")

    def display_balance(self):
        """
        Display the current account balance.

        :return: None
        """
        print(f"Current Balance: ${self._account_balance:.1f}")  # Print formatted to one decimal place

