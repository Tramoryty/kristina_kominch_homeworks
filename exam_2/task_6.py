# 6) Класс «Сотрудник компании» Worker
# Экземпляр класса при инициализации принимает аргументы:
# имя, должность и стаж работы сотрудника, метод print_info()
# выводит информацию о сотруднике в формате: «Имя: Василий Должность:
# Системный администратор :Стаж: 3 года» При выводе стажа нужно учитывать,
# что «года» должно заменяться на «лет» или «год» в зависимости от числа.
# worker1 = Worker("Алексей", "Программист", 17)
#  worker1.print_info()
# worker2 = Worker("Анна", "Маркетолог", 2)
# worker2.print_info()
# worker3 = Worker("Дмитрий", "Аналитик", 1)
# worker3.print_info()

class Worker:
    def __init__(self, name, position, years_of_experience):
        self.name = name
        self.position = position
        self.years_of_experience = years_of_experience

    def print_info(self):
        years_str = self._format_years(self.years_of_experience)
        print(f'Имя: {self.name} Должность: {self.position} Стаж: {self.years_of_experience} {years_str}')

    @staticmethod
    def _format_years(years):
        if 11 <= years % 100 <= 19:
            return 'лет'
        if years % 10 == 1:
            return 'год'
        if 2 <= years % 10 <= 4:
            return 'года'
        return 'лет'


worker1 = Worker('Алексей', 'Программист', 17)
worker1.print_info()

worker2 = Worker('Анна', 'Маркетолог', 2)
worker2.print_info()

worker3 = Worker('Дмитрий', 'Аналитик', 1)
worker3.print_info()
