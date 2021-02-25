import json
import csv


def read_file(file_path):
    with open(file_path,  'r'):
        if ".json" in file_path:
            text = json.load(file_path)
            print(text)
            file_path.close()
        elif ".cvs" in file_path:
            text1 = csv.reader(file_path)
            print(text1)
            file_path.close()
        elif ".txt" in file_path:
            with open(file_path, "r") as txt_file:
                data = []
            for line in txt_file.readlines():
                data.append(line)
            file_path.close()
# ###################################2


def file_write(file_path, text):
    file_path = '/Users/irinagolakova/PycharmProjects/ig_py4/PyHw/H_W10'
    with open(file_path, "w+") as f:
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
            json.dump(text, f, indent=2)
        elif ".csv" in file_path:
            names = ["Имя", "Возраст"]
            file_writer = csv.DictWriter(f, delimiter=",", lineterminator="\r", fieldnames=names)
            file_writer.writeheader()
            file_writer.writerow({"Имя": "Саша", "Возраст": "6"})
            file_writer.writerow({"Имя": "Маша", "Возраст": "15"})
            file_writer.writerow({"Имя": "Вова", "Возраст": "14"})
        elif ".txt" in file_path:
            text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
            f.write(text)
        else:
            print("Unsupported file format")
    return text
