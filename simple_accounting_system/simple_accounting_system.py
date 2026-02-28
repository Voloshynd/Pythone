from datetime import datetime

available_operations = ["saldo", "sprzedaż", "zakup", "konto", "lista",
                        "magazyn", "przegląd",
                        "koniec"]
warehouse = [
    {"name": "Piłka nożna", "qty": 12, "price": 79.99},
    {"name": "Piłka koszykowa", "qty": 8, "price": 89.99},
    {"name": "Rakieta tenisowa", "qty": 5, "price": 249.99},
    {"name": "Buty do biegania", "qty": 6, "price": 399.99},
    {"name": "Rękawice bokserskie", "qty": 4, "price": 199.99},
    {"name": "Mata do jogi", "qty": 15, "price": 59.99},
    {"name": "Hantle", "qty": 10, "price": 149.99},
    {"name": "Skakanka", "qty": 20, "price": 29.99},
    {"name": "Okulary pływackie", "qty": 14, "price": 49.99},
    {"name": "Kask rowerowy", "qty": 7, "price": 299.99}
]
transaction_history = []
account = 8000
account_before_operation = account

print("Wszystkie dostępne komendy:")
for each_operation in available_operations:
    print(f"- {each_operation}")

program_is_working = True

while program_is_working:
    operation = input("Proszę wprowadzić komendę: ").lower().strip()

    while operation not in available_operations:
        operation = input(
            "Niepoprawna komenda. Spróbuj ponownie: ").lower().strip()

    match operation:
    # SALDO
        case "saldo":
            while True:
                amount_input = input("Podaj kwotę: ").strip()

                if not amount_input or not amount_input.isdigit():
                    print(
                        f"Wprowadź poprawną wartość liczbową (liczba całkowita > 0)")
                    continue
                break

            while True:
                operator = input("Podaj operację (+ lub -): ").strip()
                if operator not in ["+", "-"]:
                    print("Nieprawidłowa operacja. Wpisz + lub -.")
                    continue
                break

            amount = int(amount_input)
            if operator == "+":
                account += amount
            else:
                account -= amount

            action = {
                "komenda": operation,
                "czas": datetime.now().strftime("%H:%M:%S"),
                "akcja": f"{account_before_operation} {operator} {amount} = {account} zl"
            }

            transaction_history.append(action)
            account_before_operation = account

    # ZAKUP

        case "zakup":
            while True:
                article_to_buy = input(
                    "Podaj nazwę produktu: ").strip().capitalize()
                if not article_to_buy:
                    print("Nazwa produktu nie może być pusta.")
                    continue

                if article_to_buy.isdigit():
                    print("Nazwa produktu nie może być liczbą.")
                    continue
                break

            while True:
                amount_input = input("Podaj liczbę sztuk: ").strip()
                if not amount_input.isdigit() or int(amount_input) <= 0:
                    print("Podaj poprawną liczbę sztuk (liczba > 0).")
                    continue

                amount_to_buy = int(amount_input)
                break

            while True:
                price_input = input("Podaj cenę za jedną sztukę: ").strip()
                price_input = price_input.replace(",", ".")
                if not price_input.replace(".", "").isdigit() or float(
                        price_input) <= 0:
                    print("Podaj poprawną cenę (cena > 00.00).")
                    continue
                price_for_unit = float(price_input)
                break

            total_cost = round(amount_to_buy * price_for_unit, 2)

            if total_cost > account:
                print("Brak wystarczających środków na koncie.")
            else:
                for item in warehouse:
                    if item["name"] == article_to_buy:
                        item["qty"] += amount_to_buy
                        account -= total_cost
                        print("Towar został zakupiony")
                        break
                else:
                    warehouse.append({
                        "name": article_to_buy,
                        "qty": amount_to_buy,
                        "price": price_for_unit
                    })
                    account -= total_cost
                    print("Towar został zakupiony")

                action = {
                    "komenda": operation,
                    "czas": datetime.now().strftime("%H:%M:%S"),
                    "akcja": f"{account_before_operation} - {total_cost} = {account} zl"
                }
                transaction_history.append(action)
                account_before_operation = account

    # SPRZEDAŻ

        case "sprzedaż":
            item_to_buy = input(
                "Podaj nazwę produktu, który chcesz kupić: ").lower().strip().capitalize()
            quantity_to_buy = 0

            for item in warehouse:
                if item["name"] == item_to_buy:
                    print(f"Ilość sztuk na magazynie - {item['qty']} szt.")
                    quantity_to_buy = int(input("Podaj ilość sztuk do zakupu: "))
                    while quantity_to_buy <= 0 or quantity_to_buy > item["qty"]:
                        quantity_to_buy = int(input(
                            f"Podaj ilość większą od 0 i mniejszą niż na magazynie ({item['qty']}): "))

                    print(
                        f"Zakupiono {quantity_to_buy} szt. produktu {item_to_buy}.")

                    account += quantity_to_buy * item["price"]
                    item["qty"] -= quantity_to_buy

                    action = {
                        "komenda": operation,
                        "czas": datetime.now().strftime("%H:%M:%S"),
                        "akcja": f"{account_before_operation} + {quantity_to_buy} * {item["price"]} = {account} zl"
                    }

                    transaction_history.append(action)
                    account_before_operation = account

                    break
            else:
                print(f"Nie znaleziono produktu o nazwie {item_to_buy}.")

    # KONTO

        case "konto":
            print(f"Stan konta wynosi: {account} zł")

    # MAGAZYN

        case "magazyn":
            article = input("Podaj nazwę produktu: ").strip().lower().capitalize()

            for item in warehouse:
                if item["name"] == article:
                    print(f"Ilość w magazynie: {str(item["qty"])} szt.")
                    break
            else:
                print("Nie mamy takiego produktu na magazynie")

    # PRZEGLĄD

        case "przegląd":

            if not len(transaction_history):
                print("Nie było jeszcze żadnych transakcji")
                continue

            while True:
                start_index = input("Podaj początek przeglądu akcji: ")
                end_index = input("Podaj koniec przeglądu akcji: ")
                start = 0
                end = len(transaction_history)

                if start_index != "" and end_index == "":
                    if not start_index.isdigit():
                        print("Początek zakresu musi być liczbą")
                        break
                    start = int(start_index)
                elif start_index == "" and end_index != "":
                    if not end_index.isdigit():
                        print("Koniec zakresu musi być liczbą")
                        break
                    end = int(end_index)
                elif start_index != "" and end_index != "":
                    if not start_index.isdigit() or not end_index.isdigit():
                        print("Zakres musi być liczbami")
                        break
                    start = int(start_index)
                    end = int(end_index)

                if start < 0 or end > len(transaction_history) or start >= end:
                    print(
                        f"Proszę wybrać prawidłowy zakres. Liczba dostępnych komend: {len(transaction_history)}")
                    break

                print(
                    f"{'Komenda'.ljust(20)} {'Czas'.rjust(5)} {'Akcja'.rjust(10)}")
                for transaction in transaction_history[start:end]:
                    print(
                        f"{transaction["komenda"].ljust(21)} "
                        f"{transaction["czas"].rjust(5)} "
                        f"{transaction["akcja"].rjust(20)}"
                    )

    # LISTA

        case "lista":
            print(f"{'Name'.ljust(20)} {'Qty'.rjust(5)} {'Price'.rjust(10)}")
            for item in warehouse:
                print(
                    f"{item["name"].ljust(20)} {str(item["qty"]).rjust(5)} {str(item["price"]).rjust(10)}")

    # KONIEC

        case "koniec":
            program_is_working = False
