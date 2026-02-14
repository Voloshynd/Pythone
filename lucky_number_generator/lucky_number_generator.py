num1 = int(input("Podaj pierwszą liczbę całkowitą: "))
num2 = int(input("Podaj drugą liczbę całkowitą: "))
sum_of_numbers = num1 + num2
multiplay_of_numbers = num1 * num2
modulus_of_numbers = None

if num2 == 0:
    modulus_of_numbers = "Nie można dzielić przez zero"
else:
    modulus_of_numbers = num1 % num2

print(f"""
Twoje szczęśliwe liczby to {num1} i {num2}:
- łączna suma: {sum_of_numbers}
- iloczyn: {multiplay_of_numbers}
- reszta z dzielenia: {modulus_of_numbers}
""")