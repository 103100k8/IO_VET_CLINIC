class Doctor:
    """ lekarz pracujący w klinice"""
    def __init__(self, doctor_id: int, name: str, surname: str, specialization: str, phone: str) -> None:
        self.id = doctor_id
        self.name = name
        self.surname = surname
        self.specialization = specialization
        self.phone = phone

    """ zwraca informacje o lekarzu """
    def get_info(self) -> str:
        return (
            f"Dr {self.name} {self.surname}, "
            f"Specjalizacja: {self.specialization}, "
            f"Telefon: {self.phone}")