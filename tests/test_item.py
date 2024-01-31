"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("apple", 10, 20)
item2 = Item("potato", 5, 25)

def test_calculate_total_price():
    Item.pay_rate = 0.85

    item1.apply_discount()
    item2.apply_discount()
    assert item1.calculate_total_price() == 170.0
    assert item2.calculate_total_price() == 106.25