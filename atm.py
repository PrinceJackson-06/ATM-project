balance = 10000
print("Welcome to ICICI Bank")
print("Insert Your Card")
print("Your card is valid!")
while True:
      pin=int(input("Enter Your Pin No : "))
      if pin == 1234:
            print("1.Check Balance")
            print("2.Withdraw")
            print("3. Deposit")
            print("4. Exit")
            option= int(input("Choose your Option : "))
            if option == 1 :
                print(balance)
            elif option == 2 :
                amount = int(input("Enter your withdraw amount : "))
                balance -= amount
                # amount = amount - balance
                print(f"Your Withdrawal Amount : {balance} \n")
            elif option == 3 :
                amount = int(input("Enter your Deposit amount : "))
                balance += amount
                print(f"Your Deposit amount is : {balance}\n")
            elif option == 4 :
                print("Thankyou For our Visiting ICICI ATM!")
                exit()
            else:
                print("choose your correct option!")
      else:
            print("Invalid Pin!")