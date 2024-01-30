"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture()
def laptop():
    return Item("Телефон", 10000, 20)


def test_calculate_total_price(laptop):
    assert laptop.calculate_total_price() == 200000


def test_apply_discount(laptop):
    laptop.pay_rate = 0.8
    laptop.apply_discount()
    assert laptop.price == 8000.0


def test_name(laptop):
    laptop.name = 'Смартфон'
    assert laptop.name == 'Смартфон'
    laptop.name = 'СуперСмартфон'
    assert laptop.name == 'СуперСмарт'


def test_instantiate_from_csv(laptop):
    laptop.instantiate_from_csv('src/items.csv')
    assert len(laptop.all) == 5


def test_string_to_number(laptop):
    assert laptop.string_to_number('5') == 5
    assert laptop.string_to_number('5.0') == 5
    assert laptop.string_to_number('5.5') == 5


def test_repr(laptop):
    laptop.name = 'Смартфон'
    assert repr(laptop) == "Item('Смартфон', 10000, 20)"


def test_str():
    laptop.name = 'Смартфон'
    assert str(laptop.name) == 'Смартфон'


