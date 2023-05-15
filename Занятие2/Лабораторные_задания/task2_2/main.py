import itertools

def count(start_number: float = 1, step: float = 1):

    for i in itertools.count(start_number, step):
        print(i)
        if i > 14:  #  написать функцию-генератор возвращающую целые числа
            break


# count()

if __name__ == "__main__":
    my_count = count(10, 0.5)
    print(count(my_count))