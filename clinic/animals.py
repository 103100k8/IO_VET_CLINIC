from datetime import date

class Animal:
    """Pacjent w gabinecie weterynaryjnym."""

    def __init__(self, name: str, species: str, breed: str, birth_date: date, owner_id: int) -> None:
        """
        DOC:
            name: Imię zwierzęcia(pacjenta) np.'Florek'
            species: Gatunek, np. 'pies'
            breed: Rasa, np. 'Labrador'
            birth_date: Data urodzenia, np. '10.06.2003'
            owner_id: ID właściciela zwierzęcia, np. '10657'
        """
        self.name = name
        self.species = species
        self.breed = breed
        self.birth_date = birth_date
        self.owner_id = owner_id
        self.medical_history: list[str] = []

    def age(self) -> int:
        """Wiek zwierzęcia w latach."""
        today = date.today()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )

    def add_medical_note(self, note: str) -> None:
        """Dodaje wpis do historii medycznej pacjenta"""
        self.medical_history.append(note)

    def __repr__(self) -> str:
        """Prezentacja obiektu"""
        return f"Animal(name={self.name!r}, species={self.species!r})"