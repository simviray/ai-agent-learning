# Function to greet a user
def greet_user(name):

    # Print greeting message
    print(f"Welcome, {name}")

# Function to calculate BTC tax estimate
def calculate_tax(amount):

    # Calculate 10% sample tax
    tax = amount * 0.10

    # Return the calculated value
    return tax

# Call greeting function
greet_user("Simeon")

# Call tax function
result = calculate_tax(5000)

# Print returned value
print("Estimated Tax:", result)