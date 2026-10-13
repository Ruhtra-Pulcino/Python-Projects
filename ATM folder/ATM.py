balance = 1000

print("--------------------------------")
choose = int(input("------ WELCOME TO THE ATM ------\n       1 - CHECK BALANCE\n       2 - DEPOSIT MONEY\n       3 - WITHDRAW\n       4 - EXIT\n        YOUR CHOICE: "))
print("--------------------------------\n")

while True:

    if choose < 1 or choose > 5:
        print("--------------------------------")
        print("       INVALID OPTION")
        print("--------------------------------\n")
        
        print("--------------------------------")
        choose = int(input("------ WELCOME TO THE ATM ------\n       1 - CHECK BALANCE\n       2 - DEPOSIT MONEY\n       3 - WITHDRAW\n       4 - EXIT\n        YOUR CHOICE: "))
        print("--------------------------------\n")

    elif choose == 1:

        print("--------------------------------")
        print(f"       YOUR BALANCE: ${balance}")
        print("--------------------------------\n")
        print("--------------------------------")
        choose = int(input("------ WELCOME TO THE ATM ------\n       1 - CHECK BALANCE\n       2 - DEPOSIT MONEY\n       3 - WITHDRAW\n       4 - EXIT\n        YOUR CHOICE: "))
        print("--------------------------------\n")

    elif choose == 2:
        print("--------------------------------")
        deposit = int(input("HOW MUCH DO YOU WANT TO DEPOSIT: "))

        if deposit < 1:

            print("      INVALID OPTION\n")

            deposit = int(input("HOW MUCH DO YOU WANT TO DEPOSIT: "))

            balance += deposit

            print(f"       YOUR BALANCE: {balance}")
            print("--------------------------------\n")
            print("--------------------------------")
            choose = int(input("------ WELCOME TO THE ATM ------\n       1 - CHECK BALANCE\n       2 - DEPOSIT MONEY\n       3 - WITHDRAW\n       4 - EXIT\n        YOUR CHOICE: "))
            print("--------------------------------\n")

        else:
            
            balance += deposit

            print(f"       YOUR BALANCE: {balance}")
            print("--------------------------------\n")
            print("--------------------------------")
            choose = int(input("------ WELCOME TO THE ATM ------\n       1 - CHECK BALANCE\n       2 - DEPOSIT MONEY\n       3 - WITHDRAW\n       4 - EXIT\n        YOUR CHOICE: "))
            print("--------------------------------\n")

    elif choose == 3:
        print("--------------------------------")
        withdraw = int(input("HOW MUCH DO YOU WANT TO WITHDRAW: "))

        if withdraw > balance:

            print("WITHDRAWAL AMOUNT EXCCEDS ACCOUNT BALANCE\n")
                        
            print(f"YOUR AVAILABLE WITHDRAWAL AMOUNT IS ${balance} DOLLARS.")
            print("--------------------------------\n")
            print("--------------------------------\n")
            choose = int(input("------ WELCOME TO THE ATM ------\n       1 - CHECK BALANCE\n       2 - DEPOSIT MONEY\n       3 - WITHDRAW\n       4 - EXIT\n        YOUR CHOICE: "))
            print("--------------------------------\n")


        else:

            balance -= withdraw

            print(f"       YOUR BALANCE: ${balance}")
            print("--------------------------------\n")
            print("--------------------------------")
            choose = int(input("------ WELCOME TO THE ATM ------\n       1 - CHECK BALANCE\n       2 - DEPOSIT MONEY\n       3 - WITHDRAW\n       4 - EXIT\n        YOUR CHOICE: "))
            print("--------------------------------\n")
        

    elif choose == 4:
        print("--------------------------------")
        print("       YOU LEAVE THE ATM")
        print("--------------------------------\n")
                

        break