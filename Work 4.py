class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Животное: {self.name}")


class Mammal(Animal):
    def info(self):
        print(f"Млекопитающее: {self.name}")


class Ungulate(Mammal):
    def info(self):
        print(f"Копытные: {self.name}")


class Bird(Animal):
    def info(self):
        print(f"Птица: {self.name}")


class Country:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Страна: {self.name}")


class Republic(Country):
    def info(self):
        print(f"Республика: {self.name}")


class Monarchy(Country):
    def info(self):
        print(f"Монархия: {self.name}")


class Kingdom(Monarchy):
    def info(self):
        print(f"Королевство: {self.name}")


# Пример использования:
lion = Ungulate("Лев")
eagle = Bird("Орёл")
usa = Republic("США")
uk = Kingdom("Великобритания")

lion.info()  # Ungulate: Lion
eagle.info()  # Bird: Eagle
usa.info()  # Republic: USA
uk.info()  # Kingdom: UK
