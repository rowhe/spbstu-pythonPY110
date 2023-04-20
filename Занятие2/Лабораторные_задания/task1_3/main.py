def task(numbers: list) -> int:
    return sum(i ** 3 for i in numbers if i < 0)


if __name__ == "__main__":
    list_numbers = [-2, -1, 0, 1, -3, 2, -3]
    print(task(list_numbers))
