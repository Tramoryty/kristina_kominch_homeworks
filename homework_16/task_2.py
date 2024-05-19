# 2) Вы идете в путешествие, надо подсчитать сколько у денег у каждого студента.
# Класс студен описан следующим образом:
#
# class Student:
#     def __init__(self, name, money):
#        self.name = name
#        self.money = money

class Student:
    def __init__(self, name, money: float):
       self.name = name.title()
       self.money = money

    @staticmethod
    def total_money(students):
        total_money = sum(student.money for student in students)
        return total_money


all_students = []
num_students = int(input('Введите количество студентов: '))

for i in range(num_students):
    name_student = input(f'Введите имя студента {i + 1}: ')
    money_student = float(input(f'Введите количество денег у студента {i + 1}: '))
    all_students.append(Student(name_student, money_student))

for student_num in all_students:
    print(f'Студент {student_num.name} имеет {student_num.money} денег')

all_money = Student.total_money(all_students)
print(f'Общая сумма денег у всех студентов: {all_money}')
