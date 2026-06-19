from datetime import date
from clinic.appointments import Appointment

def test_create_appointment():
    """Sprawdzamy, czy obiekt Appointment tworzy się poprawnie z podstawowymi danymi."""

    # przykładowe dane
    a = Appointment(
        animal_id=1,
        doctor_id=2,
        visit_date=date(2024, 1, 1),
        symptoms="brak apetytu"
    )

    # Sprawdzamy, czy pola zostały ustawione poprawnie
    assert a.animal_id == 1
    assert a.doctor_id == 2
    assert a.visit_date == date(2024, 1, 1)
    assert a.symptoms == "brak apetytu"

    # Sprawdzamy wartości domyślne
    assert a.diagnosis == ""
    assert a.treatment == ""
    assert a.weight is None


def test_add_diagnosis():
    """Testuje metodę dodającą diagnozę do wizyty."""
   # tworzymy przykładową wizytę
    a = Appointment(
        animal_id=1,
        doctor_id=2,
        visit_date=date.today()
    )
    #dodajemy diagnozę
    a.add_diagnosis("zapalenie gardła")

    # Sprawdzamy, czy diagnoza została poprawnie zapisana
    assert a.diagnosis == "zapalenie gardła"

def test_add_treatment():
    """Testuje metodę ustawiającą leczenie dla wizyty."""

    # tworzymy przykładową wizytę
    a = Appointment(
        animal_id=1,
        doctor_id=2,
        visit_date=date.today()
    )
    # dodajemy leczenie
    a.add_treatment("antybiotyk")

    # Sprawdzamy, czy diagnoza została poprawnie zapisana
    assert a.treatment == "antybiotyk"