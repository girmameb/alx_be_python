# polymorphism_demo.py

import math


class Shape:
    def area(self):
        """Abstract method for calculating the area. Derived classes should implement this."""
        raise NotImplementedError("Subclasses must implement the area() method.")


class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize a Rectangle instance with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return f"Rectangle(length={self.length}, width={self.width})"

    def __repr__(self):
        """Return an official string representation of the Rectangle."""
        return f"Rectangle({self.length}, {self.width})"


class Circle(Shape):
    def __init__(self, radius):
        """Initialize a Circle instance with radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2

    def __str__(self):
        """Return a string representation of the Circle."""
        return f"Circle(radius={self.radius})"

    def __repr__(self):
        """Return an official string representation of the Circle."""
        return f"Circle({self.radius})"


# Example usage
if __name__ == "__main__":
    # Create instances of Rectangle and Circle
    rectangle = Rectangle(5, 3)
    circle = Circle(4)

    # List of shapes
    shapes = [rectangle, circle]

    # Calculate and display the area for each shape
    for shape in shapes:
        print(f"{shape}: Area = {shape.area()}")

    # Print the official representations
    print("\nOfficial representations:")
    for shape in shapes:
        print(repr(shape))

