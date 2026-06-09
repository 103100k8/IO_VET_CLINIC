from datetime import date

class Animal:
    "Pacjent gabinetu weterynaryjnego"

    def __init__(self, name: str, species: str, breed: str, birth_date: date, owner_id: int) -> None:
        self.name = name
        self.species = species
        self.breeed = breed
        self.birth_date = birth_date
        self.owner_id = owner_id
        self.medical_history: list[str]=[]

    def age(self) -> int:
        """Wiek zwierzęcia w latach"""
        today = date.today()
        return today.year - self.birth_date.year - (
        (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
    )

    def add_medical_note(self, note: str) -> None:
        "Wpis do historii medycznej pacjenta"
        self.medical.history.append(note)

    def __repr__(self) -> str:
        return f"Patient (name={self.name!r}, species ={self.species!r})"    