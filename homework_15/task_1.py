# 1) Файл "books.csv" содержит информацию о книгах в следующем формате:
#
# Название,Автор,Год издания,Жанр,Цена
# Мастер и Маргарита,Михаил Булгаков,1967,Фэнтези,500
# Преступление и наказание,Фёдор Достоевский,1866,Классика,400
# 1984,Джордж Оруэлл,1949,Научная фантастика,350
# Тень горы,Грегори Дэвид Робертс,2007,Триллер,600
#
# Реализовать функцию load_books(file_path), которая загружает данные из файла "books.csv"
# и возвращает список словарей, где каждый словарь представляет информацию о книге.
# Написать функцию total_price(books), которая принимает на вход список книг и
# возвращает общую стоимость всех книг.
# Создать функцию books_by_genre(books, genre), которая выводит на экран названия
# и авторов книг определенного жанра.
# Разработать скрипт, который загружает данные о книгах, вычисляет и выводит их
# общую стоимость, а также список книг определенного жанра, например, "Фэнтези".
import csv


def load_books(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        books_reader = csv.DictReader(file)
        books_data = [book for book in books_reader]
    return books_data


print(load_books('task_1.csv'))


def total_price(books):
    tl_price = 0
    with open('task_1.csv', 'r', encoding='utf-8') as file:
        books = csv.DictReader(file)
        for book in books:
            tl_price += int(book['Цена'])
    return f'Общая стоимость всех книг = {tl_price}'


print(total_price('task_1.csv'))


def books_by_genre(books, genre):
    with open('task_1.csv', 'r', encoding='utf-8') as file:
        books = csv.DictReader(file)
        book_find = {}
        for index, book in enumerate(books):
            if book['Жанр'] == genre:
                book_find[index] = ({'Название': book['Название'], 'Автор': book['Автор']})
    return list(book_find.values())


print(books_by_genre('task_1.csv', genre=input('Введите жанр: ').capitalize()))


def books_by(books, genre):
    return f'{total_price(books)}\nСписок книг жанра {genre}: {books_by_genre(books, genre)}'


print(books_by('task_1.csv', genre=input('Введите жанр: ').capitalize()))
