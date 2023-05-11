import json


def task():
    filename = "input.json"
    with open(filename) as f1:
        load_f1 = json.load(f1)
        # print(load_f1)
    return max(load_f1, key=lambda num: num["score"])  # найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
