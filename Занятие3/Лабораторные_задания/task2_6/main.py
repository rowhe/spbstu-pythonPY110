import json


def task():
    filename = "input.json"
    with open(filename) as f:
        json_data = json.load(f)

    return sorted(json_data, key=lambda x: x["length"])  # отсортировать список словарей


if __name__ == "__main__":
    data = task()
    print(json.dumps(data, indent=4))

    with open("output.json", "w") as f2:  # дополнительно записать отсортированный список в JSON файл
        json.dump(data, f2, indent=4)
