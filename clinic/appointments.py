from datetime import date
class Appointment:
    """Klasa dotyczy wizyty zwierzęcia w klinice"""

    def __init__(
        self,
        animal_id: int,
        doctor_id: int,
        visit_date: date,
        symptoms: str = "",
        diagnosis: str = "",
        treatment: str = "",
        weight: float | None = None
    ) -> None:
        self.animal_id = animal_id
        self.doctor_id = doctor_id
        self.visit_date = visit_date
        self.symptoms = symptoms
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.weight = weight

    def add_diagnosis(self, diagnosis: str) -> None:
        self.diagnosis = diagnosis

    def add_treatment(self, treatment: str) -> None:
        self.treatment = treatment

    def set_weight(self, weight: float) -> None:
        self.weight = weight

    def __repr__(self) -> str:
        return (
            f"Appointment(animal_id={self.animal_id}, doctor_id={self.doctor_id}, "
            f"date={self.visit_date}, diagnosis={self.diagnosis!r})")