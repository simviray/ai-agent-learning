# TRY means attempt to run the code
try:

    # Ask user for a number
    number = int(input("Enter a number: "))

    # Print the number
    print("You entered:", number)

# EXCEPT runs if an error happens
except:

    # Print friendly error message
    print("Invalid input. Please enter a valid number.")