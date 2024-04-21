# 3) В текстовом файле посчитать количество строк,
# а также для каждой отдельной строки определить
# количество в ней символов.

with open('task_3.txt', 'r', encoding='cp1251') as file:
    lines = file.readlines()
    print(f'Количество строк в файле: {len(lines)}')
    for index, line in enumerate(lines):
        print(f'В {index + 1}-й строке {len(line.strip())} символа(ов)')
