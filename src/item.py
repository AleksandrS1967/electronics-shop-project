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
        if path == 'д':
            p = 'src/items.csv'
        else:
            p = f'../{path}'
        with open(p, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            cls.all = []
            for row in reader:
                Item(row['name'], int(row['price']), int(row['quantity']))

    @staticmethod
    def string_to_number(str_):
        """
        Статический метод, возвращающий число из числа-строки
        """
        return int(float(str_[0]))

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
