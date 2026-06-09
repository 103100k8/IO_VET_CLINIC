from clinic.animals import Animal
from datetime import date

burek = Animal('Burek', 'pies', 'Labrador', date(2018, 5, 10), 1)
print(burek.name)
print(burek.age())

