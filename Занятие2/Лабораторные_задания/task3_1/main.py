def positive_check(fn):
    def wrapper(arg):
        if arg < 0:  # написать проверку положительности аргумента arg
            raise ValueError("Аргумент функции не является положительным числом")
        result = fn(arg)
        return result

    return wrapper


 #декорировать функцию
def some_func(num: int):

    positive_check()


if __name__ == "__main__":
    some_func(5)  # всё хорошо

    some_func(-5)  # должна быть вызвана ошибка ValueError
