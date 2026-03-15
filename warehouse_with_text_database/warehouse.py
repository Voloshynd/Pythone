class Warehouse:
    def __init__(self, account):
        self.account = account
        self.account_before_operation = account
        self.warehouse = []
        self.transactions = []

    def check_inventory(self, good):
        product_name = good.strip().capitalize()

        for item in self.warehouse:
            if item["name"] == product_name:
                print(f"Ilość w magazynie: {item['qty']} szt.")
                break
        else:
            print(f"Nie mamy takiego produktu - '{product_name}' na magazynie")

    def get_valid_amount(self, amount):
        while True:
            valid_amount = input(amount).strip().replace(",", ".")

            try:
                number = float(valid_amount)

                if number <= 0:
                    print("Wprowadź liczbę większą od 0.")
                    continue

                return number

            except ValueError:
                print("Wprowadź poprawną liczbę.")

    def check_operator(self, symbol):
        while True:
            operator = input(symbol).strip()
            if operator not in ["+", "-"]:
                print("Nieprawidłowa operacja. Wpisz + lub -.")
                continue

            return operator

    def show_warehouse(self):
        if not len(self.warehouse):
            print("Magazyn jest pusty!")
        else:
            print(f"{'Name'.ljust(20)} {'Qty'.rjust(5)} {'Price'.rjust(10)}")

        for item in self.warehouse:
            print(
                f"{item['name'].ljust(20)} "
                f"{str(int(item['qty'])).rjust(5)} "
                f"{str(item['price']).rjust(10)}"
            )

    def show_history(self, start, end):
        print(f"{'Komenda'.ljust(15)} {'Czas'.ljust(10)} {'Akcja'}")

        for transaction in self.transactions[start:end + 1]:
            print(
                f"{transaction.command.ljust(15)} "
                f"{transaction.time.ljust(10)} "
                f"{transaction.action}"
            )

    def get_valid_product_name(self, title):
        while True:
            name = input(title).lower().strip().capitalize()

            if not name:
                print("Nazwa produktu nie może być pusta.")
                continue

            if any(char.isdigit() for char in name):
                print("Nazwa nie może zawierać liczby.")
                continue

            return name

    def get_valid_price(self, price):
        while True:
            price_input = input(price).strip().replace(",", ".")

            if not price_input.replace(".", "").isdigit() or float(
                    price_input) <= 0:
                print("Podaj poprawną cenę (cena > 0.00).")
                continue

            return float(price_input)

    def add_article(self, name, qty, price):
        self.warehouse.append(
            {
                "name": name,
                "qty": int(qty),
                "price": price
            }
        )
