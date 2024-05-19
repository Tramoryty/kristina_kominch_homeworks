# 3) Создать 4 фрукта.
# Апельсин, яблоко, мандарин, банан
# У всех фруктов есть сорт, список витаминов, цена, имя
# У апельсина, мандарина, банана есть метод очистить
# У яблока метод порезать
# У банана есть характеристика: кол-во калия
# Создать 4 объекта фрукта и использовать все доступные методы и характеристики
# При вызове метода очистить, должно писаться имя фрукта
# Например:
# `apple = Apple("sort", [a,b,c], 120, "apple")`
#
# `apple.clear()`
#
# `>>"apple очищен"

class Fruit:
    def __init__(self, sort, vitamins, price, name):
        self.sort = sort
        self.vitamins = vitamins
        self.price = price
        self.name = name

    def __str__(self):
        return f'{self.name} (сорт: {self.sort}, витамины: {', '.join(self.vitamins)}, цена: {self.price} руб)'

    def clear(self):
        pass


class Orange(Fruit):
    def clear(self):
        print(f'{self.name} очищен')


class Apple(Fruit):
    def clear(self):
        print(f'{self.name} порезан')


class Banana(Fruit):
    def __init__(self, sort, vitamins, price, name, potassium_content):
        super().__init__(sort, vitamins, price, name)
        self.potassium_content = potassium_content

    def clear(self):
        print(f'{self.name} очищен')

    def __str__(self):
        return super().__str__() + f', содержание калия: {self.potassium_content} мг'


orange = Orange('Хороший сорт', ['C', 'A', 'B'], 80, 'Апельсин')
apple = Apple('Хороший сорт', ['C', 'B', 'K'], 60, 'Яблоко')
mandarin = Orange('Хороший сорт', ['C', 'B6', 'A'], 70, 'Мандарин')
banana = Banana('Хороший сорт', ['C', 'B6', 'A'], 50, 'Банан', 358)

print(orange)
orange.clear()

print(apple)
apple.clear()

print(mandarin)
mandarin.clear()

print(banana)
banana.clear()
