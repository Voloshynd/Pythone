from datetime import datetime


# SALDO

def balance(manager):
    manager.account_before_operation = manager.account

    while True:
        amount_input = input("Podaj kwotę: ").strip()

        if not amount_input.isdigit() or int(amount_input) <= 0:
            print(
                "Wprowadź poprawną wartość liczbową (liczba całkowita > 0)")
            continue
        break

    while True:
        operator = input("Podaj operację (+ lub -): ").strip()
        if operator not in ["+", "-"]:
            print("Nieprawidłowa operacja. Wpisz + lub -.")
            continue
        break

    amount = int(amount_input)
    if amount > manager.account and operator == "-":
        print(
            f"Brak wystarczających środków na koncie! Konto wynosi - {manager.account} zł")
        return

    if operator == "+":
        manager.account += amount
    else:
        manager.account -= amount

    action = {
        "komenda": "balance",
        "czas": datetime.now().strftime("%H:%M:%S"),
        "akcja": f"{manager.account_before_operation} {operator} {amount} = {manager.account} zł"
    }

    manager.transaction_history.append(action)
    manager.execute("update")


# ZAKUP

def buy(manager):
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

    if total_cost > manager.account:
        print("Brak wystarczających środków na koncie.")
    else:
        for item in manager.warehouse:
            if item["name"] == article_to_buy:
                item["qty"] += amount_to_buy
                manager.account -= total_cost
                print("Towar został zakupiony")
                break
        else:
            manager.warehouse.append({
                "name": article_to_buy,
                "qty": amount_to_buy,
                "price": price_for_unit
            })
            manager.account -= total_cost
            print("Towar został zakupiony")

        action = {
            "komenda": "buy",
            "czas": datetime.now().strftime("%H:%M:%S"),
            "akcja": f"{manager.account_before_operation} - {total_cost} = {manager.account} zl"
        }
        manager.transaction_history.append(action)
        manager.account_before_operation = manager.account
        manager.execute("update")


# SPRZEDAŻ

def sell(manager):
    item_to_buy = input(
        "Podaj nazwę produktu, który chcesz kupić: ").lower().strip().capitalize()

    for item in manager.warehouse:
        if item['name'] == item_to_buy:

            print(f"Ilość sztuk na magazynie - {item['qty']} szt.")

            quantity_to_buy = int(
                input("Podaj ilość sztuk do zakupu: "))
            while quantity_to_buy <= 0 or quantity_to_buy > item['qty']:
                quantity_to_buy = int(input(
                    f"Podaj ilość większą od 0 i mniejszą niż na magazynie ({item['qty']}): "))

            while True:
                try:
                    sell_price = float(input("Podaj cenę sprzedaży: "))

                    if sell_price <= 0:
                        print("Cena musi być większa od 0.")
                        continue

                    break

                except ValueError:
                    print("Cena musi być liczbą.")

            print(
                f"Sprzedano {quantity_to_buy} szt. produktu {item_to_buy}.")

            manager.account += quantity_to_buy * sell_price
            item['qty'] -= quantity_to_buy

            action = {
                "komenda": "sell",
                "czas": datetime.now().strftime("%H:%M:%S"),
                "akcja": (
                    f"{manager.account_before_operation} + "
                    f"{quantity_to_buy} * {sell_price} = {manager.account} zl"
                )
            }

            manager.transaction_history.append(action)
            manager.account_before_operation = manager.account
            manager.execute("update")
            break
    else:
        print(f"Nie znaleziono produktu o nazwie {item_to_buy}.")


# KONTO

def account(manager):
    print(f"Stan konta wynosi: {manager.account} zł")


# MAGAZYN


def inventory(manager):
    article = input(
        "Podaj nazwę produktu: ").strip().lower().capitalize()

    for item in manager.warehouse:
        if item["name"] == article:
            print(f"Ilość w magazynie: {str(item['qty'])} szt.")
            break
    else:
        print("Nie mamy takiego produktu na magazynie")


# PRZEGLĄD

def review(manager):
    if not len(manager.transaction_history):
        print("Nie było jeszcze żadnych transakcji")
        return

    while True:
        start_index = input("Podaj początek przeglądu akcji: ")
        end_index = input("Podaj koniec przeglądu akcji: ")
        start = 0
        end = len(manager.transaction_history)

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

        if start < 0 or end > len(
                manager.transaction_history) or start > end:
            print(
                f"Proszę wybrać prawidłowy zakres. "
                f"Liczba dostępnych komend: {len(manager.transaction_history)}")
            break

        print(
            f"{'Komenda'.ljust(20)} {'Czas'.rjust(5)} {'Akcja'.rjust(10)}")
        for transaction in manager.transaction_history[start:end + 1]:
            print(
                f"{transaction['komenda'].ljust(21)} "
                f"{transaction['czas'].rjust(5)} "
                f"{transaction['akcja'].rjust(20)}"
            )
        return


# LISTA

def list(manager):
    print(f"{'Name'.ljust(20)} {'Qty'.rjust(5)} {'Price'.rjust(10)}")
    for item in manager.warehouse:
        print(
            f"{item['name'].ljust(20)} "
            f"{str(item['qty']).rjust(5)} {str(item['price']).rjust(10)}")
