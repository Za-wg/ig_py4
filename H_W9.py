import os
import json
import pprint
import random
import string
#
#
# def read_txt():
#     with open("names.txt", "r") as names:
#         data = names.read().split('\n')
#         datacount = 0
#         for i, item in enumerate(data):
#             if item != '\n':
#                 datacount += 1
#                 data[i] = item.split('\t')
#         return data
#
#
# def polychi_fam(data):
#     last_name_list = []
#     for lists in data:
#         last_name_list.append(lists[1])
#     return last_name_list
#
#
# data = read_txt()
# data = polychi_fam(data)
#
# print(data)
# #####################################2


def random_key():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(5))


def random_value():
    a = random.randint(-100, 100)
    b = random.uniform(0, 1)
    c = random.choice([False, True])
    return random.choice([a, b, c])


def random_dict():
    return {random_key(): random_value() for _ in range(random.randint(5, 20))}


a_dict = random_dict()
pprint.pprint(random_dict())

with open('H_W9.json') as f:
    data = json.load(f)

data.update(a_dict)

with open('H_W9.json', 'w') as f:
    json.dump(data, f)
