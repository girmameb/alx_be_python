def perform_operation(num1: float, num2: float, operation: str) -> float:
    """
    Performs arithmetic operations on two numbers.

    Args:
        num1 (float): First operand.
        num2 (float): Second operand.
        operation (str): Operation to perform ('add', 'subtract', 'multiply', or 'divide').

    Returns:
        float: Result of the arithmetic operation.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Error: Division by zero"

# Example usage:
result = perform_operation(10.0, 5.0, 'add')
print(f"Result: {result}")
