from src.item import Item

class Keyboard(Item):
    def __init__(self,name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'RU':
            self.__language = 'EN'
        else:
            self.__language = 'RU'