# Day 3 Mini Project - Even/Odd Checker

try:
    # Ask the user to enter a number
    number = int(input("Enter a number: "))

    # Check if the number is even or odd
    if number % 2 == 0:
        print(f"{number} is an Even number.")
    else:
        print(f"{number} is an Odd number.")

except ValueError:
    # Handle invalid input (like text instead of number)
    print("Invalid input! Please enter a valid integer.")
