from clinic.animals import Animal
from clinic.owners import Owner
from clinic.doctors import Doctor
from clinic.appointments import Appointment
from clinic.medical_record import MedicalRecord

class Clinic:
    """Reprezentuje klinikę weterynaryjną."""

    def __init__(self, name: str, address: str) -> None:
        """
        Args:
            name: nazwa kliniki
            address: Adres
        """
        self.name = name
        self.address = address
        self.owners: list[Owner] = []
        self.animals: list[Animal] = []
        self.doctors: list[Doctor] = []
        self.appointments: list[Appointment] = []
        self.records: list[MedicalRecord] = []

    def add_owner(self, owner: Owner) -> None:
        """Dodaje właściciela do kliniki"""
        self.owners.append(owner)

    def add_animal(self, animal: Animal) -> None:
        """Dodaje zwierzę do kliniki"""
        self.animals.append(animal)

    def add_doctor(self, doctor: Doctor) -> None:
        """Dodaje lekarza do kliniki"""
        self.doctors.append(doctor)

    def schedule_appointment(self, appointment: Appointment) -> None:
        """Dodaje wizyte w harmonogramie kliniki"""
        self.appointments.append(appointment)

    def add_medical_record(self, record: MedicalRecord) -> None:
        """Dodaje historie medyczną zwierzaka"""
        self.records.append(record)

    def __repr__(self) -> str:
        """zwraca podstawowe informacje"""
        return(
            f"Clinic(name={self.name!r},"
            f"doctors={len(self.doctors)},"
            f"animals={len(self.animals)})"
        )