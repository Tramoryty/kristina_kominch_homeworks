# 7) Класс ПЕРСОНА, экземпляр класса инициализируется аргументами фамилия, дата
# рождения и содержит методы, позволяющие вывести информацию о персоне, а также определить ее возраст.
# Дочерние классы: АБИТУРИЕНТ (фамилия, дата рождения, факультет),
# СТУДЕНТ(фамилия, дата рождения, факультет, курс), ПРЕПОДАВАТЕЛЬ (фамилия, дата рождения,
# факультет, должность, стаж), содержат свои методы вывода информации.
# Создайте список из n персон, выведите полную информацию из базы, а также
# организуйте поиск персон, чей возраст попадает в заданный диапазон.

from datetime import date, datetime


class Person:
    def __init__(self, surname, birth_date):
        self.surname = surname
        self.birth_date = datetime.strptime(birth_date, '%d.%m.%Y').date()

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age

    def print_info(self):
        print(f'Фамилия: {self.surname}, '
              f'Дата рождения: {self.birth_date.strftime('%d.%m.%Y')}, '
              f'Возраст: {self.get_age()} лет')


class Abiturient(Person):
    def __init__(self, surname, birth_date, faculty):
        super().__init__(surname, birth_date)
        self.faculty = faculty

    def print_info(self):
        super().print_info()
        print(f'Факультет: {self.faculty}')

class Student(Person):
    def __init__(self, surname, birth_date, faculty, course):
        super().__init__(surname, birth_date)
        self.faculty = faculty
        self.course = course

    def print_info(self):
        super().print_info()
        print(f'Факультет: {self.faculty}, Курс: {self.course}')


class Teacher(Person):
    def __init__(self, surname, birth_date, faculty, position, experience):
        super().__init__(surname, birth_date)
        self.faculty = faculty
        self.position = position
        self.experience = experience

    def print_info(self):
        super().print_info()
        print(f'Факультет: {self.faculty}, Должность: {self.position}, Стаж: {self.experience} лет')


def print_all_info(persons):
    for person in persons:
        person.print_info()
        print()


def find_persons_by_age(persons, min_age, max_age):
    return [person for person in persons if min_age <= person.get_age() <= max_age]


persons = [
    Abiturient('Иванов', '15.04.2003', 'Физика'),
    Student('Петров', '20.06.2001', 'Информатика', 3),
    Teacher('Сидоров', '10.02.1980', 'Математика', 'Профессор', 15),
    Abiturient('Смирнов', '30.08.2004', 'Химия'),
    Student('Кузнецов', '12.12.2002', 'Биология', 2)
    ]

print('Полная информация о всех персона:')
print_all_info(persons)

print('Поиск персон по возрастному диапазону (20-40 лет):')
found_persons = find_persons_by_age(persons, 20, 40)
print_all_info(found_persons)
