cars = ["Audi", "BMW", "VW", "Mercedes"]

counter = 0

for car in cars:
    counter += 1
    print(f"Auto Nummer {counter} ist {car}")

print(counter)

class_a = ["Jan", "Nick", "Maria", "Peter"]
class_b = ["Klara", "Jonas", "Hans", "Vladimir"]

# for student in class_a:
#    print(student)
# for student in class_b:
#    print(student)


for student in class_b:
    class_a.append(student)
print(class_a)


digits = list(range(1,11))
for digit in digits:
    print(digit)

result = max(digits)
print (result)

age = 66

if 18 <= age <= 60:
    print("Zugriff erlaubt")
elif age > 60:
    print("zu alt")
else:
    print("Zugriff verweigert")

cities = ["Berlin","Matrid","Paris"]

if "Berlin" in cities:
    print ("enthalten")
else:
    print ("nicht enthalten")

liste_carina = list(range(1,10001))
list_a = []
list_b = []

for zahl in liste_carina:
    if (zahl/5).is_integer():
        list_a.append(zahl)
    else:
        list_b.append(zahl)
print ("Liste A")
print (list_a)
print ("Liste B")
print (list_b)