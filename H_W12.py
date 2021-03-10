import random
import requests
import csv
import json

# ####################################1
FILE_NAME = "Wbnfns.csv"
url = "http://api.forismatic.com/api/1.0/"


def choise_random_int(my_quote):
    unique_quotes = []
    params = {
        "method": "getQuote",
        "format": "json",
        "key": random.randint(0, 99999),
        "lang": "ru"
    }

    while len(unique_quotes) < my_quote:
        response = requests.get(url, params=params)
        result = response.json()

        if not result['quoteAuthor']:
            continue

        if result['quoteText'] not in [q['quoteText'] for q in unique_quotes]:
            unique_quotes.append(result)

    unique_quotes = sorted(unique_quotes, key=lambda k: k['quoteAuthor'])

    return unique_quotes


hell = choise_random_int(3)


def save_in_csv_file(FILE_PATH):
    with open(FILE_PATH, "w", encoding="UTF-8"):
        writer = csv.writer(FILE_PATH)
        writer.writerows(hell)


print("First task completed")

# ######################################2


file_path_json = "/Users/irinagolakova/PycharmProjects/ig_py4/authors.json"


# 2.1 написать функцию, которая считывает данные из этого файла

def read_txt(filename="authors.txt"):
    with open(filename, 'r') as file:
        data = []
        for line in file.readlines():
            if line.find("birthday") >= 0 or line.find("death") >= 0:
                data.append(line)
    return data


list_name = read_txt()


# Написать функцию, которая принимает список строк полученной в пункте 2.1, и возвращает список словарей

def parse(line):
    date, info = line.split('-')
    name = info.split(',')[0]
    date = '/'.join(date.split())
    return {'name': name, 'date': date}


two_punkt_two = parse


# Написать функцию, которая сохраняет результат пункта 2 в json файл

def write_in_json_file(file_path):
    with open(file_path, "w") as my_file:
        text = two_punkt_two
        json.dump(text, my_file, indent=2)
