from itertools import count


def task():
    num = 2 ** 0  # 1
    # TODO с помощью yield вернуть первое число

    for i in count(0, 1):
        yield 2 ** i


if __name__ == "__main__":
    numbers = task()

    for _ in range(11):
        print(next(numbers))
