from clinic.doctors import Doctor

def test_create_doctor():
    """Sprawdzamy, czy obiekt Doctor tworzy się poprawnie z podanymi danymi."""
    # tworzymy przykładowego lekarza
    d = Doctor(
        doctor_id=1,
        name="Kasia",
        surname="Kowalska",
        specialization="chirurgia",
        phone="882-123-456"
    )
    # sprawdzamy, czy pola zostały ustawione poprawnie
    assert d.id == 1
    assert d.name == "Kasia"
    assert d.surname == "Kowalska"
    assert d.specialization == "chirurgia"
    assert d.phone == "882-123-456"

def test_get_info():
    """Testuje metodę get_info(), która zwraca informacje o lekarzu."""

    # tworzymy lekarza
    d = Doctor(
        doctor_id=2,
        name="Jan",
        surname="Nowak",
        specialization="dermatologia",
        phone="100-200-300"
    )
    # oczekiwany tekst
    expected = "Dr Jan Nowak, Specjalizacja: dermatologia, Telefon: 100-200-300"

    # sprawdzamy, czy metoda zwraca poprawny string
    assert d.get_info() == expected

def test_update_phone():
    """Testuje aktualizację numeru telefonu lekarza."""

    # tworzymy lekarza z początkowym numerem
    d = Doctor(
        doctor_id=3,
        name="Alicja",
        surname="Zielińska",
        specialization="chirurgia",
        phone="111-222-333"
    )

    # zmieniamy numer telefonu
    d.update_phone("999-888-777")
    # sprawdzamy, czy numer został zaktualizowany
    assert d.phone == "999-888-777"