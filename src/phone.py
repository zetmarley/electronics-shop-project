from src.item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim):
        super().__init__(name, price, quantity)
        if number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number):
        if new_number > 0:
            self.__number_of_sim = new_number
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")