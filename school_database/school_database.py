students = []
teachers = []
educators = []

def show_menu(options):
    for option in options:
        print(f"- {option}")


def check_name(name):
    if len(name.split()) != 2:
        return False

    for char in name:
        if char.isdigit():
            return False

    return name.lower().title()


def get_valid_name(text):
    while True:
        name = check_name(input(text))
        if not name:
            print("Imię i nazwisko musza zawierać spacje i nie zawierać cyfer")
            continue
        return name


def check_class_title(class_name):
    if len(class_name) != 2:
        return False

    if not class_name[0].isdigit() or not class_name[1].isalpha():
        return False

    return class_name.upper()


def get_valid_class(text):
    while True:
        class_name = check_class_title(input(text).strip())
        if not class_name:
            print("Nazwa klasy musi zawierać jedną liczbę oraz jedną literę")
            continue
        return class_name


def information_divider():
    print("=" * 40 + "\n")


def show_class_info(class_name, people, msg):
    is_found = False

    for person in people:
        if person["class"] == class_name:
            if not is_found:
                print(msg)
                is_found = True
            print(person["name"])

    return is_found


operations = ["create", "manage", "end"]
selections = ["student", "teacher", "educator", "end"]
management_options = ["class", "student", "teacher", "educator", "end"]

while True:
    print("Dostepne komendy:")
    show_menu(operations)
    chosen_operation = input("Prosze wpisac komende: ").strip().lower()

    if chosen_operation not in operations:
        print("Nie napisałes żadnej z dostepnych komend")
        continue

    # CREATE
    match chosen_operation:
        case "create":
            print("Dostepne opcje")
            show_menu(selections)
            selection = input("Prosze wpisac opcje: ").strip().lower()

            match selection:
                case "student":
                    name = get_valid_name("Podaj imię i nazwisko ucznia: ")
                    class_name = get_valid_class(
                        "Podaj nazwę klasy (np. '3C'): ")

                    students.append({
                        "name": name,
                        "class": class_name
                    })
                    print("Uczen zostal utworzony!")

                case "teacher":
                    name = get_valid_name("Podaj imię i nazwisko nauczyciela: ")

                    while True:
                        subject_name = input("Podaj nazwę przedmiotu: ")
                        if not subject_name or len(subject_name) < 4:
                            print(
                                "Nazwa przedmiotu nie moze zawierac mniej niz 4 znaki: ")
                            continue
                        else:
                            break

                    list_classes = []

                    while True:
                        class_input = input(
                            "Podaj nazwy klas, które prowadzi nauczyciel lub zostaw linie pustą: "
                        ).strip()

                        if class_input == "":
                            break

                        class_name = check_class_title(class_input)

                        if not class_name:
                            print(
                                "Nazwa klasy musi zawierać jedną liczbę oraz jedną literę")
                            continue

                        list_classes.append(class_name)

                    teachers.append({
                        "name": name,
                        "subject": subject_name,
                        "classes": list(set(list_classes))
                    })
                    print("Nauczyciel został utworzony!")

                case "educator":
                    name = get_valid_name("Podaj imię i nazwisko wychowawcy: ")
                    class_name = get_valid_class(
                        "Podaj nazwę klasy (np. '3C'): ")

                    educators.append({
                        "name": name,
                        "class": class_name
                    })
                    print("Wychowawca został utworzony!")

        # MANAGE
        case "manage":
            print("Dostepne opcje zarządzania użytkownikami")
            show_menu(management_options)
            management_option = input("Prosze wpisac opcje: ").strip().lower()

            match management_option:
                case "class":
                    class_name = get_valid_class(
                        "Podaj nazwę klasy (np. '3C'): ")

                    information_divider()
                    found_students = show_class_info(
                        class_name,
                        students,
                        f"Wszyscy uczniowie z klasy {class_name}:"
                    )

                    if not found_students:
                        print("Nie ma uczniów z tej klasy")

                    information_divider()
                    found_educator = show_class_info(
                        class_name,
                        educators,
                        f"Wychowawca klasy {class_name}:"
                    )

                    if not found_educator:
                        print("Ta klasa nie posiada wychowawcy")

                case "student":
                    name = get_valid_name("Podaj imię i nazwisko ucznia: ")

                    student_class = None

                    for student in students:
                        if student["name"] == name:
                            student_class = student["class"]
                            break

                    if student_class is None:
                        print("Nie ma takiego ucznia")

                    found = False

                    for teacher in teachers:
                        if student_class in teacher["classes"]:
                            if not found:
                                information_divider()
                                print(
                                    f"Wszystkie lekcje ucznia {name} oraz nauczyciele:")
                                found = True

                            print(
                                f"{teacher['subject'].rjust(10)} - {teacher['name']}")

                    if not found:
                        print("Do tego ucznia nie przypisano żadnych lekcji")

                case "teacher":
                    name = get_valid_name("Podaj imię i nazwisko nauczyciela: ")

                    found = False
                    all_classes = []

                    for teacher in teachers:
                        if teacher["name"] == name:
                            if not found:
                                information_divider()
                                print(
                                    f"Wszystkie klasy, które prowadzi nauczyciel - {name}:")
                                found = True

                            all_classes.extend(teacher["classes"])

                    if found:
                        for each_class in set(all_classes):
                            print(each_class)
                    else:
                        print("Do tego nauczyciela nie przypisano żadnej klasy")

                case "educator":
                    name = get_valid_name("Podaj imię i nazwisko wychowacy: ")

                    educator_class = None

                    for educator in educators:
                        if educator["name"] == name:
                            educator_class = educator["class"]
                            break

                    if educator_class is None:
                        print("Nie ma takiego wychowawcy")

                    else:
                        found = False

                        for student in students:
                            if educator_class == student["class"]:
                                if not found:
                                    information_divider()
                                    print(
                                        f"Wszyscy uczniowie, których prowadzi wychowawca - {name}:")
                                    found = True

                                print(student["name"])

                        if not found:
                            print(
                                "Do tego wychowawcy nie przypisano żadnych uczniów")
        case "end":
            break
