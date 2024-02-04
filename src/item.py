import csv

class Item:
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
    def instantiate_from_csv(cls):
        """Инициализируем содержимое items.csv"""
        count = 1
        with open("src/items.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Item.all.append(Item(row["name"], row["price"], row["quantity"]))

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