# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method to return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method to return the product of two numbers and print the class attribute calculation_type."""
        print(f"Calculation Type: {cls.calculation_type}")
        return a * b


# Example usage
if __name__ == "__main__":
    # Using the static method to add two numbers
    sum_result = Calculator.add(5, 3)
    print(f"Sum: {sum_result}")  # Output: Sum: 8

    # Using the class method to multiply two numbers
    product_result = Calculator.multiply(4, 7)
    print(f"Product: {product_result}")  # Output: Product: 28

