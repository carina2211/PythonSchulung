persons = [
    {"name": "Carina", "height": 180, "age": 32},
    {"name": "Simon", "height": 185, "age": 35},
    {"name": "Emilie", "height": 160, "age": 31}
]

# print(f"Name ist {person['name']} ")
# und das Alter ist {person['age']}")
for person in persons:
    print(f"Name ist {person['name']} und das Alter ist {person['age']}")

animal = {"name": "Berta", "type": "Giraffe"}

print(animal)
animal["type"] = "Löwe"
animal["Partner"] = {"name": "Helmut", "type": "Giraffe", "hasChildren": True}

# Ebene 1   #Ebene 2
print(animal["Partner"]["hasChildren"])

students = {"Jannick": 261456,
            "Peter": 456156,
            "Klara": 147258
            }

for key, value in students.items():
    print(f"Key: {key} und Value: {value}")

for person in persons:
    for key, value in person.items():
        print(f"Key: {key} und Value: {value}")

print("###############################")

mitarbeiter = [
    {"name": "Carina", "Berufsbezeichnung": "BI Engineer", "Gehalt": 62500},
    {"name": "Laura", "Berufsbezeichnung": "Empfangsdame", "Gehalt": 35500},
    {"name": "Peter", "Berufsbezeichnung": "Sysadmin", "Gehalt": 80500},
    {"name": "Mike", "Berufsbezeichnung": "Buchhalter", "Gehalt": 40500},
    {"name": "Raphael", "Berufsbezeichnung": "Head of Shoppis", "Gehalt": 150500},
]

result = 0
for ma in mitarbeiter:
     result += ma["Gehalt"]

print (result)