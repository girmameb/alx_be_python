# library_system.py

class Book:
    def __init__(self, title, author):
        """Initialize a Book instance with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the Book."""
        return f"Book: {self.title} by {self.author}"

    def __repr__(self):
        """Return an official string representation of the Book."""
        return f"Book('{self.title}', '{self.author}')"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize an EBook instance with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of the EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

    def __repr__(self):
        """Return an official string representation of the EBook."""
        return f"EBook('{self.title}', '{self.author}', {self.file_size})"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize a PrintBook instance with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of the PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, {self.page_count} pages"

    def __repr__(self):
        """Return an official string representation of the PrintBook."""
        return f"PrintBook('{self.title}', '{self.author}', {self.page_count})"


class Library:
    def __init__(self):
        """Initialize an empty library."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)


# Example usage
if __name__ == "__main__":
    # Create instances of books
    ebook1 = EBook("Digital Fortress", "Dan Brown", 2)
    printbook1 = PrintBook("The Catcher in the Rye", "J.D. Salinger", 277)

    # Create a Library instance
    library = Library()

    # Add books to the library
    library.add_book(ebook1)
    library.add_book(printbook1)

    # List books in the library
    library.list_books()

