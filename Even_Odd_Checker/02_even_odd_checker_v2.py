# ============================
# Day 3 - Even/Odd Checker
# Author: Faiz Ur Rehman Ashrafi
# ============================


# Function to check whether number is even/odd & positive/negative/zero
def checker(number):
    """Check the type of number and return description"""
    if number == 0:
        return "Zero (Even)"  # Special case
    elif number % 2 == 0:  # Even numbers
        return "Positive Even" if number > 0 else "Negative Even"
    else:  # Odd numbers
        return "Positive Odd" if number > 0 else "Negative Odd"


# Function to validate input and add to numbers list
def check(number):
    """Validate input and store in global list 'numbers'"""
    try:
        numbers.append(int(number))  # Convert input to integer
    except ValueError:
        return "Value Error"  # If input is not a valid integer


# Function to handle multiple numbers input
def multiple():
    """Take multiple numbers until user enters 'q'"""
    while True:
        number = input("Enter number (or 'q' to stop): ")
        if number.lower() == "q":  # Exit condition
            break
        if check(number) == "Value Error":  # Invalid input
            print("Invalid Input! Only integers allowed.")


# Function to handle single number input
def single():
    """Take only one number"""
    number = input("Enter a number: ")
    if check(number) == "Value Error":  # Validate input
        print("Invalid Input! Only integers allowed.")
        return
    return "break"  # Return break signal after one input


# Function to show results of checked numbers
def show_result(numbers):
    """Display results of all stored numbers"""
    if not numbers:  # If list is empty
        print("Empty!")
    else:
        for i, number in enumerate(numbers, start=1):  # Loop with index
            print(f"{i}. Number: {number} → {checker(number)}")


# Function to handle user choice: single or multiple
def batch_func(batch):
    """Decide execution mode: single or multiple"""
    if batch == 1:
        single()
        show_result(numbers)
        return "break"
    elif batch == 2:
        multiple()
        show_result(numbers)
        return "break"


# ============================
# Main Program Execution
# ============================

numbers = []  # Global list to store all inputs
batch = int(input("1. Check Single Number\n2. Check Multiple Numbers\nSelect Option: "))


def run():
    """Main loop to run batch function until user quits"""
    while True:
        result = batch_func(batch)
        if result == "break":
            break  # Exit once user finishes input


# Run the program once
run()

# Ask user if they want to repeat
repeat = input("Do you want to check again? (y/n): ")
if repeat.lower() == "y":
    run()
else:
    print("Thanks for using me. Exiting...")
