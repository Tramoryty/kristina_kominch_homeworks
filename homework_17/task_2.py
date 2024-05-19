# 2) Создайте класс Робот
#
#     создайте 2 типа оружия: меч, автомат
#
#     Создайте 2 типа амуниции: броня, шлем
#
#     Добавьте оружию и амуниции свои характеристики(например урон, прочность)
#
#     Создайте своего робота с каким либо оружием
#
#     (может быть несколько и брони может быть несколько. Так же может быть ничего)
#
#     Выведите весь арсенал робота на экран

class Robot:
    def __init__(self, name):
        self.name = name
        self.weapons = []
        self.armors = []

    def add_weapon(self, name, damage):
        weapon = {'name': name, 'damage': damage}
        self.weapons.append(weapon)

    def add_armor(self, name, durability):
        armor = {'name': name, 'durability': durability}
        self.armors.append(armor)

    def show_arsenal(self):
        print(f'Арсенал робота {self.name}:')
        if self.weapons:
            print('Оружие:')
            for weapon in self.weapons:
                print(f'  - {weapon['name']} (Урон: {weapon['damage']})')
        else:
            print('  - Нет оружия')

        if self.armors:
            print('Амуниция:')
            for armor in self.armors:
                print(f'  - {armor['name']} (Прочность: {armor['durability']})')
        else:
            print('  - Нет амуниции')


robot = Robot('Робот-воин')

robot.add_weapon('Меч', 50)
robot.add_weapon('Автомат', 100)
robot.add_armor('Броня', 200)
robot.add_armor('Шлем', 100)

robot.show_arsenal()
