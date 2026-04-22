import pathlib
import ast


def load_data(manager):
    is_file_exists = pathlib.Path("data.txt").exists()

    if not is_file_exists:
        with open("data.txt", "w", encoding="UTF-8") as f:
            f.write("0\n")
            f.write("[]\n")
            f.write(
                "[{'name': 'Piłka nożna', 'qty': 12, 'price': 79.99}, {'name': 'Piłka koszykowa', 'qty': 8, 'price': 89.99}, {'name': 'Rakieta tenisowa', 'qty': 5, 'price': 249.99}, {'name': 'Buty do biegania', 'qty': 6, 'price': 399.99}]\n")

    with open("data.txt", "r", encoding="UTF-8") as f:
        lines = f.readlines()

    if len(lines) < 3:
        manager.account = 0
        manager.transaction_history = []
        manager.warehouse = []
        return

    manager.account = float(lines[0].strip())
    manager.transaction_history = ast.literal_eval(lines[1].strip())
    manager.warehouse = ast.literal_eval(lines[2].strip())


def update_data(manager):
    with open("data.txt", "w", encoding="UTF-8") as f:
        f.write(f"{manager.account}\n")
        f.write(f"{manager.transaction_history}\n")
        f.write(f"{manager.warehouse}\n")
