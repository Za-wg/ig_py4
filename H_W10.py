import json
import csv

file_path = "/Users/irinagolakova/PycharmProjects/ig_py4/authors.json"


def read_file_format(file):
    if file_path.endswith(".json"):
        read_json_file(file)
    elif file_path.endswith(".txt"):
        read_txt_file(file)
    elif file_path.endswith(".cvs"):
        read_cvs_file(file)
    else:
        print("Unsupported file format")


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        json.load(file)
    return file


def read_cvs_file(file_path):
    with open(file_path, 'r') as file:
        csv.reader(file)
    return file


def read_txt_file(file_path):
    with open(file_path, 'r') as file:
        data = []
        for line in file.readlines():
            data.append(line)
    return data


read_file_format()


# ###################################2


def file_write(file_path):
    with open(file_path, 'w') as myfile:
        return myfile


def file_extension(myfile):
    if file_path.endswith(".json"):
        file_write_json(myfile)
    elif file_path.endswith(".txt"):
        file_write_txt(myfile)
    elif file_path.endswith(".cvs"):
        file_write_cvs(myfile)
    else:
        print("Unsupported file format")


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


file_extension()
