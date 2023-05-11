import json


def task():
    filename = "input.json"
    with open(filename) as f1:  # считать содержимое JSON файла
        gen_exr = [f["contains_improvement_appeals"] for f in json.load(f1)]  # записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
