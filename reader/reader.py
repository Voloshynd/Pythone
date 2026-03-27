import sys
from helpers import read_csv, write_csv, check_path, show_changes, apply_changes

def main() -> None:
    if len(sys.argv) < 3:
        print(
            "Użycie: python reader.py <plik_wejsciowy> <plik_wyjsciowy> <zmiany...>")
        sys.exit(1)

    path_file_in = sys.argv[1]
    path_file_out = sys.argv[2]
    changes = sys.argv[3:]

    check_path(path_file_in, f"Plik '{path_file_in}' nie istnieje.")
    check_path(path_file_out, f"Plik '{path_file_out}' nie istnieje.")

    data = read_csv(path_file_in)
    data = apply_changes(data, changes)
    show_changes(data)
    write_csv(path_file_out, data)

if __name__ == "__main__":
    main()
