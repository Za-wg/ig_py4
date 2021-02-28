import json

file_path = '/Users/irinagolakova/PycharmProjects/ig_py4/PyHw/data.json'


# Необходимо написать функцию, которая считает эти данные из файла
def read_json_file(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        text = json.load(file)
    return text

# Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть)


def func(x):
    return x['name'].split()[-1]


def sort_by_surname(file_path):
    surname = sorted(file_path, key=func)
    sort_surname = sorted(file_path, key=abs(surname))
    print(sort_surname)

# Написать функцию сортировки по дате смерти из поля "years"


def key(file_path):
    year = file_path["years"].split("–")[1]
    if len(year.split()) == 1:
        return int(year.split()[0][:-1])
    return -int(year.split(" ")[-2])


new_data = sorted(file_path, key=key)
print(*file_path, sep="\n")

# Написать функцию сортировки по количеству слов в поле "text"


def sort_key_by_name(sort_dict):
    value = sort_dict["text"]
    return value


def sort_key_by_len_name(sort_dict):
    return len(sort_dict["text"])


result = sorted(file_path, key=sort_key_by_len_name)
print(result)


