"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture()
def laptop():
    return Item("laptop", 10000, 20)


def test_calculate_total_price(laptop):
    assert laptop.calculate_total_price() == 200000


def test_apply_discount(laptop):
    laptop.pay_rate = 0.8
    if laptop.apply_discount() != None:
        assert laptop.apply_discount() == 8000.0
