import csv
import os


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
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        """
        Проверяет, что длина наименования товара не больше 10 симвовов.
        В противном случае,
        обрезать строку (оставить первые 10 символов)
        """
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls, path):
        """
        Класс-метод, инициализирующий экземпляры класса `Item`
        данными из файла _src/items.csv_
        """
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            cls.all = []
            for row in reader:
                Item(row['name'], cls.string_to_number(float(row['price'])), cls.string_to_number(row['quantity']))

    @staticmethod
    def string_to_number(str_):
        """
        Статический метод, возвращающий число из числа-строки
        """
        if isinstance(str_, float):
            return float(str_)
        else:
            return int(float(str_))

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
        self.price *= self.pay_rate

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        return 'TypeError'