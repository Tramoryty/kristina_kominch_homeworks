# 5) Класс «Волшебник» (Wizard)
# Экземпляр класса при инициализации принимает аргументы:
# – имя;
# – рейтинг;
# – на какой возраст выглядит.
# Класс должен обеспечивать функциональность:
# – change_rating(value) – изменять рейтинг на значение value; не может стать больше 100 и
# меньше 1, изменяется только до достижения экстремального значения; при увеличении
# рейтинга уменьшается возраст на abs(value) // 10, но только до 18, дальше не уменьшается;
# при уменьшении рейтинга возраст соответственно увеличивается;
# – к экземпляру класса можно прибавить строку: (wd += string), значение рейтинга
# увеличивается на ее длину, а возраст, соответственно, уменьшается на длину // 10, условия
# изменения такие же;
# – экземпляр класса можно вызвать с аргументом-числом; возвращает значение: (аргумент
# - возраст) * рейтинг;
# __str__() – возвращает строку:
# “Wizard <name> with <rating> rating looks <age> years old”
# – экземпляры класса можно сравнивать: сначала по рейтингу, затем по возрасту, затем по
# имени по алфавиту; для этого нужно реализовать методы сравнения: <, >, <=, >=, ==, !=.

class Wizard:
    def __init__(self, name, rating, age):
        self.name = name
        self.rating = max(1, min(rating, 100))
        self.age = max(age, 18)

    def change_rating(self, value):
        new_rating = self.rating + value
        if new_rating > 100:
            value = 100 - self.rating
            self.rating = 100
        elif new_rating < 1:
            value = 1 - self.rating
            self.rating = 1
        else:
            self.rating = new_rating

        age_change = abs(value) // 10
        if value > 0:
            self.age = max(self.age - age_change, 18)
        elif value < 0:
            self.age += age_change

    def add_string_length_to_rating(self, string):
        length = len(string)
        self.change_rating(length)

    def calculate_magic_power(self, number):
        return (number - self.age) * self.rating

    def __str__(self):
        return f'Wizard {self.name} with {self.rating} rating looks {self.age} years old'

    def compare_wizards(self, other):
        if self.rating == other.rating:
            if self.age == other.age:
                return self.name < other.name
            return self.age < other.age
        return self.rating < other.rating

    def is_greater_than(self, other):
        return not self.compare_wizards(other) and not self.is_equal_to(other)

    def is_equal_to(self, other):
        return self.rating == other.rating and self.age == other.age and self.name == other.name

    def is_not_equal_to(self, other):
        return not self.is_equal_to(other)


wizard1 = Wizard("Gandalf", 90, 50)
wizard2 = Wizard("Merlin", 80, 40)

wizard1.change_rating(15)
print(wizard1)

wizard2.change_rating(-50)
print(wizard2)

wizard1.add_string_length_to_rating("magic")
print(wizard1)

result = wizard1.calculate_magic_power(60)
print(result)

print(wizard1.is_greater_than(wizard2))
print(wizard2.is_greater_than(wizard1))
print(wizard1.is_equal_to(wizard2))
print(wizard1.is_not_equal_to(wizard2))
