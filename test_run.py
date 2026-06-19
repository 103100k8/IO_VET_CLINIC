from datetime import date

from clinic.animals import Animal
from clinic.owners import Owner
from clinic.doctors import Doctor
from clinic.appointments import Appointment
from clinic.medical_record import MedicalRecord
from clinic.clinic import Clinic

def main() -> None:
    clinic = Clinic("k8vet", "Bułgarska 31 Poznań")

    owner = Owner(1, "Jan", "Kowalski", "123", "janko@gmail.com")
    animal = Animal("Ciapek", "pies", "Jamnik", date(2022, 1, 1) ,1)
    doctor = Doctor(1, "Maja", "Ślimak", "neurolog", "999")

    clinic.add_owner(owner)
    clinic.add_animal(animal)
    clinic.add_doctor(doctor)

    appointment = Appointment(animal.animal_id, doctor.id, date.today())
    clinic.schedule_appointment(appointment)

    record = MedicalRecord(animal.animal_id)
    record.add_disease("grypa")
    record.add_vaccination("borelioza")
    record.add_note("w normie")
    clinic.add_medical_record(record)

    print("Raport z Kliniki")
    print(clinic)
    print("Właściciele: ", clinic.owners)
    print("Zwierzeta: ", clinic.animals)
    print("Doktorzy: ", clinic.doctors)
    print("Wizyty: ", clinic.appointments)
    print("Wpisy: ", [r.get_summary() for r in clinic.records])

if __name__ == "__main__":
    main()
