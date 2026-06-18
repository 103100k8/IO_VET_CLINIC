from datetime import date

class MedicalRecord:
    """historia medyczna zwierzecia w klinice"""

    def __init__(self, animal_id: int) -> None:
        """
        Args: 
        animal_id: identyfikator zwierzecia, którego dotyczy historia
        """

        self.animal_id = animal_id
        self.diseases: list[str] = []
        self.vaccinations: list[str] = []
        self.notes: list[str] = []

    def add_disease(self, name: str, diagnosed_date: date | None = None) -> None:
        """dodaje chorobe do historii medycznej zwierzęcia"""
        if diagnosed_date is None:
            diagnosed_date = date.today()
        self.diseases.append(f"{name} ({diagnosed_date})")
    
    def add_vaccination(self, name: str, vaccination_date: date | None = None) -> None:
        """dodaje chorobe do hisrotii zwierzęcia"""
        if vaccination_date is None:
            vaccination_date = date.today()
        self.vaccinations.append(f"{name} ({vaccination_date})")

    def add_note(self, note: str) -> None:
        """Dodaje notatkę medyczną z wizyty"""
        self.notes.append(note)

    def get_summary(self) -> str:
        """zwraca podsumowanie historii medycznej"""
        return(
            f"MedicalRecord(animal_id={self.animal_id},"
            f"diseases={len(self.diseases)},"
            f"vaccinations={len(self.vaccinations)},"
            f"notes={len(self.notes)})"
        )

    def __repr__(self) -> str:
        return self.get_summary()
