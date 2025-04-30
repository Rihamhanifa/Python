# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

# Main function to get user input and perform the calculation
def calculator():
    # Ask the user for two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Ask the user to choose an operation
    operation = input("Choose an operation: +, -, *, /: ")
    
    # Call the appropriate function based on the user's choice
    if operation == "+":
        print(f"The result is: {add(num1, num2)}")
    elif operation == "-":
        print(f"The result is: {subtract(num1, num2)}")
    elif operation == "*":
        print(f"The result is: {multiply(num1, num2)}")
    elif operation == "/":
        print(f"The result is: {divide(num1, num2)}")
    else:
        print("Invalid operation!")

# Call the calculator function
calculator()
