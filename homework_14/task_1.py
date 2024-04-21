# 1) Файл содержит числа и буквы. Каждый записан в
# отдельной строке. Нужно считать содержимое в список
# так, чтобы сначала шли числа по возрастанию, а потом
# слова по возрастанию их длины. (из класса)

with open('task_1.txt', 'r', encoding='utf-8') as file:
    list_read = [i.replace('\n', '') for i in file.readlines()]
    list_num = []
    list_word = []
    for i in list_read:
        if i.isdigit():
            list_num.append(int(i))
        else:
            list_word.append(i)
    list_num.sort()
    list_word.sort(key=len)
    print(f'Отсортированный список: {list_num + list_word}')
