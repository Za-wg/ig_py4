import json
import csv

file_path = input(str('Введите полный путь к файлу:'))

#
# def read_file(name):
#     with open(name, "w+") as f:
#         if (".json" in name):
#             text = ("This text for \"JSON\" file.")
#             json.dump(text, f)
#             json.dumps(name)
#             f.close()
#         elif (".csv" in name):
#             text = [
#                     ["Тетради", 60],
#                     ["Ручки", 25],
#                     ["Карандаши", 30]
#                    ]
#             writer = csv.writer(f)
#             writer.writerows(text)
#             csv.reader(f)
#             f.close()
#         elif (".txt" in name):
#                 f.write("This text for \"TXT\" file.")
#                 f.readlines()
#                 f.close()
#         else:
#             print("Unsupported file format")


def read_file(file_path):
    with open(file_path,  'r', encoding='utf-8'):
        if (".json" in file_path):
            text = json.load(file_path)
            print(text)