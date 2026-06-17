class Owner:
    """Reprezentuje właściciela zwierzęcia."""

    def __init__(self, owner_id: int, first_name: str, last_name: str, phone: str, email: str) -> None:
        """
        Args:
            id: Numer identyfikacyjny właściciela
            first_name: Imię właściciela
            last_name: Nazwisko właściciela
            phone: Numer telefonu
            email: Adres email
        """
        self.owner_id = owner_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.animals: list[str] = []

    def full_name(self) -> str:
        """Zwraca imię i nazwisko właściciela."""
        return f"{self.first_name} {self.last_name}"

    def register_animal(self, animal_name: str) -> None:
        """Rejestruje zwierzę pod tym właścicielem."""
        self.animals.append(animal_name)

    def __repr__(self) -> str:
        """Tekstowa reprezentacja obiektu."""
        return f"Owner({self.full_name()!r})"