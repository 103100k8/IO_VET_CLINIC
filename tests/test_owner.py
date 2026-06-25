from clinic.owners import Owner


def test_create_owner():
    """Sprawdza, czy obiekt Owner tworzy się w poprawny sposób z podanymi danymi."""
    # stworzenie testowego właściciela
    o = Owner(
        owner_id=1,
        first_name="Marek",
        last_name="Świderek",
        phone="321 123 456",
        email="markomarek5@sztosik.com"
    )
    # sprawdzenie poprawnego ustawienia pól (oczekiwany wynik)
    assert o.owner_id == 1
    assert o.first_name == "Marek"
    assert o.last_name == "Świderek"
    assert o.phone == "321 123 456"
    assert o.email == "markomarek5@sztosik.com"
    assert o.animals == []


def test_full_name():
    """Testuje metodę full_name(), która zwraca imię i nazwisko właściciela."""
    # tworzymy testowego właściciela
    o = Owner(
        owner_id=2,
        first_name="Maja",
        last_name="Ślimak",
        phone="123 321 456",
        email="majaslimak@pokemonik1.com"
    )
    # sprawdzenie poprawnego ustawienia pól (oczekiwany wynik)
    expected = "Maja Ślimak"

    # sprawdzenie, czy metoda zwraca poprawny string
    assert o.full_name() == expected


def test_register_animal():
    """Sprawdza poprawność rejestracji zwierzęcia u właściciela."""
    # tworzymy właściciela bez zwierzątka
    o = Owner(
        owner_id=3,
        first_name="Kasia",
        last_name="Ceglasia",
        phone="111 222 333",
        email="katcegl@pokemonik2.com"
    )
    # rejestracja zwierzęcia
    o.register_animal("Biszkopcik")

    # sprawdzenie poprawności dodania zwierzęcia do listy
    assert o.animals == ["Biszkopcik"]


def test_register_multiple_animals():
    """Sprawdza poprawność rejestracji KILKU zwierząt u jednego właściciela."""
    o = Owner(4, "Marek", "Świderek", "321 123 456", "markomarek5@sztosik.com")
    # rejestrujemy dwa zwierzęta
    o.register_animal("Borysek")
    o.register_animal("Krokiecik")

    # sprawdzenie czy obie nazwy są dodane do listy w odpowiedniej kolejności
    assert o.animals == ["Borysek", "Krokiecik"]


def test_owner_repr():
    owner = Owner(1, "Maja", "Ślimak", "002", "majaslimak@pokemonik1.com")
    rep = repr(owner)
    assert "Owner" in rep
    assert "Maja Ślimak" in rep