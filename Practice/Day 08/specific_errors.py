# TRY running the code
try:

    # Ask user for a number
    number = int(input("Enter a number: "))

    # Divide 100 by the number
    result = 100 / number

    # Print result
    print("Result:", result)

# Handle invalid number input
except ValueError:

    print("Please enter a valid number.")

# Handle division by zero
except ZeroDivisionError:

    print("Cannot divide by zero.")