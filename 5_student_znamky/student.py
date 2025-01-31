class Student:
    def __init__(
        self,
        student_id: int,
        isic_id: str,
        first_name: str,
        last_name: str,
        class_name: str,
        email: str
    ):
        # Private attributes
        self.__student_id = student_id
        self.__isic_id = isic_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__class_name = class_name
        self.__email = email

        # Dictionary where key=subject (str), value = list of grades.
        # Each grade is a dict with keys: event_name, points, base
        self.__subjects = {}

    def addSubject(self, subject: str) -> None:
        """Add a subject to the student's subject list."""
        if subject in self.__subjects:
            print(f"Predmet '{subject}' uz existuje.")
        else:
            self.__subjects[subject] = []

    def removeSubject(self, subject: str) -> None:
        """Remove a subject from the student's subject list.
        If there are any grades, ask for confirmation."""
        if subject not in self.__subjects:
            print(f"Predmet '{subject}' neexistuje.")
            return

        # Check if there are grades
        if len(self.__subjects[subject]) > 0:
            confirm = input(f"Existuju znamky z predmetu '{subject}'. Chcete ho odstranit aj s nimi? (y/n) ")
            if confirm.lower() != 'y':
                print("Predmet nebol odstranený.")
                return
        del self.__subjects[subject]
        print(f"Predmet '{subject}' bol odstránený.")

    def addGrade(self, subject: str, event_name: str, points: float, base: float) -> None:
        """Add a grade to the specified subject."""
        if subject not in self.__subjects:
            print(f"Predmet '{subject}' neexistuje, nejde pridat znamku.")
            return
        # Append a grade dictionary to the subject's list
        self.__subjects[subject].append({
            "event_name": event_name,
            "points": points,
            "base": base
        })

    def removeGrade(self, event_name: str) -> None:
        """Remove a grade from all subjects if event_name matches."""
        removed_count = 0
        for subject, grades in self.__subjects.items():
            # Filter out the grade with the matching event_name
            initial_len = len(grades)
            self.__subjects[subject] = [g for g in grades if g["event_name"] != event_name]
            removed_count += (initial_len - len(self.__subjects[subject]))
        if removed_count == 0:
            print(f"Znamka s event_name '{event_name}' sa nenasla.")
        else:
            print(f"Odstranili sme {removed_count} hodnotenie/hodnotenia s event_name '{event_name}'.")

    def printAllGrades(self, subject: str = None) -> None:
        """If subject is None, prints all grades from all subjects. Otherwise prints all grades for the given subject."""

        def calc_average(grades_list):
            if not grades_list:
                return 0.0
            total_points = sum(g["points"] for g in grades_list)
            total_base = sum(g["base"] for g in grades_list)
            if total_base == 0:
                return 0.0
            return (total_points / total_base) * 100.0

        def slovne_hodnotenie(average: float) -> str:
            """Return slovne hodnotenie based on average percentage."""
            if average >= 90:
                return "vyborny"
            elif average >= 80:
                return "chvalitebny"
            elif average >= 70:
                return "dobry"
            elif average >= 60:
                return "dostatocny"
            else:
                return "nedostatocny"

        # If subject is None, print for all subjects
        if subject is None:
            for subj, grades in self.__subjects.items():
                print(f"=== Predmet: {subj} ===")
                if not grades:
                    print("Ziadne hodnotenia.")
                else:
                    for g in grades:
                        print(f"Event: {g['event_name']}, Body: {g['points']}/{g['base']}")
                    avg_pct = calc_average(grades)
                    print(f"Priemer: {avg_pct:.2f}%")
                    print(f"Slovne hodnotenie: {slovne_hodnotenie(avg_pct)}")
                print("------------------------")
        else:
            # Print only for the given subject
            if subject not in self.__subjects:
                print(f"Predmet '{subject}' neexistuje.")
                return
            grades = self.__subjects[subject]
            if not grades:
                print(f"Ziaden zaznam pre predmet '{subject}'.")
                return
            print(f"=== Predmet: {subject} ===")
            for g in grades:
                print(f"Event: {g['event_name']}, Body: {g['points']}/{g['base']}")
            avg_pct = calc_average(grades)
            print(f"Priemer: {avg_pct:.2f}%")
            print(f"Slovne hodnotenie: {slovne_hodnotenie(avg_pct)}")

    def store(self, filename: str) -> None:
        """Stores all student information into a file named filename.student."""
        import json
        data = {
            "student_id": self.__student_id,
            "isic_id": self.__isic_id,
            "first_name": self.__first_name,
            "last_name": self.__last_name,
            "class_name": self.__class_name,
            "email": self.__email,
            "subjects": self.__subjects
        }
        with open(f"{filename}.student", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self, filename: str) -> None:
        """Loads all student information from a file named filename.student."""
        import json
        try:
            with open(f"{filename}.student", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.__student_id = data["student_id"]
                self.__isic_id = data["isic_id"]
                self.__first_name = data["first_name"]
                self.__last_name = data["last_name"]
                self.__class_name = data["class_name"]
                self.__email = data["email"]
                self.__subjects = data["subjects"]
        except FileNotFoundError:
            print(f"Subor '{filename}.student' sa nenasiel.")
        except json.JSONDecodeError:
            print(f"Subor '{filename}.student' ma neplatny format.")

if __name__ == "__main__":
    # Example test code
    s = Student(12345, "ISIC12345", "Janko", "Hrasko", "IV.A", "janko.hrasko@example.com")

    s.addSubject("matematika")
    s.addGrade("matematika", "test_1", 8, 10)
    s.addGrade("matematika", "test_2", 6, 10)

    s.addSubject("programovanie")
    s.addGrade("programovanie", "du1", 3, 10)
    s.addGrade("programovanie", "test_1", 9, 10)

    s.printAllGrades()

    s.store("janko_hrasko")
    s.load("janko_hrasko")

    s.printAllGrades("programovanie")
