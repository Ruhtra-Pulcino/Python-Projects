choice = int(input("welcome to the simple calculator\nType one of the options below\n1 - Sum\n2 - Subtraction\n3 -Multiplication\n4 - Division\n5 - Leave calculator\n"))

while True:

    if choice == 1:

        number1 = int(input("Type the first number: "))
        number2 = int(input("Type the last number: \n"))

        result = number1 + number2

        print(f"{number1} + {number2}: {result}\n")

        choice = int(input("welcome to the simple calculator\nType one of the options below\n1 - Sum\n2 - Subtraction\n3 -Multiplication\n4 - Division\n5 - Leave calculator\n"))     

    elif choice == 2:

        number1 = int(input("Type the first number: "))
        number2 = int(input("Type the last number: \n"))
        
        result = number1 - number2
        
        print(f"{number1} - {number2}: {result}\n")
        
        choice = int(input("welcome to the simple calculator\nType one of the options below\n1 - Sum\n2 - Subtraction\n3 -Multiplication\n4 - Division\n5 - Leave calculator\n"))

    elif choice == 3:

        number1 = int(input("Type the first number: "))
        number2 = int(input("Type the last number: \n"))
        
        result = number1 * number2
        
        print(f"{number1} * {number2}: {result}\n")
        
        choice = int(input("welcome to the simple calculator\nType one of the options below\n1 - Sum\n2 - Subtraction\n3 -Multiplication\n4 - Division\n5 - Leave calculator\n"))

    elif choice == 4:

        number1 = int(input("Type the first number: "))
        number2 = int(input("Type the last number: \n"))
        
        result = number1 / number2
        
        print(f"{number1} / {number2}: {result}\n")
        
        choice = int(input("welcome to the simple calculator\nType one of the options below\n1 - Sum\n2 - Subtraction\n3 -Multiplication\n4 - Division\n5 - Leave calculator\n"))
    
    elif choice == 5:

        print("You leave the calculator")

        break