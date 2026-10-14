menu = print("", 38*"-", "\n  WELCOME TO THE TEMPERATURE CONVERTER", "\n", 38*"-", "\n", 7*" ", "  CHOOSE ONE OPTION\n", 10*" ", "  1 - CONVERT" "\n", 5*" ", "  2 - LEAVE THE SYSTEM")

while True:
    print("", 38*"-")
    option = input("         ENTER YOUR CHOICE HERE: ")
    print("", 38*"-")
    
    if option == '1':
        
        temperature = input("    ENTER THE TEMPERATURE (1C, 1F OR 1K): ")
        
        if 'c' in temperature or 'C' in temperature:
            
            temperature = temperature[:-1]
            temperature_convert = float(temperature)
            
            print(3*" ", f"YOUR ORIGINAL TEMPERATURE: {temperature_convert} C")
            print(8*" ", f"IN FAHRENHEIT: {(temperature_convert * 9/5) + 32} F")
            print(9*" ", f"IN KELVIN: {temperature_convert + 273.15} K")
            
            print("", 38*"-", "\n", 12*" ", "1 - CONVERT" "\n", 5*" ", "  2 - LEAVE THE SYSTEM")
            
        elif 'f' in temperature or 'F' in temperature:
            
            temperature = temperature[:-1]
            temperature_convert = float(temperature)
            
            print(3*" ", f"YOUR ORIGINAL TEMPERATURE: {temperature_convert} F")
            print(8*" ", f"IN CELSIUS: {(temperature_convert - 32) * 5/9} C")
            print(9*" ", f"IN KELVIN: {(temperature_convert - 32) * 5/9 + 273.15} K")
            
            print("", 38*"-", "\n", 12*" ", "1 - CONVERT" "\n", 5*" ", "  2 - LEAVE THE SYSTEM")
            
        elif 'k' in temperature or 'K' in temperature:
            
            temperature = temperature[:-1]
            temperature_convert = float(temperature)
            
            print(3*" ", f"YOUR ORIGINAL TEMPERATURE: {temperature_convert} K")
            print(8*" ", f"IN CELSIUS: {(temperature_convert - 273.15)} C")
            print(9*" ", f"IN FAHRENHEIT: {(temperature_convert - 273.15) * 9/5 + 32} F")
            
            print("", 38*"-", "\n", 12*" ", "1 - CONVERT" "\n", 5*" ", "  2 - LEAVE THE SYSTEM")
            
        else:
            
            print(4*" ", "YOU WROTE IT IN AN INVALID FORMAT")
            print("", 38*"-", "\n", 12*" ", "1 - CONVERT" "\n", 5*" ", "  2 - LEAVE THE SYSTEM")
            
                
    elif option == '2':
        
        print("", 38*"-", "\n", 8*" ", " YOU LEAVE THE SYSTEM")
        
        break
    
    else:
        
        print(12*" ","INVALID OPTION\n", 38*"-")
        print("", 38*"-", "\n", 12*" ", "1 - CONVERT" "\n", 5*" ", "  2 - LEAVE THE SYSTEM")
        
