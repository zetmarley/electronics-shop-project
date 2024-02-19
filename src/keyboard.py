from src.item import Item

class MixinLang:
    def __init__(self, language='EN'):
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'RU':
            self.__language = 'EN'
        else:
            self.__language = 'RU'

class Keyboard(Item, MixinLang):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
