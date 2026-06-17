class Doctor:
    """ lekarz pracujący w klinice"""

    """Tworzy obiekt lekarza z podstawowymi danymi identyfikacyjnymi."""
    def __init__(self, doctor_id: int, name: str, surname: str, specialization: str, phone: str) -> None:
        self.id = doctor_id
        self.name = name
        self.surname = surname
        self.specialization = specialization
        self.phone = phone

    """ zwraca informacje o lekarzu w formie tekstowej """
    def get_info(self) -> str:
        return (
            f"Dr {self.name} {self.surname}, "
            f"Specjalizacja: {self.specialization}, "
            f"Telefon: {self.phone}")

    """Aktualizuje numer telefonu lekarza."""
    def update_phone(self, new_phone: str) -> None:
        self.phone = new_phone