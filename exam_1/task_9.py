# 9.	Дана строка [“hello my friend”, “my name is”, “house”, “cat”, “dog”].
# В новый список добавить элементы, которые содержат пробел

string_list = ['hello my friend', 'my name is', 'house', 'cat', 'dog']
print(f'Данный список: {string_list}')
new_list = []
for i in string_list:
    if ' ' in i:
        new_list.append(i)
print(f'Новый список с элементами из Данного, которые содержат пробел: {new_list}')
