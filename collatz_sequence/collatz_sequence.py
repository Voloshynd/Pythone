x = int(input("Podaj liczbe x od 1 do 100: "))
sequence = ""
sequence_is_not_complete = True

while sequence_is_not_complete:

    while x < 1 or x > 99:
        x = int(input("Nieprawidłowa liczba, podaj liczbe od 1 do 100: "))

    print(f"Liczba {x} jest poprawna!")

    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = x * 3 + 1

        if x != 1:
            sequence += str(x) + ","
        else:
            sequence += str(x)

    sequence_is_not_complete = False

print(sequence.replace(",","->"))