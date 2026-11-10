class Student:
    def __init__(self, name, major, gpa_for_semesters):
        self.name = name
        self.major = major
        self.__gpa_for_semesters = gpa_for_semesters

    def __str__(self):
        return f"{self.name} is studying {self.major}."

    def get_gpa(self):
        return self.__gpa_for_semesters

    def set_gpa(self, new_value):
        self.__gpa_for_semesters = new_value

    def calculate_average_gpa(self):
        return sum(self.__gpa_for_semesters) / len(self.__gpa_for_semesters)

    def is_in_good_standing(self):
        return f"{self.name} is a student."


class UndergraduateStudent(Student):
    def __str__(self):
        return f"{self.name} is an undergraduate student studying {self.major}."

    def is_in_good_standing(self):
        if self.calculate_average_gpa() >= 2.5:
            return f"{self.name} is in good academic standing."
        else:
            return f"{self.name} is not in good academic standing."


class GraduateStudent(Student):
    def __str__(self):
        return f"{self.name} is a graduate student studying {self.major}."

    def is_in_good_standing(self):
        if self.calculate_average_gpa() >= 3.0:
            return f"{self.name} is in good academic standing."
        else:
            return f"{self.name} is not in good academic standing."


# Example testing
if __name__ == "__main__":
    student1 = Student("John", "Computer Science", [3.5, 4.0, 3.0])
    student2 = Student("Becky", "Mathematics", [2.5, 3.0, 3.5, 4.0, 3.0])
    undergrad1 = UndergraduateStudent("Adama", "Marketing", [2.0, 3.3, 3.5])
    graduate1 = GraduateStudent("Ivan", "Math", [2.0, 3.3, 3.5])

    print(student1)
    print(student1.calculate_average_gpa())
    print(student2.is_in_good_standing())

    print(undergrad1)
    print(undergrad1.is_in_good_standing())

    print(graduate1)
    print(graduate1.is_in_good_standing())
