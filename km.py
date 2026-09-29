class ATM:
    def __init__(self, pin, balance=5000):
        self.__pin = pin
        self.__balance = balance
        self.__history = []

    def login(self):
        for attempt in range(3):
            entered_pin = input("Enter ATM PIN: ")
            if entered_pin == self.__pin:
                print("\nLogin Successful!\n")
                return True
            else:
                print("Incorrect PIN!")
        print("Card Blocked! Too many attempts.")
        return False

    def check_balance(self):
        print(f"Current Balance: ₹{self.__balance}")
        self.__history.append(f"Balance Checked: ₹{self.__balance}")

    def deposit(self):
        try:
            amount = float(input("Enter deposit amount: ₹"))
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            self.__balance += amount      # amount = amount += self.__balance
            self.__history.append(f"Deposited: ₹{amount}")
            print("Deposit Successful!")
        except ValueError as e:
            print("Error:", e)

    def withdraw(self):
        try:
            amount = float(input("Enter withdrawal amount: ₹"))
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            if amount > self.__balance:
                raise Exception("Insufficient Balance!")
            self.__balance -= amount
            self.__history.append(f"Withdrawn: ₹{amount}")
            print("Please collect your cash.")
        except Exception as e:
            print("Error:", e)

    def history(self):
        print("\nTransaction History")
        print("-" * 30)
        if not self.__history:
            print("No transactions found.")
        else:
            for transaction in self.__history:
                print(transaction)

    def menu(self):
        while True:
            print("\n===== ATM MENU =====")
            print("1. Balance Inquiry")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transaction History")
            print("5. Exit")

            choice =input("Enter your choice: ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.history()
            elif choice == "5":
                print("Thank you for using our ATM.")
                break
            else:
                print("Invalid Choice!")


# Driver Code
atm = ATM(pin="1234", balance=10000)

if atm.login():
    atm.menu()