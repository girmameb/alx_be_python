# library_management.py

class Book:
    """Represents a book in the library with a title, author, and availability status."""

    def __init__(self, title, author):
        """Initialize the Book with a title, author, and set the checked-out status to False."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Check out the book. Returns True if successful, False if the book is already checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book. Returns True if successful, False if the book was not checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_checked_out(self):
        """Check if the book is checked out."""
        return self._is_checked_out

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"

class Library:
    """Represents a library with a collection of books."""

    def __init__(self):
        """Initialize the Library with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title. Returns True if successful, False if the book is not available."""
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False

    def return_book(self, title):
        """Return a book by title. Returns True if successful, False if the book was not checked out."""
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if not book.is_checked_out()]
        for book in available_books:
            print(book)

    def __str__(self):
        """Return a string representation of the library."""
        return '\n'.join(str(book) for book in self._books)

