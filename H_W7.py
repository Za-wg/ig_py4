# ##################################1
from random import randint
ran_list = [randint(1, 100) for i in range(20)]
print(ran_list)
print('_____________________________________1')
# #################################2
import random

def create_random_point():
    point = (random.randint(-10, 10),
             random.randint(-10, 10),
             random.randint(-10, 10))
    return point

def print_point(point):
    for key, value in point.items():
        print(f"Name: {key}, point: {value}")

point_a = {"A": create_random_point()}
point_b = {"B": create_random_point()}
point_c = {"C": create_random_point()}

triangle = point_a | point_b | point_c
print(triangle)
print('_____________________________________2')
# # # ################################3
my_str = 'Lorem ipsum'
def my_print():
    return '***' + my_str + "***"
print(my_print())
print('_____________________________________3')
# #################################4
persons = [{"name": "John", "age": 11},
          {"name": "Jo", "age": 51},
          {"name": "Eva", "age": 11},
          {"name": "Jack", "age": 35},
          {"name": "Kate", "age": 15},
          {"name": "Linda", "age": 55},
          {"name": "Galager", "age": 20},
          {"name": "Din", "age": 60}]

all_age = []
for person in persons:
    all_age.append(person["age"])
res = min(all_age)
min_name = []
for person in persons:
    if person["age"] == res:
        min_name.append(person["name"])
print("Минимальный возраст:", min_name)

max_len = int()
for person in persons:
    if len(person['name']) > max_len:
        max_len = len(person['name'])
names_max_len = [person['name'] for person in persons if len(person['name']) == max_len]
print("Самое длинное имя:", names_max_len)

aver_age = [person['age'] for person in persons]
sum_age = sum(aver_age)
res = sum(aver_age) / len(aver_age)
print("Cреднее количество лет:", res)

print('_____________________________________4')
# ######################################5
my_dict_1 = {"maze runner": "part 3", "gold": 2, "hanger game": "part 2", "harry": 367, "break": "all"}
my_dict_2 = {"break": "all", "Sol": "1-2", "gold": 2, "viking": "ser 1"}
# Создать список из ключей, которые есть в обоих словарях.
all_dict = {key: my_dict_2[key] for key in my_dict_1 if my_dict_1[key] == my_dict_2.get(key)}
result = list(all_dict)
print(result)
# Создать список из ключей, которые есть в первом, но нет во втором словаре.
al_dict = []
for key in my_dict_1:
        if key not in my_dict_2:
            al_dict.append(key)
print(al_dict)
# Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре
res = dict((key, my_dict_1[key]) for key in my_dict_1 if key not in my_dict_2)
print(res)
# Объединить эти два словаря в новый словарь по правилу:
# - если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# - если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]}
resu = dict()
for item in my_dict_1.items():
    if item[0] not in my_dict_2:
        resu[item[0]] = item[1]
    else:
        resu[item[0]] = [item[1], my_dict_2[item[0]]]
print(resu)