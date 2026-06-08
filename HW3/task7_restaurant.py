class Dish:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_description(self):
        return f"{self.name} ({self.category}) - {self.price} грн"


class Order:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)
        print(f"Страву '{dish.name}' додано до замовлення.")

    def remove_dish(self, dish_name):
        for dish in self.dishes:
            if dish.name == dish_name:
                self.dishes.remove(dish)
                print(f"Страву '{dish_name}' видалено з замовлення.")
                return
        print(f"Страву '{dish_name}' не знайдено в замовленні.")

    def get_total(self):
        return sum(dish.price for dish in self.dishes)

    def display_order(self):
        if not self.dishes:
            print("Замовлення порожнє.")
            return
        print("\nВаше замовлення:")
        for dish in self.dishes:
            print(f"  - {dish.get_description()}")
        print(f"Загальна сума: {self.get_total()} грн")


class Restaurant:
    def __init__(self):
        self.menu = []

    def add_dish_to_menu(self, dish):
        self.menu.append(dish)
        print(f"Страву '{dish.name}' додано до меню.")

    def display_menu(self):
        if not self.menu:
            print("Меню порожнє.")
            return
        print("\n=== МЕНЮ РЕСТОРАНУ ===")
        categories = {}
        for dish in self.menu:
            if dish.category not in categories:
                categories[dish.category] = []
            categories[dish.category].append(dish)

        for category, dishes in categories.items():
            print(f"\n{category}:")
            for dish in dishes:
                print(f"  {dish.get_description()}")


# Приклад використання
if __name__ == "__main__":
    restaurant = Restaurant()

    restaurant.add_dish_to_menu(Dish("Борщ", 85, "Перші страви"))
    restaurant.add_dish_to_menu(Dish("Солянка", 95, "Перші страви"))
    restaurant.add_dish_to_menu(Dish("Котлета по-київськи", 150, "Основні страви"))
    restaurant.add_dish_to_menu(Dish("Варениці з вишнею", 70, "Десерти"))

    restaurant.display_menu()

    order = Order()
    order.add_dish(restaurant.menu[0])  # Борщ
    order.add_dish(restaurant.menu[2])  # Котлета
    order.add_dish(restaurant.menu[3])  # Варениці
    order.display_order()

    order.remove_dish("Борщ")
    order.display_order()
