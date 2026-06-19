class Doctor:
    """ lekarz pracujący w klinice"""

    def __init__(self, doctor_id: int, name: str, surname: str, specialization: str, phone: str) -> None:
        """Tworzy obiekt lekarza z podstawowymi danymi identyfikacyjnymi."""
        self.id = doctor_id
        self.name = name
        self.surname = surname
        self.specialization = specialization
        self.phone = phone

    def get_info(self) -> str:
    """ zwraca informacje o lekarzu w formie tekstowej """
        return (
            f"Dr {self.name} {self.surname}, "
            f"Specjalizacja: {self.specialization}, "
            f"Telefon: {self.phone}")

    def update_phone(self, new_phone: str) -> None:
        """Aktualizuje numer telefonu lekarza."""
        self.phone = new_phone