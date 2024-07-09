# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Performs arithmetic operations on two numbers based on the operation specified.

    Parameters:
    - num1 (float): The first number for the operation.
    - num2 (float): The second number for the operation.
    - operation (string): The operation to be performed. Can be 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
    - float or str: Result of the arithmetic operation or an error message.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Division by zero is not allowed"
        else:
            return num1 / num2
    else:
        return "Invalid operation"
