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
    sort_surname = sorted(sotr, key=sotr)
    return sort_surname

# Написать функцию сортировки по дате смерти из поля "years"


def sort_by_death(a: str) -> int:
    year = re.match(".+\s(\d+)\D*$", a).group(1)
    year = -int(year) if ("bc" in a.lower()) else int(year)
    return year


res = sorted(file_path, key=lambda x: sort_by_death(x["years"]))

# Написать функцию сортировки по количеству слов в поле "text"


def sort_key_by_name(sort_dict):
    value = sort_dict["text"]
    return value


def sort_key_by_len_name(sort_dict):
    return len(sort_dict["text"])


result = sorted(file_path, key=sort_key_by_len_name)
print(result)


