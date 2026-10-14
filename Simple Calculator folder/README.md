# Simple Calculator with `while` Loops

## 📌 About the Project

This project is a Python exercise focused on practicing **conditional statements**, `while` loops, arithmetic operations, and user input.

The program implements a simple terminal-based calculator that allows users to perform addition, subtraction, multiplication, and division. It supports both integers and decimal numbers, validates menu selections, and prevents division by zero.

## 🎯 Objectives

- Practice `while` loops to create a continuous interactive menu.
- Use `if`, `elif`, and `else` statements to handle different operations.
- Perform arithmetic operations using Python operators.
- Work with user input using `input()`.
- Convert strings into integers and floating-point numbers.
- Use conditional statements to distinguish between integer and decimal inputs.
- Validate menu selections to prevent invalid options.
- Handle division by zero to avoid invalid mathematical operations.
- Control program execution using the `break` statement.

## ⚙️ How It Works

1. The program displays a menu with five options: Sum, Subtraction, Multiplication, Division, and Exit.
2. The user selects an operation by entering the corresponding number.
3. The program requests two numbers for the selected arithmetic operation.
4. Each number is converted to an integer or a floating-point number depending on whether its input contains a decimal point.
5. The selected arithmetic operation is performed, and the result is displayed in the terminal.
6. Before division, the program checks whether the second number is zero and displays an error message if division is not possible.
7. If the user enters an invalid menu option, the program displays an error message.
8. The menu repeats until the user selects the exit option, which terminates the loop.

## 🛠️ Technologies

- **Python 3**
- `while` loops
- `if`, `elif`, and `else` statements
- Arithmetic operators (`+`, `-`, `*`, `/`)
- Variables and data types (`int` and `float`)
- User input with `input()`
- String operations and the `in` operator
- Formatted strings (f-strings)
- Input validation
- `break` statement

## 📚 What I Learned

This exercise helps reinforce the fundamentals of Python programming by combining loops, conditional logic, data type conversion, and arithmetic operations. It also provides practical experience handling different numerical inputs and implementing basic error prevention, such as checking for division by zero.

## 🚀 Future Improvements

- Handle non-numeric inputs without crashing the program.
- Reduce code repetition by reusing the number input and conversion logic.
- Use functions to organize each arithmetic operation.
- Improve decimal number validation.
- Handle negative numbers and different decimal formats.
- Display integer results without unnecessary decimal places when appropriate.
- Add additional operations, such as exponentiation, square roots, and percentages.

---

*Part of my ongoing journey to strengthen my Python programming fundamentals and build a solid foundation for Artificial Intelligence, Machine Learning, and Software Engineering.*
