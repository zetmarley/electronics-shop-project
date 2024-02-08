from src.item import Item
from src.phone import Phone

item1 = Item("apple", 10, 20)
item2 = Item("potato", 5, 25)
phone1 = Phone("Iphone 15", 90000, 50, 1)
phone2 = Phone("Samsung", 40000, 50, 2)

def test_Phone():
    assert str(phone1) == "Iphone 15"
    assert repr(phone1) == "Phone('Iphone 15', 90000, 50, 1)"

    assert item1 + phone1 == 70
    assert phone1 + phone2 == 100

    assert phone2.number_of_sim == 2