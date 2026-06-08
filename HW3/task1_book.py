class Book:
    def __init__(self, title, author, pages):
        self._title = title
        self._author = author
        self._pages = pages

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def pages(self):
        return self._pages

    # Сетери
    @title.setter
    def title(self, value):
        self._title = value

    @author.setter
    def author(self, value):
        self._author = value

    @pages.setter
    def pages(self, value):
        if value > 0:
            self._pages = value
        else:
            print("Кількість сторінок має бути додатньою!")

    def display_info(self):
        print(f"Назва: {self._title}")
        print(f"Автор: {self._author}")
        print(f"Кількість сторінок: {self._pages}")

    def is_long_book(self):
        return self._pages > 300


if __name__ == "__main__":
    book1 = Book("Гаррі Поттер і філософський камінь", "Дж. К. Роулінг", 320)
    book1.display_info()
    print(f"Це довга книга? {book1.is_long_book()}")
    print()

    book2 = Book("Маленький принц", "Антуан де Сент-Екзюпері", 96)
    book2.display_info()
    print(f"Це довга книга? {book2.is_long_book()}")
