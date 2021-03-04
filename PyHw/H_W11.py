import json
import re

file_path = '/Users/irinagolakova/PycharmProjects/ig_py4/PyHw/data.json'


# Необходимо написать функцию, которая считает эти данные из файла
def read_json_file(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        text = json.load(file)
    return text

# Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть)


def sort_by_surname(x):
    sotr = x['name'].split(" ")[-1]
    return sort

sort_surname = sorted(sotr, key=sort_by_surname)
                      
# Написать функцию сортировки по дате смерти из поля "years"


def sort_by_death(a: str) -> int:
    year = re.match(".+\s(\d+)\D*$", a).group(1)
    year = -int(year) if ("bc" in a.lower()) else int(year)
    return year


res = sorted(file_path, key=sort_by_death)

# Написать функцию сортировки по количеству слов в поле "text"


def sort_by_len(file):
    lines = [sorted(line.rstrip().split(), key=len) for line in file]
    return lines


