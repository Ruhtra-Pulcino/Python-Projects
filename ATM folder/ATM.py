balance = 1000

choose = int(input("Welcome to the ATM\n1 - Check balance\n2 - Deposit Money\n3 - Withdraw\n4 - Exit\n"))

while True:

    if choose < 1 or choose > 5:

        print("Invalid option")

        choose = int(input("Welcome to the ATM\n1 - Check balance\n2 - Deposit Money\n3 - Withdraw\n4 - Exit\n"))

    elif choose == 1:

        print(f"Your balance: ${balance}")

        choose = int(input("Welcome to the ATM\n1 - Check balance\n2 - Deposit Money\n3 - Withdraw\n4 - Exit\n"))

    elif choose == 2:

        deposit = int(input("How much do you want to deposit: "))

        if deposit < 1:

            print("Invalid option")

            deposit = int(input("How much do you want to deposit: "))

            balance += deposit

            print(f"Your balance: {balance}")
            
            choose = int(input("Welcome to the ATM\n1 - Check balance\n2 - Deposit Money\n3 - Withdraw\n4 - Exit\n"))

        else:
            
            balance += deposit

            print(f"Your balance: {balance}")

            choose = int(input("Welcome to the ATM\n1 - Check balance\n2 - Deposit Money\n3 - Withdraw\n4 - Exit\n"))

    elif choose == 3:

        withdraw = int(input("How much do you want to withdraw: "))

        if withdraw > balance:

            print("Withdrawal amount exceeds account balance")
            
            print(f"Your available withdrawal amount is ${balance} dollars.")
            
            choose = int(input("Welcome to the ATM\n1 - Check balance\n2 - Deposit Money\n3 - Withdraw\n4 - Exit\n"))


        else:

            balance -= withdraw

            print(f"Your balance: ${balance}")

            choose = int(input("Welcome to the ATM\n1 - Check balance\n2 - Deposit Money\n3 - Withdraw\n4 - Exit\n"))
        

    elif choose == 4:

        print("You leave the ATM")

        break