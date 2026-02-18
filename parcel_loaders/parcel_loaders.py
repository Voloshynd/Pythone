import sys

items_to_send = abs(int(input("Ile elementów chcesz wysłać: ")))
max_parcel_weight = 20

if items_to_send == 0:
    print("Nie wysyłamy nic, jeśli nie ma czego wysłać.")
    sys.exit()

items_weights = ""
item = 1

while item <= items_to_send:
    item_weight = int(input(f"Podaj wagę {item}-go elementu (1–10 kg): "))

    if 1 <= item_weight < 10:
        items_weights += str(item_weight)

        item += 1
    else:
        print("Nieprawidłowa waga! Przepraszamy!!! ")
        break

parcels_amount = 1
parcel_weight = 0
total_weight = 0
parcel_devide = ""

for i in range(len(items_weights)):
    weight = int(items_weights[i])

    if parcel_weight + weight <= max_parcel_weight:
        parcel_weight += weight
    else:
        parcels_amount += 1
        parcel_weight = weight

    parcel_devide += str(weight)

    if i + 1 < len(items_weights):
        next_weight = int(items_weights[i + 1])
        if parcel_weight + next_weight <= max_parcel_weight:
            parcel_devide += "+"
        else:
            parcel_devide += ", "

    total_weight += weight

empty_kg = parcels_amount * max_parcel_weight - total_weight
ending = ""

if parcels_amount == 1:
    ending = "paczkę"
elif 1 < parcels_amount <= 4:
    ending = "paczki"
else:
    ending = "paczek"

parcels = parcel_devide.replace("+", "")
parcels = parcels.replace(", ", ",")

parcel_weight = 0
min_weight_parcel = None
parcel_number = 0
min_parcel_number = 0

for i in range(len(parcels)):
    if parcels[i].isdigit():
        parcel_weight += int(parcels[i])

    elif parcels[i] == ",":
        parcel_number += 1

        if min_weight_parcel is None or parcel_weight < min_weight_parcel:
            min_weight_parcel = parcel_weight

        parcel_weight = 0

parcel_number += 1

if min_weight_parcel is None or parcel_weight < min_weight_parcel:
    min_weight_parcel = parcel_weight
    min_parcel_number = parcel_number

if not min_parcel_number:
    min_parcel_number += 1

print(f"""
Podsumowanie:
    Wysłano {parcels_amount} {ending} ({parcel_devide})
    Wysłano {total_weight} kg
    Suma pustych kilogramów: {empty_kg}kg
    Najwięcej pustych kilogramów ma paczka Nr: {min_parcel_number}  {max_parcel_weight - min_weight_parcel}kg
""")
