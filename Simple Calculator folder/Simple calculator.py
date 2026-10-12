choice = int(input("welcome to the simple calculator\nType one of the options below\n1 - Sum\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Leave calculator\nYour choice: "))

while True:

    if choice == 1:

        number1 = (input("Type the first number: "))
        number2 = (input("Type the last number: "))

        if '.' in number1 and '.' not in number2:

            number1 = float(number1)
            number2 = int(number2)

            result = number1 + number2

            print(f"\n{number1} + {number2} : {result}\n")

            choice = int(input("welcome to the simple calculator\nType one of the options below\n1 - Sum\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Leave calculator\nYour choice: "))     

        elif '.' not in number1 and '.' in number2:

            number1 = int(number1)
            number2 = float(number2)

            result = number1 + number2

            print(f"\n{number1} + {number2} : {result}")

            choice = int(input("welcome to the simple calculator\nType one of the options below\n1 - Sum\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Leave calculator\nYour choice: "))

        elif '.' not in number1 and '.' not in number2:

            number1 = int(number1)
            number2 = int(number2)

            result = number1 + number2

            print(f"\n{number1} + {number2} : {result}")

            choice = int(input("welcome to the simple calculator\nType one of the options below\n1 - Sum\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Leave calculator\nYour choice: "))

        elif '.' in number1 and '.' in number2:

            number1 = float(number1)
            number2 = float(number2)

            result = number1 + number2

            print(f"\n{number1} + {number2} : {result}")

            choice = int(input("welcome to the simple calculator\nType one of the options below\n1 - Sum\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Leave calculator\nYour choice: "))

    elif choice == 2:

        number1 = (input("Type the first number: "))
        number2 = (input("Type the last number: "))
        
        if '.' in number1 and '.' not in number2:
        
            number1 = float(number1)
            number2 = int(number2)
        
            result = number1 - number2
        
            print(f"\n{number1} - {number2} : {result}\n")
        
            choice = int(input("welcome to the simple calculator\nType one of the options below\n1 - Sum\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Leave calculator\nYour choice: "))     
        
        elif '.' not in number1 and '.' in number2:
        
            number1 = int(number1)
            number2 = float(number2)
        
            result = number1 - number2
        
            print(f"\n{number1} - {number2} : {result}")
        
            choice = int(input("welcome to the simple calculator\nType one of the options below\n1 - Sum\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Leave calculator\nYour choice: "))
        
        elif '.' not in number1 and '.' not in number2:
        
            number1 = int(number1)
            number2 = int(number2)
        
            result = number1 - number2
        
            print(f"\n{number1} - {number2} : {result}")
        
            choice = int(input("welcome to the simple calculator\nType one of the options below\n1 - Sum\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Leave calculator\nYour choice: "))
        
        elif '.' in number1 and '.' in number2:
        
            number1 = float(number1)
            number2 = float(number2)
        
            result = number1 - number2
        
            print(f"\n{number1} - {number2} : {result}")
        
            choice = int(input("welcome to the simple calculator\nType one of the options below\n1 - Sum\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Leave calculator\nYour choice: "))

    elif choice == 3:

        number1 = (input("Type the first number: "))
        number2 = (input("Type the last number: "))
        
        if '.' in number1 and '.' not in number2:
        
            number1 = float(number1)
            number2 = int(number2)
        
            result = number1 * number2
        
            print(f"\n{number1} * {number2} : {result}\n")
        
            choice = int(input("welcome to the simple calculator\nType one of the options below\n1 - Sum\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Leave calculator\nYour choice: "))     
        
        elif '.' not in number1 and '.' in number2:
        
            number1 = int(number1)
            number2 = float(number2)
        
            result = number1 * number2
        
            print(f"\n{number1} * {number2} : {result}")
        
            choice = int(input("welcome to the simple calculator\nType one of the options below\n1 - Sum\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Leave calculator\nYour choice: "))
        
        elif '.' not in number1 and '.' not in number2:
        
            number1 = int(number1)
            number2 = int(number2)
        
            result = number1 * number2
        
            print(f"\n{number1} * {number2} : {result}")
        
            choice = int(input("welcome to the simple calculator\nType one of the options below\n1 - Sum\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Leave calculator\nYour choice: "))
        
        elif '.' in number1 and '.' in number2:
        
            number1 = float(number1)
            number2 = float(number2)
        
            result = number1 * number2
        
            print(f"\n{number1} * {number2} : {result}")
        
            choice = int(input("welcome to the simple calculator\nType one of the options below\n1 - Sum\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Leave calculator\nYour choice: "))

    elif choice == 4:

        number1 = float(input("Type the first number: "))
        number2 = float(input("Type the last number: "))

        if number1 == 0 or number2 == 0:

            print("It is not possible to divide by zero.\n")

            choice = int(input("welcome to the simple calculator\nType one of the options below\n1 - Sum\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Leave calculator\nYour choice: "))

        else:
            
            number1 = (input("Type the first number: "))
            number2 = (input("Type the last number: "))
            
            if '.' in number1 and '.' not in number2:
            
                number1 = float(number1)
                number2 = int(number2)
            
                result = number1 / number2
            
                print(f"\n{number1} / {number2} : {result}\n")
            
                choice = int(input("welcome to the simple calculator\nType one of the options below\n1 - Sum\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Leave calculator\nYour choice: "))     
            
            elif '.' not in number1 and '.' in number2:
            
                number1 = int(number1)
                number2 = float(number2)
            
                result = number1 / number2
            
                print(f"\n{number1} / {number2} : {result}")
            
                choice = int(input("welcome to the simple calculator\nType one of the options below\n1 - Sum\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Leave calculator\nYour choice: "))
            
            elif '.' not in number1 and '.' not in number2:
            
                number1 = int(number1)
                number2 = int(number2)
            
                result = number1 / number2
            
                print(f"\n{number1} / {number2} : {result}")
            
                choice = int(input("welcome to the simple calculator\nType one of the options below\n1 - Sum\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Leave calculator\nYour choice: "))
            
            elif '.' in number1 and '.' in number2:
            
                number1 = float(number1)
                number2 = float(number2)
            
                result = number1 / number2
            
                print(f"\n{number1} / {number2} : {result}")
            
                choice = int(input("welcome to the simple calculator\nType one of the options below\n1 - Sum\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Leave calculator\nYour choice: "))
    
    elif choice == 5:

        print("You leave the calculator")

        break