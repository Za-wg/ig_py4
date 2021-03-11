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

# ####################################2

filename = "authors.txt"
file_path = "/Users/irinagolakova/PycharmProjects/ig_py4/12json.json"


def read_txt():
    with open(filename, 'r') as file:
        data = []
        for line in file.readlines():
            if line.find("birthday") >= 0 or line.find("death") >= 0:
                data.append(line)
    return data


def main():
    for line in read_txt():
        dats, info = line.split('-')
        name = info.split(',')[0]
        dats = '/'.join(dats.split())
        print({'name': name, 'dats': dats})


main()


def write_in_json_file():
    with open(file_path, "w") as my_file:
        text = main
        json.dump(text, my_file, indent=2)


