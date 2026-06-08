class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def reset(self):
        self.count = 0

    def get_value(self):
        return self.count


if __name__ == "__main__":
    counter = Counter()
    print(f"Початкове значення: {counter.get_value()}")

    counter.increment()
    counter.increment()
    counter.increment()
    print(f"Після 3 інкрементів: {counter.get_value()}")

    counter.decrement()
    print(f"Після декременту: {counter.get_value()}")

    counter.reset()
    print(f"Після скидання: {counter.get_value()}")
