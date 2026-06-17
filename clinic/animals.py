from datetime import date

class Animal:
    """Reprezentuje zwierzę pacjenta w gabinecie weterynaryjnym."""

    def __init__(self, name: str, species: str, breed: str, birth_date: date, owner_id: int) -> None:
        """
        Args:
            name: Imię pacjenta
            species: Gatunek (np.'kot')
            breed: Rasa
            birth_date: Data urodzenia
            owner_id: ID właściciela
        """
        self.name = name
        self.species = species
        self.breed = breed
        self.birth_date = birth_date
        self.owner_id = owner_id
        self.medical_history: list[str] = []

    def age(self) -> int:
        """Zwraca wiek zwierzęcia w latach"""
        today = date.today()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )

    def add_medical_note(self, note: str) -> None:
        """Dodaje wpis do historii medycznej"""
        self.medical_history.append(note)

    def __repr__(self) -> str:
        """Zwraca podstawowe informacje charakterystyczne o zwierzęciu tzn imię i gatunek"""
        return f"Animal(name={self.name!r}, species={self.species!r})"