import requests
import csv
import json

# ####################################1
FILE_PATH = "/Users/irinagolakova/PycharmProjects/ig_py4/FileCvs.cvs"
url = "http://api.forismatic.com/api/1.0/"


# Написать функцию, которая принимает в виде параметра целое число - количество цитат

def choise_random_int(int):
    for number in range(int):
        params = {"method": "getQuote",
                  "format": "json",
                  "key": number,
                  "lang": "ru"}
        response = requests.get(url, params=params)
        result = response.json()
        for key in result:
            print(f"{key} ------ {result[key]}")


myData = choise_random_int(3)

# !!! Если автор не указан, цитату не брать !!!


def without_author(myData):
    om = [myData.get(key) for key in ('quoteText', 'quoteAuthor', 'quoteLink')]
    return om

list_ = without_author

# !!! Cортировать список в алфавитном порядке !!!


def sortByAlphabet(quoteAuthor):
    return quoteAuthor[0]  # Ключом является первый символ в каждой строке, сортируем по нему


newList = sorted(list_, key=sortByAlphabet)  # Каждый элемент передается в качестве параметра функции


# сохранить их в csv файл

def save_in_file_cvs(FILE_PATH):
    with open(FILE_PATH, "w", encoding="UTF-8"):
        writer = csv.writer(FILE_PATH)
        writer.writerows(newList)

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
