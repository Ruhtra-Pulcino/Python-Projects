"""
Exercise: ATM Simulation

Objective: Develop a Python program that simulates the
basic operations of an ATM. The user must be able to
check the balance, deposit money, withdraw money, and exit the program.

Requirements:

Check Balance:

- Upon selecting this option, the program must display the current account balance.

Deposit Money:

- The user must be able to enter an amount to deposit into the account.
- The amount must be positive.
- After a successful deposit, the account balance must be updated and a
confirmation message must be displayed.

Withdraw Money:

- The user must be able to enter an amount to withdraw from the account.
- The amount must be positive and must not exceed the current balance.
- After a successful withdrawal, the account balance must be
updated and a confirmation message must be displayed.

Exit:

- The user must be able to exit the program by choosing this option. 

Input Validation:

- The program must handle invalid inputs appropriately, displaying error messages when applicable. 

User Interface:

- The program must display a menu of options to the user and allow
the selection of actions to be performed. 
- The menu options must be presented within a loop, allowing
multiple operations until the user chooses to exit. 

ATM
1 - Check Balance
2 - Deposit Money
3 - Withdraw Money
4 - Exit
Choose an option (1-4):

Initial Balance:

- The account must start with an initial balance of R$ 1000.00.

Instructions:

- Start by initializing the balance and entering a loop that displays the options menu. 
- Implement each operation as described in the requirements. 
- Make sure to test all options and possible scenarios to ensure
the program works correctly.


Tip: You can use `if`, `elif`, and `else` statements along with a `while` loop
to handle user selections and keep the program running
until the exit option is chosen.

"""