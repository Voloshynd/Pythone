from datetime import datetime
from warehouse import Warehouse
from helpers import show_commands, read_balance, write_balance, write_warehouse, \
    read_warehouse, read_transactions, write_transactions
from operation import Operation
from constants import AVAILABLE_OPERATIONS as operations


def run_accounting_app():

    balance = read_balance()
    warehouse = Warehouse(balance)
    current_stock = read_warehouse()
    passed_transactions = read_transactions()

    for item in current_stock:
        name, qty, price = item.values()
        warehouse.add_article(name, qty, price)

    for transaction in passed_transactions:
        warehouse.transactions.append(transaction)

    while True:
        show_commands(operations)
        operation = input("Proszę wprowadzić komendę: ").lower().strip()

        while operation not in operations:
            operation = input(
                "Niepoprawna komenda. Spróbuj ponownie: ").lower().strip()

        match operation:
            # SALDO
            case "balance":
                amount_input = warehouse.get_valid_amount("Podaj kwotę: ")
                operator = warehouse.check_operator(
                    "Podaj operator (+ lub -): ")

                warehouse.account_before_operation = warehouse.account
                if operator == "+":
                    warehouse.account += amount_input
                else:
                    if amount_input > warehouse.account:
                        print("Brak wystarczających środków na koncie.")
                    else:
                        warehouse.account -= amount_input
                        write_balance(str(warehouse.account))
                        action = Operation(operation,
                                           datetime.now().strftime("%H:%M:%S"),
                                           f"{warehouse.account_before_operation} {operator} {amount_input} "
                                           f"= {warehouse.account:.2f} zl")

                        print("Operacja zakończyła się pomyślnie.")
                        write_transactions(action.command, action.time,
                                           action.action)
                        warehouse.transactions.append(action)

            # SPRZEDAŻ
            case "sell":
                item_to_buy = warehouse.get_valid_product_name(
                    "Podaj nazwę produktu, który chcesz sprzedać: ")
                warehouse.account_before_operation = warehouse.account

                for item in warehouse.warehouse:
                    if item['name'] == item_to_buy:

                        print(f"Ilość sztuk na magazynie - {item['qty']} szt.")
                        quantity_to_buy = warehouse.get_valid_amount(
                            "Podaj ilość sztuk do zakupu: ")

                        while quantity_to_buy > item[
                            'qty']:
                            quantity_to_buy = input(
                                f"Podaj ilość większą od 0 i mniejszą niż na magazynie ({item['qty']}): ")

                        sell_price = warehouse.get_valid_price(
                            "Podaj cenę sprzedaży: ")

                        print(
                            f"Sprzedano {quantity_to_buy} szt. produktu {item_to_buy}.")
                        warehouse.account += quantity_to_buy * sell_price
                        item['qty'] -= quantity_to_buy

                        write_balance(str(warehouse.account))
                        action = Operation(operation,
                                           datetime.now().strftime("%H:%M:%S"),
                                           f"{warehouse.account_before_operation} + {quantity_to_buy} "
                                           f"* {sell_price} = {warehouse.account:.2f} zl")

                        write_transactions(action.command, action.time,
                                           action.action)
                        warehouse.transactions.append(action)
                        warehouse.account_before_operation = warehouse.account

                        break
                else:
                    print(f"Nie znaleziono produktu o nazwie {item_to_buy}.")

            # ZAKUP
            case "buy":
                article_to_buy = warehouse.get_valid_product_name(
                    "Podaj nazwę produktu: ")
                amount_input = warehouse.get_valid_amount(
                    "Podaj poprawną liczbę sztuk (liczba > 0): ")
                price_input = warehouse.get_valid_price(
                    "Podaj cenę za jedną sztukę: ")

                total_cost = round(amount_input * price_input, 2)
                warehouse.account_before_operation = warehouse.account

                if total_cost > warehouse.account:
                    print("Brak wystarczających środków na koncie.")
                else:
                    for item in warehouse.warehouse:
                        if item["name"] == article_to_buy:
                            item["qty"] += amount_input
                            warehouse.account -= total_cost
                            print("Towar został zakupiony")
                            break
                    else:
                        warehouse.add_article(article_to_buy, amount_input,
                                              price_input)

                        write_warehouse(article_to_buy, amount_input,
                                        price_input)
                        warehouse.account -= total_cost
                        print("Towar został zakupiony")

                write_balance(str(warehouse.account))
                action = Operation(operation,
                                   datetime.now().strftime("%H:%M:%S"),
                                   f"{warehouse.account_before_operation} - {total_cost} "
                                   f"= {warehouse.account:.2f} zl")

                write_transactions(action.command, action.time, action.action)
                warehouse.transactions.append(action)
                warehouse.account_before_operation = warehouse.account

            # PRZEGLĄD
            case "review":
                if not warehouse.transactions:
                    print("Nie było jeszcze żadnych transakcji")
                    continue

                start_index = input("Podaj początek przeglądu akcji: ")
                end_index = input("Podaj koniec przeglądu akcji: ")

                start = 0
                end = len(warehouse.transactions) - 1

                if start_index:
                    if not start_index.isdigit():
                        print("Początek zakresu musi być liczbą")
                        continue
                    start = int(start_index)

                if end_index:
                    if not end_index.isdigit():
                        print("Koniec zakresu musi być liczbą")
                        continue
                    end = int(end_index)

                if start < 0 or end >= len(
                        warehouse.transactions) or start > end:
                    print(
                        f"Niepoprawny zakres. Dostępne operacje: {len(warehouse.transactions)}")
                    continue

                warehouse.show_history(start, end)

            # KONTO
            case "account":
                print(f"Stan konta wynosi: {warehouse.account:.2f} zł")

            # MAGAZYN
            case "inventory":
                product = input("Podaj nazwę produktu: ")
                warehouse.check_inventory(product)
            # LISTA
            case "list":
                warehouse.show_warehouse()
            # KONIEC
            case "end":
                print("Aplikacja została zamknięta")
                break


run_accounting_app()
