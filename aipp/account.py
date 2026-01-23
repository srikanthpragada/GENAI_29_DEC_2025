# Create a class Account to store account no, customer name, balance 
# Provide methods like deposit, withdraw, getbalance()

class Account:
    def __init__(self, account_no, customer_name, balance=0):
        self.account_no = account_no
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance
    
    