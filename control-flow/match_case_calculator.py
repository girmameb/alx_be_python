# Prompt user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask for operation choice
operation = input("Choose the operation (+, -, *, /): ")

# Perform calculation based on operation chosen
match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            result = None
    case _:
        print(f"Error: '{operation}' is not a valid operation.")

# Output the result
if result is not None:
    print(f"The result is {result}.")
