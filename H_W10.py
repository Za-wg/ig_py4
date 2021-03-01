import json
import csv


def choose_format_file_reading(file_path):
    with open(file_path, 'r') as file:
        if ".json" in file_path:
            read_json_file(file)
        elif ".cvs" in file_path:
            read_cvs_file(file)
        elif ".txt" in file_path:
            read_txt_file(file)
        else:
            print("Unsupported file format")
    return file


def read_json_file(file):
    json.load(file)
    return file


def read_cvs_file(file):
    csv.reader(file)
    return file


def read_txt_file(file):
    data = []
    for line in file.readlines():
        data.append(line)
    return file_path

# ###################################2


file_path = '/Users/irinagolakova/PycharmProjects/ig_py4/PyHw/Py9.json'


def choose_format_file_for_write(file_path):
    with open(file_path, 'w') as myfile:
        if ".json" in file_path:
            file_write_json(myfile)
        elif ".cvs" in file_path:
            file_write_cvs(myfile)
        elif ".txt" in file_path:
            file_write_txt(myfile)
        else:
            print("Unsupported file format")
    return myfile


def file_write_json(myfile):
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
        json.dump(text, myfile, indent=2)


def file_write_cvs(myfile):
        names = ["Имя", "Возраст"]
        file_writer = csv.DictWriter(myfile, delimiter=",", lineterminator="\r", fieldnames=names)
        file_writer.writeheader()
        file_writer.writerow({"Имя": "Саша", "Возраст": "6"})
        file_writer.writerow({"Имя": "Маша", "Возраст": "15"})
        file_writer.writerow({"Имя": "Вова", "Возраст": "14"})


def file_write_txt(myfile):
        text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
        myfile.write(text)
