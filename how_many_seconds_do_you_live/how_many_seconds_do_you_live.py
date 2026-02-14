age = int(input("Podaj swój wiek: "))
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print(f"""
Masz {age} lat, czyli żyjesz około:
{days} dni
{hours} godzin
{minutes} minut
{seconds} sekund
""")