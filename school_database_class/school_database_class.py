class User:
    students = []
    teachers = []
    educators = []
    operations = ["create", "manage", "end"]
    selections = ["student", "teacher", "educator", "end"]
    management_options = ["class", "student", "teacher", "educator", "end"]

    def __init__(self, name = None, subject = None, class_name = None):
        self.name = name
        self.subject = subject
        self.class_name = class_name

    @staticmethod
    def show_menu(options):
        for option in options:
            print(f"- {option}")

    @staticmethod
    def check_name(name):
        if len(name.split()) != 2:
            return False

        for char in name:
            if char.isdigit():
                return False

        return name.lower().title()

    @staticmethod
    def get_valid_name(text):
        while True:
            name = User.check_name(input(text))
            if not name:
                print(
                    "Imię i nazwisko muszą zawierać spację i nie zawierać cyfr")
                continue
            return name

    @staticmethod
    def check_class_title(class_name):
        if len(class_name) != 2:
            return False

        if not class_name[0].isdigit() or not class_name[1].isalpha():
            return False

        return class_name.upper()

    @staticmethod
    def get_valid_class(text):
        while True:
            class_name = User.check_class_title(input(text).strip())
            if not class_name:
                print(
                    "Nazwa klasy musi zawierać jedną liczbę oraz jedną literę")
                continue
            return class_name

    @staticmethod
    def check_subject_title(text):
        while True:
            subject = input(text).strip()

            if not subject or len(subject) < 4:
                print("Nazwa przedmiotu musi mieć minimum 4 znaki")
                continue

            return subject

    @staticmethod
    def get_teacher_classes(text):
        list_classes = []

        while True:
            teacher_classes = input(text).strip()

            if teacher_classes == "":
                break

            teacher_classes = User.check_class_title(teacher_classes)

            if not teacher_classes:
                print(
                    "Nazwa klasy musi zawierać jedną liczbę oraz jedną literę")
                continue

            list_classes.append(teacher_classes)

        return list_classes

    @staticmethod
    def information_divider():
        print("=" * 40 + "\n")

    @staticmethod
    def show_class_info(class_name, people, msg):
        is_found = False

        for person in people:
            if person["class"] == class_name:
                if not is_found:
                    print(msg)
                    is_found = True
                print(person["name"])

        return is_found

while True:
    print("Dostepne komendy:")
    User.show_menu(User.operations)
    chosen_operation = input("Prosze wpisac komende: ").strip().lower()

    match chosen_operation:
        case "create":
            print("Dostepne opcje")
            User.show_menu(User.selections)
            selection = input("Prosze wpisac opcje: ").strip().lower()

            match selection:
                case "student":
                    name = User.get_valid_name("Podaj imię i nazwisko ucznia: ")
                    class_name = User.get_valid_class("Podaj nazwę klasy (np. '3C'): ")

                    User.students.append({
                        "name": name,
                        "class": class_name
                    })
                    print("Uczen zostal utworzony!")

                case "teacher":
                    name = User.get_valid_name("Podaj imię i nazwisko nauczyciela: ")
                    subject = User.check_subject_title("Podaj nazwę przedmiotu: ")
                    list_classes = User.get_teacher_classes("Podaj nazwy klas, które prowadzi nauczyciel lub zostaw linie pustą: ")

                    User.teachers.append({
                        "name": name,
                        "subject": subject,
                        "classes": list(set(list_classes))
                    })
                    print("Nauczyciel został utworzony!")

                case "educator":
                    name = User.get_valid_name("Podaj imię i nazwisko wychowawcy: ")
                    class_name = User.get_valid_class("Podaj nazwę klasy (np. '3C'): ")

                    User.educators.append({
                        "name": name,
                        "class": class_name
                    })
                    print("Wychowawca został utworzony!")


        case "manage":
            print("Dostepne opcje zarządzania użytkownikami")
            User.show_menu(User.management_options)
            management_option = input("Prosze wpisac opcje: ").strip().lower()

            match management_option:
                case "class":
                    class_name = User.get_valid_class("Podaj nazwę klasy (np. '3C'): ")

                    User.information_divider()
                    found_students = User.show_class_info(
                        class_name,
                        User.students,
                        f"Wszyscy uczniowie z klasy {class_name}:"
                    )

                    if not found_students:
                        print("Nie ma uczniów z tej klasy")

                    User.information_divider()
                    found_educator = User.show_class_info(
                        class_name,
                        User.educators,
                        f"Wychowawca klasy {class_name}:"
                    )

                    if not found_educator:
                        print("Ta klasa nie posiada wychowawcy")

                case "student":
                    name = User.get_valid_name("Podaj imię i nazwisko ucznia: ")

                    student_class = None

                    for student in User.students:
                        if student["name"] == name:
                            student_class = student["class"]
                            break

                    if student_class is None:
                        print("Nie ma takiego ucznia")

                    is_found = False

                    for teacher in User.teachers:
                        if student_class in teacher["classes"]:
                            if not is_found:
                                User.information_divider()
                                print(
                                    f"Wszystkie lekcje ucznia {name} oraz nauczyciele:")
                                is_found = True

                            print(
                                f"{teacher['subject'].rjust(10)} - {teacher['name']}")

                    if not is_found:
                        print("Do tego ucznia nie przypisano żadnych lekcji")

                case "teacher":
                    name = User.get_valid_name("Podaj imię i nazwisko nauczyciela: ")

                    is_found = False
                    all_classes = []

                    for teacher in User.teachers:
                        if teacher["name"] == name:
                            if not is_found:
                                User.information_divider()
                                print(
                                    f"Wszystkie klasy, które prowadzi nauczyciel - {name}:")
                                is_found = True

                            all_classes.extend(teacher["classes"])

                    if is_found:
                        for each_class in set(all_classes):
                            print(each_class)
                    else:
                        print("Do tego nauczyciela nie przypisano żadnej klasy")

                case "educator":
                    name = User.get_valid_name("Podaj imię i nazwisko wychowacy: ")

                    educator_class = None

                    for educator in User.educators:
                        if educator["name"] == name:
                            educator_class = educator["class"]
                            break

                    if educator_class is None:
                        print("Nie ma takiego wychowawcy")

                    else:
                        is_found = False

                        for student in User.students:
                            if educator_class == student["class"]:
                                if not is_found:
                                    User.information_divider()
                                    print(
                                        f"Wszyscy uczniowie, których prowadzi wychowawca - {name}:")
                                    is_found = True

                                print(student["name"])

                        if not is_found:
                            print(
                                "Do tego wychowawcy nie przypisano żadnych uczniów")
        case "end":
            break