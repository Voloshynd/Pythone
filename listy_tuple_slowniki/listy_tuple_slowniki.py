from datetime import datetime

library = [
    ("Sunrise on the Reaping", "Suzanne Collins", 2025),
    ("Atomic Habits", "James Clear", 2018),
    ("The Secret of Secrets", "Dan Brown", 2025),
    ("The Let Them Theory", "Mel Robbins", 2023),
    ("The Atomic Habits Workbook", "James Clear", 2018)]

operations = ["add", "show", "search", "years", "dict", "end"]

print("Wszystkie dostępne opcje:")
for operation in operations:
    print(f"- {operation}")

program_is_working = True

while program_is_working:

    operation = input("Proszę wprowadzić opcje: ").lower().strip()

    while operation not in operations:
        operation = input(
            "Niepoprawna opcja. Spróbuj ponownie: ").lower().strip()

    # DODAWANIE NOWEJ KSIĄŻKI
    match operation:
        case "add":
            while True:
                book_title = input("Podaj nazwę książki: ").strip()

                if not book_title:
                    print("Tytuł książki nie może być pusty.")
                    continue

                for book in library:
                    if book_title.lower() == book[0].lower():
                        print(
                            "Książka z takim tytułem już jest w bibliotece. Podaj inną nazwę książki.")
                        break
                else:
                    book_title = book_title.capitalize()
                    break

            while True:
                author = input("Podaj autora książki: ").strip()

                if len(author.split()) != 2:
                    print("Podaj imię i nazwisko autora książki.")
                    continue

                author = author.title()
                break

            while True:
                published_year = input("Podaj rok publikacji: ").strip()

                if not published_year.isdigit():
                    print("Rok publikacji musi być liczbą")
                    continue

                if len(published_year) != 4:
                    print("Rok publikacji musi mieć dokładnie 4 cyfry")
                    continue

                year = int(published_year)
                current_year = datetime.now().year

                if year > current_year:
                    print("Rok publikacji nie może być w przyszłości")
                    continue

                break

            new_book = (book_title, author, published_year)
            library.append(new_book)

        # WYŚWIETLANIE WSZYSTKICH KSIĄŻEK
        case "show":
            print(
                f"{'Nr.'.ljust(4)} {'Tytuł'.ljust(40)} {'Autor'.ljust(25)} {'Rok publikacji'.rjust(15)}")
            print("-" * 90)

            for num, (title, writer, published_year) in enumerate(library,
                                                                  start=1):
                print(
                    f"{str(num).ljust(4)} {title.ljust(40)} {writer.ljust(25)} {str(published_year).rjust(15)}")

        # WYSZUKIWANIE KSIĄŻEK DANNEGO AUTORA
        case "search":
            while True:
                autor = input("Podaj autora książki: ").strip()

                if len(autor.split()) != 2:
                    print("Podaj imię i nazwisko autora książki.")
                    continue

                autor = autor.title()
                break

            num = 1
            found = False

            for title, writer, published_year in library:
                if autor.lower() == writer.lower():
                    print(
                        f"{str(num).ljust(4)} {title.ljust(40)} {writer.ljust(25)} {str(published_year).rjust(15)}")
                    num += 1
                    found = True

            if not found:
                print(
                    f"Niestety nie posiadamy książek autora - {autor.title()}")
                num = 1

        # WYŚWIETLANIE UNIKALNYCH LAT WYDANIA
        case "years":
            unique_years = set()

            for book in library:
                unique_year = book[-1]
                unique_years.add(unique_year)

            print("Unikalne lata wydania:", sorted(unique_years))
            unique_years = set()

        # TWORZENIE SŁOWNIKA
        case "dict":
            dict_by_years = {}

            for book in library:
                if book[-1] not in dict_by_years:
                    dict_by_years[book[-1]] = []

                if book[-1] in dict_by_years:
                    dict_by_years[book[-1]].append(book[0])

            print(dict_by_years)
            dict_by_years = {}

        # ZAKOŃCZENIE DZIAŁANIA
        case "end":
            program_is_working = False
