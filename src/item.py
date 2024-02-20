import csv
from abc import ABC

class InstantiateCSVError(KeyError):
    def __init__(self, *args):
        self.message = "Файл item.csv поврежден"

    def __str__(self):
        return self.message

class Item(ABC):
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if issubclass(self.__class__, other.__class__) or issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity

    @property
    def name(self):
        """Геттер name"""
        return self.__name

    @name.setter
    def name(self, name):
        """Сеттер name"""
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, path='../src/items.csv'):
        """Инициализируем содержимое items.csv"""
        try:
            with open(path, encoding='utf-8', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    Item.all.append(Item(row["name"], int(row["price"]), int(row["quantity"])))
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')
        except ValueError:
            raise InstantiateCSVError


    @staticmethod
    def string_to_number(number):
        """Преобразуем строчку в целые числа"""
        return int(float(number))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate