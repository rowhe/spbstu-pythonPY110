def task() -> list:
    temp_tuple = (0, 36.6, 100)
    for i in temp_tuple:
       tuple_ = tuple(int(i * 9/5 + 32))  #  вернуть список температур по Фаренгейту
    return list_

if __name__ == "__main__":
    print(task())
