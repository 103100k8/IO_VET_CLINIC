from datetime import date

from clinic.animals import Animal
from clinic.owners import Owner
from clinic.doctors import Doctor
from clinic.appointments import Appointment
from clinic.medical_record import MedicalRecord
from clinic.clinic import Clinic


def test_add_owner():
    clinic = Clinic("k8vet", "Bułgarska 31 Poznań")

    owner = Owner(1, "Jan", "Kowalski", "123", "janko@gmail.com")
    clinic.add_owner(owner)

    assert len(clinic.owners) == 1
    assert clinic.owners[0].first_name == "Jan"

def test_add_animal():
    clinic = Clinic("k8vet", "Bułgarska 31 Poznań")

    animal = Animal("Ciapek", "pies", "Jamnik", date(2022, 1, 1) ,1)
    clinic.add_animal(animal)

    assert len(clinic.animals) == 1
    assert clinic.animals[0].name == "Ciapek"

def test_add_doctor():
    clinic = Clinic("k8vet", "Bułgarska 31 Poznań")

    doctor = Doctor(1, "Maja", "Ślimak", "neurolog", "999")
    clinic.add_doctor(doctor)

    assert len(clinic.doctors) == 1
    assert clinic.doctors[0].name == "Maja"

def test_schedule_appointment():
    clinic = Clinic("k8vet", "Bułgarska 31 Poznań")

    appointment = Appointment(1, 1, date.today())
    clinic.schedule_appointment(appointment)

    assert len(clinic.appointments) ==1

def test_add_medical_record():
    clinic = Clinic("k8vet", "Bułgarska 31 Poznań")

    record = MedicalRecord(1)
    clinic.add_medical_record(record)

    assert len(clinic.records) == 1

def test_clinic_repr():
    clinic = Clinic("k8vet", "Bułgarska 31 Poznań")

    rep = repr(clinic)

    assert "k8vet" in rep
    assert "doctors" in rep
    assert "animals" in rep

def test_full_flow():
    clinic = Clinic("k8vet", "Bułgarska 31 Poznań")

    owner = Owner(1, "Jan", "Kowalski", "123", "jan@mail.com")
    animal = Animal("Ciapek", "pies", "Jamnik", date(2022, 1, 1), owner.owner_id)
    doctor = Doctor(1, "Maja", "Ślimak", "neurolog", "999")
    appointment = Appointment(animal.animal_id, doctor.id, date.today())
    record = MedicalRecord(animal.animal_id)

    clinic.add_owner(owner)
    clinic.add_animal(animal)
    clinic.add_doctor(doctor)
    clinic.schedule_appointment(appointment)
    clinic.add_medical_record(record)

    assert len(clinic.owners) == 1
    assert len(clinic.animals) == 1
    assert len(clinic.doctors) == 1
    assert len(clinic.appointments) == 1
    assert len(clinic.records) == 1