
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully!")
        else:
            print("Enter a valid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid amount.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Amount withdrawn successfully!")

    def display_balance(self):
        print("Account holder:", self.name)
        print("Current balance: Rs.", self.balance)


account = BankAccount("Teja", 1000)

while True:
    print("\n--- BANK ACCOUNT ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: Rs. "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: Rs. "))
        account.withdraw(amount)

    elif choice == "3":
        account.display_balance()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
