class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} amount is deposited.")
        else:
            print("Invalid!")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn.")
        else:
            print("You don't have enough money!")

    def get_balance(self):
        return self.__balance


class Savings_account(Account):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        print(f"Interest added: {interest}")
        self.deposit(interest)


class Current_Account(Account):
    def __init__(self, name, balance, overdraft_limit):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.get_balance() + self.overdraft_limit:
            print("Overdraft limit exceeded.")
        else:
            new_balance = self.get_balance() - amount
            self._Account__balance = new_balance
            print(f"{amount} withdrawn (with overdraft if needed)")


def menu():
    print("1. Savings Account \n2. Current Account")
    choice = int(input("Enter your account type: "))

    name = input("Enter your name: ")
    balance = float(input("Enter your initial balance: "))

    if choice == 1:
        rate = float(input("Enter interest rate: "))
        account = Savings_account(name, balance, rate)
    elif choice == 2:
        limit = float(input("Enter overdraft limit: "))
        account = Current_Account(name, balance, limit)
    else:
        print("Invalid choice!")
        return

    while True:
        print("\n1. Deposit \n2. Withdraw \n3. Check Balance \n4. Add Interest (Savings only) \n5. Exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            amt = float(input("Enter amount: "))
            account.deposit(amt)

        elif ch == 2:
            amt = float(input("Enter amount: "))
            account.withdraw(amt)

        elif ch == 3:
            print(f"Balance: {account.get_balance()}")

        elif ch == 4:
            if isinstance(account, Savings_account):
                account.calculate_interest()
            else:
                print("Only for Savings Account!")

        elif ch == 5:
            print("Thank you!")
            break

        else:
            print("Invalid choice! Try again.")


menu()
