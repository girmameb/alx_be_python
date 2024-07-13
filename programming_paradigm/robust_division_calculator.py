# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Perform division with error handling."""
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        # Perform division
        result = num / denom
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result:.2f}"

