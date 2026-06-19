from clinic.medical_record import MedicalRecord

def test_add_disease():
    record = MedicalRecord(animal_id=1)

    record.add_disease("grypa")

    assert len(record.diseases) == 1
    assert "grypa" in record.diseases[0]

def test_add_vaccination():
    record = MedicalRecord(animal_id=1)

    record.add_vaccination("przeciw kleszczom")

    assert len(record.vaccinations) == 1
    assert "przeciw kleszczom" in record.vaccinations[0]

def test_add_note():
    record = MedicalRecord(animal_id=1)

    record.add_note("Badania kontrolne - wszystko w normie")

    assert record.notes == ["Badania kontrolne - wszystko w normie"]

def test_summary():
    record = MedicalRecord(animal_id=1)

    record.add_disease("grypa")
    record.add_vaccination("przeciw kleszczom")
    record.add_note("wszystko w normie")

    summary = record.get_summary()

    assert "diseases=1" in summary
    assert "vaccinations=1" in summary