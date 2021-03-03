import json
import random
import string

# #####################################1
# Считать данные из файла names.txt и поместить в список только фамилии из файла.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Фамилия находится всегда на одной и той же позиции в строке.

def read_txt():
    with open("names.txt", "r") as file:
        for i in file:
            surname = i.split()[1]
        return surname


data = read_txt()

print(data)

# ############################################2

# Собственно сам полный путь к файлу
file_path = '/Users/irinagolakova/PycharmProjects/ig_py4/PyHw/H_W9.json'

# Создать функцию для записи в файл json
def generate_and_write_json(file_path):
    with open(file_path, 'w') as my_file:
        json.dump(data, my_file, indent= 2)
    return my_file

# Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита (можно с повторениями символов).
def random_key():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(5))


# Значения - или целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1, или True/False. Выбор значения должен быть равновероятным. Т.е. вероятность того, что значение будет целым
# такая же, как и вероятность того, что будет типа float или типа bool.
def random_value():
    value = random.choice([int, bool, float])
    if value == int:
        random.randint(-100, 100)
    elif value == float:
        random.uniform(0, 1)
    elif value == bool:
        random.choice([False, True])
    return value

# Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
def random_dict():
    return {random_key(): random_value() for _ in range(random.randint(5, 20))}


data = random_dict()
