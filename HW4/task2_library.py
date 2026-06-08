class Book:
    """Клас книги з property та операторами порівняння"""

    def __init__(self, title, author, pages):
        self._title = title
        self._author = author
        self._pages = pages

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title cannot be empty")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not value:
            raise ValueError("Author cannot be empty")
        self._author = value

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if value <= 0:
            raise ValueError("Pages must be positive")
        self._pages = value

    def __str__(self):
        return f'"{self._title}" by {self._author} ({self._pages} pages)'

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self._pages == other._pages

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self._pages < other._pages

    def __le__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self._pages <= other._pages

    def __gt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self._pages > other._pages

    def __ge__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self._pages >= other._pages

    def __ne__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self._pages != other._pages


class Library:
    """Бібліотека з перевантаженням операторів"""

    def __init__(self, name):
        self.name = name
        self._books = []

    def add_book(self, book):
        """Додає книгу до бібліотеки"""
        if not isinstance(book, Book):
            raise TypeError("Only Book instances can be added")
        self._books.append(book)

    def remove_book(self, book):
        """Видаляє книгу з бібліотеки"""
        if book in self._books:
            self._books.remove(book)
        else:
            raise ValueError("Book not found in library")

    def __iadd__(self, book):
        """Оператор += для додавання книги"""
        self.add_book(book)
        return self

    def __isub__(self, book):
        """Оператор -= для видалення книги"""
        self.remove_book(book)
        return self

    def __contains__(self, book):
        """Оператор in для перевірки наявності книги"""
        return book in self._books

    def __len__(self):
        """Повертає кількість книг"""
        return len(self._books)

    def __str__(self):
        if not self._books:
            return f"Library '{self.name}' is empty"
        books_list = "\n  ".join(str(book) for book in self._books)
        return f"Library '{self.name}' contains {len(self._books)} book(s):\n  {books_list}"


if __name__ == "__main__":
    print("=== Тестування Book ===")
    book1 = Book("1984", "George Orwell", 328)
    book2 = Book("Brave New World", "Aldous Huxley", 268)
    book3 = Book("Fahrenheit 451", "Ray Bradbury", 249)

    print(book1)
    print(book2)
    print(book3)

    print(f"\n{book1.title} > {book2.title}: {book1 > book2}")
    print(f"{book2.title} < {book1.title}: {book2 < book1}")
    print(f"{book3.title} == {book2.title}: {book3 == book2}")

    print("\n=== Тестування Library ===")
    library = Library("Міська бібліотека")
    print(library)

    print("\n--- Додавання книг через += ---")
    library += book1
    library += book2
    library.add_book(book3)
    print(library)

    print(f"\nКількість книг: {len(library)}")

    print(f"\n{book1.title} у бібліотеці: {book1 in library}")
    book4 = Book("The Hobbit", "J.R.R. Tolkien", 310)
    print(f"{book4.title} у бібліотеці: {book4 in library}")

    print("\n--- Видалення книги через -= ---")
    library -= book2
    print(library)
    print(f"Кількість книг: {len(library)}")
