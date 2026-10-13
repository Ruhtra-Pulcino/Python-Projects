secret_number1 = 5
secret_number2 = 7

attempts = 5

guess1 = int(input("Type the first number: "))
guess2 = int(input("Type the second number: "))

while True:

    if secret_number1 == guess1 and secret_number2 == guess2:
    
        print("Congrats you win.")
        print(f"The numbers were: {secret_number1} | {secret_number2}")

        break

    elif secret_number1 != guess1 and secret_number2 != guess2 and attempts > 0:

        print("You got both of them wrong")

        attempts -= 1

        if attempts > 0:

            print(f"You have {attempts} more attempts\n")

            guess1 = int(input("Type the first number: "))
            guess2 = int(input("Type the second number: "))

        else:

             print("What a shame you lost.\n")
             print(f"The numbers were: {secret_number1} | {secret_number2}")
                 
             break

    elif secret_number1 == guess1 and secret_number2 != guess2 and attempts > 0:

        attempts -= 1

        if attempts > 0:

            print(f"you got the first number right: {secret_number1}")

            print(f"You have {attempts} more attempts\n")

            guess2 = int(input("Type the second number: "))

        else: 
            
            print("What a shame you lsot.\n")
            print(f"The numbers were: {secret_number1} | {secret_number2}")

            break

    elif secret_number1 != guess1 and secret_number2 == guess2 and attempts > 0:

        attempts -= 1

        if attempts > 0:

            print(f"You got the second number right: {secret_number2}")

            print(f"You have {attempts} more attempts\n")

            guess1= int(input("Type the first number: "))

        else:

            print("what a shame you lost.\n")
            print(f"The numbers were: {secret_number1} | {secret_number2}")

            break

    elif attempts == 0:
    
            print("What a shame you lost.\n")
            print(f"The numbers were: {secret_number1} | {secret_number2}")
    
            break


        