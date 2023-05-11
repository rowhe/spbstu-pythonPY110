def task() -> list:
    temp_tuple = (0, 36.6, 100)
    result = [(i * 9/5) + 32 for i in temp_tuple]
    #  вернуть список температур по Фаренгейту
    return result

if __name__ == "__main__":
    print(task())
