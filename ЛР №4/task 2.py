import csv
import json


def main():
    csv_to_json("input.csv", "output.json")


if __name__ == '__main__':
    with open("output.json") as output_f:
        for line in output_f:
            print(line, end="")

def csv_to_json(csv_file_path, json_file_path):
    # Открываем CSV файл для чтения
    with open(csv_file_path, 'r') as csv_file:
        # Используем DictReader для чтения CSV и создания словарей для каждой строки
        csv_reader = csv.DictReader(csv_file)

        # Создаем список для хранения словарей (записей)
        data = []

        # Проходим по каждой строке в CSV и добавляем словарь в список
        for row in csv_reader:
            data.append(row)

    # Открываем JSON файл для записи
    with open(json_file_path, 'w') as json_file:
        # Используем json.dump для записи списка словарей в JSON файл с отступами
        json.dump(data, json_file, indent=4)