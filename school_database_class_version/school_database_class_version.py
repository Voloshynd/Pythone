class Person:
    def __init__(self, name  = None, class_name = None):
        self.name = name.strip() if name else None
        self.class_name = class_name.strip() if class_name else None

    def check_name(self, name):
        if len(name.split()) != 2:
            return False

        for char in name:
            if char.isdigit():
                return False

        return name.lower().title()

    def get_valid_name(self, string):
        while True:
            name = input(string).strip()
            valid_name = self.check_name(name)

            if not valid_name:
                print(
                    "Imię i nazwisko muszą zawierać spację i nie zawierać cyfr")
                continue

            return valid_name

    def check_class_title(self, class_name):
        if len(class_name) != 2:
            return False

        if not class_name[0].isdigit() or not class_name[1].isalpha():
            return False

        return class_name.upper()

    def get_valid_class(self, string):
        while True:
            class_name = input(string).strip()
            valid_class = self.check_class_title(class_name)
            if not valid_class:
                print(
                    "Nazwa klasy musi zawierać jedną liczbę oraz jedną literę")
                continue
            return valid_class


class Student(Person):
    def __init__(self, name = None, class_name = None):
        super().__init__(name, class_name)


class Teacher(Person):
    def __init__(self, name = None, subject = None, classes = None):
        super().__init__(name)
        self.subject = subject
        self.classes = classes

    def get_valid_subject(self, string):
        while True:
            subject = input(string).strip()

            if not subject or len(subject) < 4:
                print("Nazwa przedmiotu nie może mieć mniej niż 4 znaki")
                continue

            return subject

    def add_classes(self, string):
        classes = []

        while True:
            class_input = input(string).strip()

            if class_input == "":
                break

            class_name = self.check_class_title(class_input)

            if not class_name:
                print(
                    "Nazwa klasy musi zawierać jedną liczbę oraz jedną literę")
                continue

            classes.append(class_name)

        return list(set(classes))


class Educator(Person):
    def __init__(self, name = None, class_name = None):
        super().__init__(name, class_name)


class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.educators = []

    def add_student(self, name, class_name):
        student = Student(name, class_name)
        self.students.append(student)

    def add_teacher(self, name, subject, classes):
        teacher = Teacher(name, subject, classes)
        self.teachers.append(teacher)

    def add_educator(self, name, class_name):
        educator = Educator(name, class_name)
        self.educators.append(educator)

    def show_class_info(self, class_name):
        return [student for student in self.students if
                student.class_name == class_name]

    def show_class_educator(self, class_name):
        return [educator for educator in self.educators if
                educator.class_name == class_name]

    def get_student_class(self, name):
        for student in self.students:
            if student.name == name:
                return student.class_name
        return None

    def show_teachers(self, student_class):
        return [teacher for teacher in self.teachers if
                student_class in teacher.classes]

    def show_teachers_classes(self, name):
        all_classes = []

        for teacher in self.teachers:
            if teacher.name == name:
                all_classes.extend(teacher.classes)

        return list(set(all_classes))

    def show_educator_students(self, name):
        educator_class = None
        for educator in self.educators:
            if educator.name == name:
                educator_class = educator.class_name
                break

        if educator_class is None:
            return None

        students_in_class = [student.name for student in self.students if
                             student.class_name == educator_class]

        return students_in_class


OPERATIONS = ["create", "manage", "end"]
SELECTIONS = ["student", "teacher", "educator", "end"]
MENAGEMENT_OPTIONS = ["class", "student", "teacher", "educator", "end"]

def show_menu(options):
    for option in options:
        print(f"- {option}")

def information_divider():
    print("=" * 40 + "\n")


 # CREATE
def handle_create(school, person):
    print("Dostepne opcje")
    show_menu(SELECTIONS)
    selection = input("Prosze wpisać opcje: ").strip().lower()

    match selection:
        case "student":
            name = person.get_valid_name("Podaj imię i nazwisko ucznia: ")
            class_name = person.get_valid_class("Podaj klasę ucznia (np. 3C): ")

            school.add_student(name, class_name)
            print("Uczeń został utworzony!")

        case "teacher":
            teacher = Teacher()

            name = person.get_valid_name("Podaj imię i nazwisko nauczyciela: ")
            subject = teacher.get_valid_subject("Podaj nazwę przedmiotu: ")
            classes = teacher.add_classes(
                "Podaj nazwy klas, które prowadzi nauczyciel lub zostaw linie pustą: "
            )

            school.add_teacher(name, subject, classes)
            print("Nauczyciel został utworzony!")

        case "educator":
            name = person.get_valid_name("Podaj imię i nazwisko wychowawcy: ")
            class_name = person.get_valid_class("Podaj nazwę klasy (np. '3C'): ")

            school.add_educator(name, class_name)
            print("Wychowawca został utworzony!")

# MANAGE
def handle_manage(school, person):
    print("Dostepne opcje zarządzania użytkownikami")
    show_menu(MENAGEMENT_OPTIONS)
    management_option = input("Prosze wpisać opcje: ").strip().lower()

    match management_option:

        case "class":
            class_name = person.get_valid_class("Podaj nazwę klasy (np. '3C'): ")

            students_list = school.show_class_info(class_name)

            if not students_list:
                information_divider()
                print("Nie ma uczniów z tej klasy")
            else:
                information_divider()
                for student in students_list:
                    print(student.name)

        case "student":
            name = person.get_valid_name("Podaj imię i nazwisko ucznia: ")
            student_class = school.get_student_class(name)

            if student_class is None:
                information_divider()
                print("Nie ma takiego ucznia")
            else:
                teachers = school.show_teachers(student_class)

                if not teachers:
                    print("Do tego ucznia nie przypisano żadnych lekcji")
                else:
                    information_divider()
                    print(f"Wszystkie lekcje ucznia {name} oraz jego nauczyciele:")

                    for teacher in teachers:
                        print(f"{teacher.subject.rjust(10)} - {teacher.name}")

        case "teacher":
            name = person.get_valid_name("Podaj imię i nazwisko nauczyciela: ")
            classes = school.show_teachers_classes(name)

            if not classes:
                print("Do tego nauczyciela nie przypisano żadnej klasy")
            else:
                information_divider()
                print(f"Wszystkie klasy, które prowadzi nauczyciel - {name}:")

                for each_class in classes:
                    print(each_class)

        case "educator":
            name = person.get_valid_name("Podaj imię i nazwisko wychowawcy: ")

            students_list = school.show_educator_students(name)

            if students_list is None:
                print("Nie ma takiego wychowawcy")
            elif not students_list:
                print("Do tego wychowawcy nie przypisano żadnych uczniów")
            else:
                information_divider()
                print(f"Wszyscy uczniowie, których prowadzi wychowawca - {name}:")

                for student_name in students_list:
                    print(student_name)

def run_app():
    school = School()
    person = Person()

    while True:
        print("Dostepne komendy:")
        show_menu(OPERATIONS)

        chosen_operation = input("Prosze wpisac komende: ").strip().lower()

        if chosen_operation not in OPERATIONS:
            print("Nie napisałes żadnej z dostepnych komend")
            continue

        match chosen_operation:

            case "create":
                handle_create(school, person)

            case "manage":
                handle_manage(school, person)

            case "end":
                break

run_app()