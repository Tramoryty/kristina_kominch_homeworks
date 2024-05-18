# 4) Напишите программу с классом Student, в котором есть
# три атрибута: name, groupNumber и age. По умолчанию name = Ivan, age = 18, groupNumber = 10A.
# Необходимо создать пять методов: getName, getAge, getGroupNumber, setNameAge, setGroupNumber.
# Метод getName нужен для получения данных об имени конкретного студента, метод getAge нужен
# для получения данных о возрасте конкретного студента, vетод setGroupNumberнужен для получения
# данных о номере группы конкретного студента. Метод SetNameAge позволяет изменить данные атрибутов
# установленных по умолчанию, метод setGroupNumber позволяет изменить номер группы установленный по
# умолчанию. В программе необходимо создать пять экземпляров класса Student,
# установить им разные имена, возраст и номер группы.

class Student:
    def __init__(self, name='Ivan', age=18, groupNumber='10A'):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber


student1 = Student()
student2 = Student()
student3 = Student()
student4 = Student()
student5 = Student()

student1.setNameAge('Alex', 19)
student1.setGroupNumber('10B')

student2.setNameAge('Maria', 20)
student2.setGroupNumber('11A')

student3.setNameAge('John', 21)
student3.setGroupNumber('12A')

student4.setNameAge('Anna', 18)
student4.setGroupNumber('10C')

student5.setNameAge('Michael', 22)
student5.setGroupNumber('11B')

print(f'Student 1: {student1.getName()}, Age: {student1.getAge()}, Group: {student1.getGroupNumber()}')
print(f'Student 2: {student2.getName()}, Age: {student2.getAge()}, Group: {student2.getGroupNumber()}')
print(f'Student 3: {student3.getName()}, Age: {student3.getAge()}, Group: {student3.getGroupNumber()}')
print(f'Student 4: {student4.getName()}, Age: {student4.getAge()}, Group: {student4.getGroupNumber()}')
print(f'Student 5: {student5.getName()}, Age: {student5.getAge()}, Group: {student5.getGroupNumber()}')
