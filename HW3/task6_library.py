class Book:
    def __init__(self, title, author, pages, book_id):
        self.title = title
        self.author = author
        self.pages = pages
        self.book_id = book_id

    def display_info(self):
        print(f"ID: {self.book_id}")
        print(f"Назва: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Кількість сторінок: {self.pages}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Книгу '{book.title}' додано до бібліотеки.")

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"Книгу з ID {book_id} видалено з бібліотеки.")
                return
        print(f"Книгу з ID {book_id} не знайдено.")

    def search_book(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if found_books:
            print(f"\nЗнайдено {len(found_books)} книг(и):")
            for book in found_books:
                book.display_info()
                print()
        else:
            print(f"Книгу з назвою '{title}' не знайдено.")


# Приклад використання
if __name__ == "__main__":
    library = Library()

    book1 = Book("Кобзар", "Тарас Шевченко", 240, 1)
    book2 = Book("Тіні забутих предків", "Михайло Коцюбинський", 120, 2)
    book3 = Book("Захар Беркут", "Іван Франко", 180, 3)

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    library.search_book("Кобзар")
    library.remove_book(2)
    library.search_book("Тіні")
