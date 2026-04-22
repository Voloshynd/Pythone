from manager import Manager
from storage import load_data, update_data
from commands import balance, buy, sell, account, inventory, review, list


def main() -> None:
    manager = Manager()

    @manager.assign("load")
    def load(manager):
        load_data(manager)

    manager.execute("load")

    @manager.assign("update")
    def update(manager):
        update_data(manager)

    # SALDO
    @manager.assign("balance")
    def get_balance(manager):
        balance(manager)

    # ZAKUP

    @manager.assign("buy")
    def to_buy(manager):
        buy(manager)

    # SPRZEDAŻ

    @manager.assign("sell")
    def to_sell(manager):
        sell(manager)

    # KONTO

    @manager.assign("account")
    def get_balance(manager):
        account(manager)

    # MAGAZYN

    @manager.assign("inventory")
    def get_inventory(manager):
        inventory(manager)

    # PRZEGLĄD

    @manager.assign("review")
    def show_history(manager):
        review(manager)

    # LISTA

    @manager.assign("list")
    def get_stock(manager):
        list(manager)

    print("Wszystkie dostępne komendy:")
    for operation in manager.available_operations:
        print(f"- {operation}")

    while True:
        command = input("Proszę wprowadzić komendę: ").lower().strip()

        while command not in manager.available_operations:
            command = input(
                "Niepoprawna komenda. Spróbuj ponownie: ").lower().strip()

        match command:
            case "balance":
                manager.execute(command)
            case "sell":
                manager.execute(command)
            case "buy":
                manager.execute(command)
            case "account":
                manager.execute(command)
            case "inventory":
                manager.execute(command)
            case "review":
                manager.execute(command)
            case "list":
                manager.execute(command)
            case "end":
                break


if __name__ == "__main__":
    main()
