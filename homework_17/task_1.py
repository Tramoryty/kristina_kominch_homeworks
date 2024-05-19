# 1) Создайте класс Students, содержащий поля:
# фамилия и инициалы,
# номер группы,
# успеваемость (список из пяти элементов).
#
# Создать класс School:
#
# Добавить возможно для добавления студентов в школу
#
# Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 5 или 6.
#
# Добавить возможность вывода учеников заданной группы
#
# Добавить возможность вывода учеников претендующих на автомат(средний балл >= 7)

class Student:
    def __init__(self, surname, initials, group_number, grades):
        self.surname = surname
        self.initials = initials
        self.group_number = group_number
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def is_top_student(self):
        return all(grade in [5, 6] for grade in self.grades)

    def is_eligible_for_automatic(self):
        return self.average_grade() >= 7


class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_top_students(self):
        top_students = [student for student in self.students if student.is_top_student()]
        for student in top_students:
            print(f'{student.surname} {student.initials}, группа: {student.group_number}')

    def get_students_by_group(self, group_number):
        group_students = [student for student in self.students if student.group_number == group_number]
        for student in group_students:
            print(f'{student.surname} {student.initials}, '
                  f'группа: {student.group_number}, '
                  f'оценки: {student.grades}')

    def get_automatic_eligible_students(self):
        eligible_students = [student for student in self.students if student.is_eligible_for_automatic()]
        for student in eligible_students:
            print(f'{student.surname} {student.initials}, '
                  f'группа: {student.group_number}, '
                  f'средний балл: {student.average_grade()}')


school = School()

school.add_student(Student('Иванов', 'И.И.', 101, [5, 5, 6, 5, 6]))
school.add_student(Student('Петров', 'П.П.', 102, [4, 3, 5, 4, 6]))
school.add_student(Student('Сидоров', 'С.С.', 101, [7, 8, 9, 6, 7]))
school.add_student(Student('Кузнецов', 'К.К.', 103, [10, 10, 9, 8, 7]))
school.add_student(Student('Алексеев', 'А.А.', 102, [5, 5, 5, 5, 5]))

print(f'Студенты с оценками 5 или 6:')
school.get_top_students()

print('\nСтуденты группы 101:')
school.get_students_by_group(101)

print(f'\nСтуденты, претендующие на автомат:')
school.get_automatic_eligible_students()
