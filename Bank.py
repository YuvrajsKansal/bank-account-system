class Bankaccount:
    def __init__(self, name, balance=0.00):
        self.name = name
        self.__balance = balance

    def __str__(self):
        return f"{self.name} | Balance: {self.__balance:.2f}"

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return
        if amount > self.__balance:
            print("Insufficient funds.")
            return
        self.__balance -= amount
        print(f"Withdrew {amount:.2f}. New balance: {self.__balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return
        self.__balance += amount
        print(f"Deposited {amount:.2f}. New balance: {self.__balance:.2f}")

class Savingsaccount(Bankaccount):
    interest_rate = 0.06
    def __str__(self):
        return super().__str__() + f" | Savings ({self.interest_rate*100:.0f}% interest)"
    def apply_interest(self):
        interest = round(self.get_balance() * self.interest_rate, 2)
        self.deposit(interest)

def get_int_input(prompt, valid_choices):
    while True:
        try:
            val = int(input(prompt))
            if val not in valid_choices:
                print(f"Please enter one of: {valid_choices}")
                continue
            return val
        except ValueError:
            print("Please enter a valid number.")

def get_amount_input(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val <= 0:
                print("Amount must be positive.")
                continue
            return val
        except ValueError:
            print("Please enter a valid number.")

accounts = {}
saccounts = {}
next_acc_number = 1
next_sacc_number = 1

def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()
        if name == "":
            print("Name cannot be empty.")
        elif not all(part.isalpha() for part in name.split()):
            print("Name must contain only letters.")
        else:
            return name

def get_opening_balance():
    while True:
        balance = input("Enter initial balance (or press Enter for 0): ")
        if balance == "":
            return 0.0
        try:
            return float(balance)
        except ValueError:
            print("Invalid balance. Please enter a number.")

def create_account():
    global next_acc_number
    name = get_valid_name()
    balance = get_opening_balance()
    acc_id = f"ACC{next_acc_number:03d}"
    next_acc_number += 1
    accounts[acc_id] = Bankaccount(name, balance)
    print(f"Current account created: {acc_id}")

def create_savings_account():
    global next_sacc_number
    name = get_valid_name()
    balance = get_opening_balance()
    acc_id = f"SACC{next_sacc_number:03d}"
    next_sacc_number += 1
    saccounts[acc_id] = Savingsaccount(name, balance)
    print(f"Savings account created: {acc_id}")
    saccounts[acc_id].apply_interest()

def view_account():
    acc_id = input("Enter account number: ").strip()
    acc = accounts.get(acc_id) or saccounts.get(acc_id)
    if acc is None:
        print("Account not found.")
        return
    print(acc)
    action = get_int_input("1) Withdraw 2) Deposit 3) Back: ", [1,2,3])
    if action == 1:
        acc.withdraw(get_amount_input("Enter withdrawal amount: "))
    elif action == 2:
        acc.deposit(get_amount_input("Enter deposit amount: "))

def list_accounts():
    if not accounts and not saccounts:
        print("No accounts found.")
        return
    for acc_id, acc in {**accounts, **saccounts}.items():
        print(f"{acc_id}: {acc}")

def main():
    print("Welcome to the python bank!")
    while True:
        print("\n1) Current 2) Savings 3) View 4) List 5) Exit")
        choice = get_int_input("Enter here (1-5): ", [1,2,3,4,5])
        if choice == 5:
            print("Thank you for visiting the python bank!")
            break
        elif choice == 1: create_account()
        elif choice == 2: create_savings_account()
        elif choice == 3: view_account()
        elif choice == 4: list_accounts()

main()