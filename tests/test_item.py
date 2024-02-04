"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("apple", 10, 20)
item2 = Item("potato", 5, 25)

def test_calculate_total_price():
    """homework1"""
    Item.pay_rate = 0.85

    item1.apply_discount()
    item2.apply_discount()
    assert item1.calculate_total_price() == 170.0
    assert item2.calculate_total_price() == 106.25

def test_name():
    """homework2"""
    assert item1.name == "apple"
    item1.name = "appleappleapple"
    assert item1.name == "appleapple"

def test_csv():
    """homework2"""
    Item.instantiate_from_csv()

    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

def test_string_to_number():
    """homework2"""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_repr_str():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'