import ast


def show_commands(commands):
    print("Wszystkie dostępne komendy:")
    for command in commands:
        print(f"- {command}")


def read_balance(file_path="balance.txt"):
    with open(file_path, "w") as f:
        f.write("0.00")

    with open("balance.txt", "r") as balance_txt:
        balance = balance_txt.read().strip()

    if not balance:
        return 0.0

    balance = float(balance)
    balance = f"{balance:.2f}"
    return float(balance)


def write_balance(balance):
    with open("balance.txt", "w") as balance_txt:
        balance = float(balance)
        balance_txt.write(f"{balance:.2f}")


def read_warehouse(file_path="warehouse.txt"):
    with open(file_path, "w"):
        pass

    with open("warehouse.txt", "r") as warehouse_txt:
        stock = warehouse_txt.readlines()
        clean_list = [ast.literal_eval(line.strip()) for line in stock if
                      line.strip()]
        return clean_list


def write_warehouse(name, qty, price):
    description = {"name": name,
                   "qty": qty,
                   "price": price}

    with open("warehouse.txt", "a", encoding="utf-8") as warehouse_txt:
        warehouse_txt.write("\n" + str(description))


def read_transactions(file_path="transaction_history.txt"):
    with open(file_path, "w"):
        pass

    with open("transaction_history.txt", "r") as transactions_txt:
        transactions = transactions_txt.readlines()
        clean_transactions = [ast.literal_eval(line.strip()) for line in
                              transactions if
                              line.strip()]
        return clean_transactions


def write_transactions(command, time, action):
    operation = {"command": command,
                 "time": time,
                 "action": action}

    with open("transaction_history.txt", "a") as transactions_txt:
        transactions_txt.write("\n" + str(operation))
