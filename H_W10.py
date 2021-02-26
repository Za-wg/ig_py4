import json
import csv


def read_json_file(file_path):
    with open(file_path,  'r'):
        if ".json" in file_path:
            json.load(file_path)
    return file_path


def read_cvs_file(file_path):
    with open(file_path, 'r'):
        if ".cvs" in file_path:
            csv.reader(file_path)
    return file_path


def read_txt_file(file_path):
    with open(file_path, "r") as txt_file:
        if ".txt" in file_path:
            data = []
            for line in txt_file.readlines():
                data.append(line)
    return file_path

# ###################################2


file_path = '/Users/irinagolakova/PycharmProjects/ig_py4/PyHw/Py9.json'


def file_write_json(file_path):
    with open(file_path, "w") as my_file:
        if ".json" in file_path:
            text = {"People": [
                {
                    "name": "Jhon",
                    "age": 21
                },
                {
                    "name": "Ruta",
                    "age": 19
                }
                    ]}
            json.dump(text, my_file, indent=2)


def file_write_cvs(file_path):
    with open(file_path, "w") as my_file:
        if ".csv" in file_path:
            names = ["Имя", "Возраст"]
            file_writer = csv.DictWriter(my_file, delimiter=",", lineterminator="\r", fieldnames=names)
            file_writer.writeheader()
            file_writer.writerow({"Имя": "Саша", "Возраст": "6"})
            file_writer.writerow({"Имя": "Маша", "Возраст": "15"})
            file_writer.writerow({"Имя": "Вова", "Возраст": "14"})


def file_write_txt(file_path):
    with open(file_path, "w") as my_file:
        if ".txt" in file_path:
            text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
            my_file.write(text)
