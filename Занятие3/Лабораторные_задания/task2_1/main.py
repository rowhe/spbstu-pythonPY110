import json


def task() -> str:
    dict_numbers = {}
    # for i in range(1,11):
    #     dict_numbers[i] = i ** 2
    dict_numbers = { i:i**2 for i in range(1,11)}#  c помощью dict comprehension сформировать словарь
    return json.dumps(dict_numbers, indent=4)  # сеализовать словарь в JSON строку



if __name__ == "__main__":
    print(task())
