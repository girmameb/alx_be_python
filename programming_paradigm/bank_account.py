# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initializes the BankAccount with an optional initial balance."""
        self._account_balance = initial_balance  # Encapsulation: private attribute

    def deposit(self, amount):
        """Deposits a specified amount into the account."""
        if amount > 0:
            self._account_balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws a specified amount from the account. Returns True if successful, otherwise False."""
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Displays the current balance."""
        print(f"Current Balance: ${self._account_balance:.2f}")

# Ensure that this script can be tested independently (optional)
if __name__ == "__main__":
    # Simple tests for the BankAccount class
    account = BankAccount(100)
    account.display_balance()  # Should show $100.00
    account.deposit(50)
    account.display_balance()  # Should show $150.00
    if account.withdraw(20):
        print("Withdrawal successful.")
    else:
        print("Withdrawal failed.")
    account.display_balance()  # Should show $130.00
    if not account.withdraw(200):
        print("Insufficient funds.")
    account.display_balance()  # Should still show $130.00

