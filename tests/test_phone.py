import pytest
from src.phone import Phone


@pytest.fixture()
def Phone_():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_number_of_sim(Phone_):
    assert Phone_.number_of_sim == 2
    Phone_.number_of_sim = 1
    assert Phone_.number_of_sim == 1
    Phone_.number_of_sim = 0


def test_repr(Phone_):
    assert repr(Phone_) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str(Phone_):
    assert str(Phone_.name) == "iPhone 14"