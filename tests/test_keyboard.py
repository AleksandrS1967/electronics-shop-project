import pytest
from src.keyboard import Keyboard


@pytest.fixture()
def keyboard_():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_language(keyboard_):
    assert str(keyboard_.name) == "Dark Project KD87A"
    assert str(keyboard_.language) == "EN"


def test_change_lang(keyboard_):
    keyboard_.change_lang()
    assert str(keyboard_.language) == "RU"
    keyboard_.change_lang()
    assert str(keyboard_.language) == "EN"


