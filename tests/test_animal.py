from clinic.animals import Animal
from datetime import date

def test_animal_id_auto_increment():
    Animal.reset_id_counter()

    burek = Animal('Burek', 'pies', 'Labrador', date(2018, 5, 10), 1)
    rudy = Animal("Rudy", "kot", "dachowy", date(2021, 2, 2), 1)

    assert burek.animal_id == 1
    assert rudy.animal_id == 2

def test_animal_age_calculation():
    Animal.reset_id_counter()

    burek = Animal('Burek', 'pies', 'Labrador', date(2018, 5, 10), 1)
    assert burek.age() >= 0

def test_animal_repr_contains_data():
    Animal.reset_id_counter()

    burek = Animal('Burek', 'pies', 'Labrador', date(2018, 5, 10), 1)
    rep = repr(burek)

    assert "Burek" in rep
    assert "pies" in rep


