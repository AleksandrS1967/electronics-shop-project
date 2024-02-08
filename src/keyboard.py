from src.item import Item


class MixinLog:
    """ дополнительный функционал по хранению и
        изменению раскладки клавиатуры в отдельном классе-миксине,
        который “подмешивается” в цепочку наследования класса Keyboard
    """
    def __init__(self):
        self._language = "EN"

    def change_lang(self):
        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"

    @property
    def language(self):
        return self._language


class Keyboard(Item, MixinLog):
    pass

