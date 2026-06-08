class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height


if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(f"Прямокутник {rect.width}x{rect.height}")
    print(f"Площа: {rect.area()}")
    print(f"Периметр: {rect.perimeter()}")
    print(f"Це квадрат? {rect.is_square()}")
    print()

    square = Rectangle(7, 7)
    print(f"Прямокутник {square.width}x{square.height}")
    print(f"Площа: {square.area()}")
    print(f"Периметр: {square.perimeter()}")
    print(f"Це квадрат? {square.is_square()}")
