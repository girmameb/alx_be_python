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
                return True
            else:
                return False
        else:
            raise ValueError("Withdrawal amount must be positive.")

    def get_balance(self):
        """
        Get the current account balance.

        :return: The current balance of the account.
        """
        return self._account_balance

