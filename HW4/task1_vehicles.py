class Engine:
    """Базовий клас для керування двигуном"""

    def start_engine(self):
        print("Engine started")

    def stop_engine(self):
        print("Engine stopped")


class Vehicle:
    """Базовий клас з властивостями транспорту"""

    def __init__(self, max_speed):
        self.max_speed = max_speed

    def drive(self):
        print(f"Driving at maximum speed of {self.max_speed}")


class Car(Engine, Vehicle):
    """Клас автомобіля"""

    def __init__(self, model, max_speed):
        Vehicle.__init__(self, max_speed)
        self.model = model

    def drive(self):
        print(f"Car {self.model} is driving at {self.max_speed}")


class Boat(Engine, Vehicle):
    """Клас човна"""

    def __init__(self, boat_type, max_speed):
        Vehicle.__init__(self, max_speed)
        self.type = boat_type

    def drive(self):
        print(f"Boat of type {self.type} is sailing at {self.max_speed}")


class AmphibiousVehicle(Car, Boat):
    """Амфібія - транспорт для суші та води"""

    def __init__(self, model, boat_type, max_speed, is_on_land=True):
        Car.__init__(self, model, max_speed)
        self.type = boat_type
        self.is_on_land = is_on_land

    def drive(self):
        if self.is_on_land:
            Car.drive(self)
        else:
            Boat.drive(self)


if __name__ == "__main__":
    print("=== Тестування Car ===")
    car = Car("Tesla Model S", 250)
    car.start_engine()
    car.drive()
    car.stop_engine()

    print("\n=== Тестування Boat ===")
    boat = Boat("моторний", 80)
    boat.start_engine()
    boat.drive()
    boat.stop_engine()

    print("\n=== Тестування AmphibiousVehicle ===")
    amphibious = AmphibiousVehicle("Amphicar", "моторний", 120, is_on_land=True)
    amphibious.start_engine()
    print("На суші:")
    amphibious.drive()

    amphibious.is_on_land = False
    print("На воді:")
    amphibious.drive()
    amphibious.stop_engine()
