from itertools import count


def task():
    counter = count(100, 10)

    for i in range(10):
        # next_ = next(counter)
        print(next(counter))

if __name__ == "__main__":
    task()
