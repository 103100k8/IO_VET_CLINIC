from datetime import date

class Animal:
    """Reprezentuje zwierzę pacjenta w gabinecie weterynaryjnym."""

    _id_counter = 1

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
        self.animal_id = Animal._id_counter
        Animal._id_counter += 1

    @classmethod
    def reset_id_counter(cls) -> None:
        cls._id_counter = 1

    def age(self) -> int:
        """Zwraca wiek zwierzęcia w latach"""
        today = date.today()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )

    def __repr__(self) -> str:
        """Zwraca podstawowe informacje charakterystyczne o zwierzęciu tzn imię i gatunek"""
        return f"Animal(id={self.animal_id}, name={self.name!r}, species={self.species!r})"