# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Initialize a new Book instance with title, author, and publication year."""
        self.title = title
        self.author = author
        self.year = year
       # print(f"Book created: {self}")

    def __del__(self):
        """Print a message when the Book object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a human-readable string representation of the Book object."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return an official string representation of the Book object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

# Example usage:
if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", 1949)
    print(book1)  # Should use __str__ method
    print(repr(book1))  # Should use __repr__ method

    # Delete the object to trigger the __del__ method
    del book1

