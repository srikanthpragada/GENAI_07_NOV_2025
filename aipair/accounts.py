# Account class with acno, customer, balance attributes and methods to deposit, withdraw, and display balance
class InsufficientBalanceError(Exception):
    def __init__(self, message="Insufficient balance for withdrawal"):
        super().__init__(message)


class Account:
    def __init__(self, acno, customer, balance=0):
        self.acno = acno
        self.customer = customer
        self.current_balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.current_balance += amount

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account balance.

        Args:
            amount (float): The amount to withdraw. Must be positive.

        Raises:
            ValueError: If the withdrawal amount is not positive.
            InsufficientBalanceError: If the withdrawal amount exceeds the current balance.

        Updates:
            self.current_balance: Decreases by the withdrawn amount.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.current_balance:
            raise InsufficientBalanceError(
                f"Cannot withdraw {amount}: available balance is {self.current_balance}"
            )
        self.current_balance -= amount

    def display_balance(self):
        return self.current_balance