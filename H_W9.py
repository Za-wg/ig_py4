import os
import json
import random
import string
#
#
# def read_txt():
#     with open("names.txt", "r") as names:
#         data = names.read().split('\n')
#         for i, item in enumerate(data):
#             if item != '\n':
#                 data[i] = item.split('\t')
#         return data
#
#
# def get_last_name(data):
#     last_name_list = [lists[1] for lists in data]
#     return last_name_list
#
#
# data = read_txt()
# data = get_last_name(data)
#
# print(data)
# #####################################2


def generate_and_write_json():
    file_path = os.path.abspath('PyHw/H_W9.json')
    return file_path


def add_last_name_in_file():
    file = generate_and_write_json()
    with open(file, "w", encoding="utf-8") as my_file:
        json.dump(data, my_file, indent=2)
    return my_file


def random_key():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(5))


def random_value():
    value = random.choice([int, bool, float])
    for result in value:
        if value == int:
            random.randint(-100, 100)
        elif value == float:
            random.uniform(0, 1)
        elif value == bool:
            random.choice([False, True])
    return result


def random_dict():
    return {random_key(): random_value() for _ in range(random.randint(5, 20))}


data = random_dict()

