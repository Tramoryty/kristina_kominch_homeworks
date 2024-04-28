# 1) Создайте функцию, которая принимает на вход список словарей и сохраняет его в CSV файл.
# Каждый словарь представляет собой строку данных, а ключи словарей - названия столбцов.
import csv


def dict_to_csv(dict_list, filename):
    header = set()
    for item in dict_list:
        header.update(item.keys())
    with open(filename, 'w', encoding='cp1251', newline='') as file:
        #это гуглила
        dict_writer = csv.DictWriter(file, fieldnames=header)
        dict_writer.writeheader()
        for item in dict_list:
            dict_writer.writerow(item)


data = [
    {'Имя': 'Иван', 'Фамилия': 'Иванов', 'Возраст': 20},
    {'Имя': 'Мария', 'Email': 'maria@email.com', 'Возраст': 22},
    {'Фамилия': 'Сидоров', 'Возраст': 21, 'Город': 'Москва'}
]

dict_to_csv(data, 'task_2.csv')
