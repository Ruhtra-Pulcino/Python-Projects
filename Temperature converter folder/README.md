# Temperature Converter with `while` Loops

## 📌 About the Project

This project is a Python exercise focused on practicing **conditional statements**, `while` loops, mathematical operations, and string manipulation.

The program is a terminal-based temperature converter that allows users to convert temperatures between Celsius, Fahrenheit, and Kelvin. It uses the temperature unit entered by the user to determine which conversion formulas to apply and displays the equivalent temperatures in the other two units.

## 🎯 Objectives

- Practice `while` loops to create a continuous interactive menu.
- Use `if`, `elif`, and `else` statements to handle different conversion options.
- Apply mathematical formulas to convert between Celsius, Fahrenheit, and Kelvin.
- Work with user input using `input()`.
- Manipulate strings to extract numerical values and identify temperature units.
- Convert string inputs into floating-point numbers using `float()`.
- Use formatted strings (f-strings) to display conversion results.
- Validate menu selections and temperature formats.
- Control program execution using the `break` statement.

## ⚙️ How It Works

1. The program displays a welcome menu with options to convert temperatures or exit the system.
2. The user selects an option to start a conversion.
3. The program requests a temperature in a format such as `25C`, `77F`, or `298.15K`.
4. It identifies the temperature unit by checking the input for `C`, `F`, or `K`, regardless of letter case.
5. The numerical portion of the input is extracted and converted into a floating-point number.
6. The program applies the appropriate mathematical formulas to convert the original temperature into the other two units.
7. The original temperature and the converted values are displayed in the terminal.
8. If the temperature format or menu selection is invalid, the program displays an error message.
9. The menu continues to appear until the user chooses to exit the system.

## 🌡️ Conversion Formulas

- **Celsius to Fahrenheit:** \((C \times 9/5) + 32\)
- **Celsius to Kelvin:** \(C + 273.15\)
- **Fahrenheit to Celsius:** \((F - 32) \times 5/9\)
- **Fahrenheit to Kelvin:** \((F - 32) \times 5/9 + 273.15\)
- **Kelvin to Celsius:** \(K - 273.15\)
- **Kelvin to Fahrenheit:** \((K - 273.15) \times 9/5 + 32\)

## 🛠️ Technologies

- **Python 3**
- `while` loops
- `if`, `elif`, and `else` statements
- Arithmetic operators
- Variables and floating-point numbers (`float`)
- User input with `input()`
- String manipulation and slicing
- Membership operators (`in`)
- Formatted strings (f-strings)
- Input validation
- `break` statement

## 📚 What I Learned

This exercise helps reinforce Python fundamentals by combining conditional logic, loops, string manipulation, and mathematical calculations in a practical application. It also provides experience interpreting user input, identifying units, and applying different formulas depending on the selected temperature scale.

## 🚀 Future Improvements

- Validate numerical input to prevent errors when users enter invalid values.
- Reject temperatures below absolute zero.
- Display conversion results rounded to two decimal places.
- Improve input validation to handle spaces and alternative formats.
- Refactor repeated menu code into reusable functions.
- Create separate functions for each temperature conversion.
- Improve the interface and organize the program for better readability.

---

*Part of my ongoing journey to strengthen my Python programming fundamentals and build a solid foundation for Artificial Intelligence, Machine Learning, and Software Engineering.*