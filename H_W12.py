import random
import requests
import csv
import json

# ####################################1
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


def save_in_csv_file(FILE_PATH="Wbnfns.csv"):
    with open(FILE_PATH, "w", encoding="UTF-8") as f:
        writer = csv.writer(f)
        writer.writerows(hell)


save_in_csv_file()

print("First task completed")

# ####################################2

filename = "authors.txt"
file_path = "/Users/irinagolakova/PycharmProjects/ig_py4/eliFFile.json"


def read_txt():
    with open(filename, 'r') as file:
        data = []
        for line in file.readlines():
            if line.find("birthday") >= 0 or line.find("death") >= 0:
                data.append(line)
    return data


read_txt()


def main():
    result_data = []
    for line in read_txt():
        date, info = line.split(sep="-", maxsplit=1)
        name = info.split("'s ")[0]
        date = '/'.join(date.split())
        result_data.append({'name': name, 'date': date})
    return result_data


res = main()


def write_in_json_file(data):
    with open(file_path, "w") as my_file:
        json.dump(data, my_file, indent=2)


write_in_json_file(res)

print("The second task is completed")
