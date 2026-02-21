import random

board = "---------"
wins_combinations = "012,345,678,036,147,258,048,246"
is_playing = True
player = "O"
computer = "X"


print("Rozpoczynamy grę!!!")

while is_playing :

    print(5 * "=" + "Ruch komputera" + 5 * "=")

    while True:
        computer_field_identifier = random.randint(1, 9)

        if board[computer_field_identifier - 1] == "-":
            pos = computer_field_identifier - 1
            board = board[:pos] + computer + board[pos + 1:]
            print(f"Ruch komputera na: {computer_field_identifier}")
            break

    for combo in wins_combinations.split(","):
        if (
                board[int(combo[0])] == computer and
                board[int(combo[1])] == computer and
                board[int(combo[2])] == computer
        ):
            print("Przegrana!")
            is_playing = False
            break

    if "-" not in board:
        print("Remis!")
        break

    print(board[:3])
    print(board[3:6])
    print(board[6:9])

    print(5 * "=" + "Ruch gracza" + 5 * "=")

    while True:
        player_field_identifier = int(
            input("Proszę podać identyfikator pola od 1 do 9: "))
        if 1 <= player_field_identifier <= 9 and board[
            player_field_identifier - 1] == "-":
            pos = player_field_identifier - 1
            board = board[:pos] + player + board[pos + 1:]
            print(f"Twój ruch na: {player_field_identifier}")
            break
        else:
            print("Błąd! Proszę podać liczbę od 1 do 9! ")


    for combo in wins_combinations.split(","):
        if (
                board[int(combo[0])] == player and
                board[int(combo[1])] == player and
                board[int(combo[2])] == player
        ):
            print("Wygrana!")
            is_playing = False
            break

    if "-" not in board:
        print("Remis!")
        break

    print(board[:3])
    print(board[3:6])
    print(board[6:9])


