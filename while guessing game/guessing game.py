secret_number1 = 5
secret_number2 = 7

attempts = 5

guess1 = int(input("Type the first number: "))
guess2 = int(input("Type the second number: "))

while True:

    if attempts == 0:

        print("What a shame you lost.")

        break

    elif secret_number1 != guess1 and secret_number2 != guess2:

        print("You got both of them wrong")

        attempts -= 1

        print(f"You have {attempts} more attempts\n")

        guess1 = int(input("Type the first number: "))
        guess2 = int(input("Type the second number: "))

    elif secret_number1 == guess1 and secret_number2 != guess2:

        print(f"You got the first number right: {secret_number1}")

        attempts -= 1

        print(f"You have {attempts} more attmepts\n")

        guess2 = int(input("Type the second number: "))


    elif secret_number1 != guess1 and secret_number2 == guess2:

        print(f"You got the second number right: {secret_number2}")

        attempts -= 1
        
        print(f"You have {attempts} more attmepts\n")

        guess1 = int(input("Type the first number: "))

    elif secret_number1 == guess1 and secret_number2 == guess2:

        print("Congrats you win.")

        break