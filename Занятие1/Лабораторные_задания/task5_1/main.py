def task():
    numbers = [1, 2, 3, 4, 5]
    chars = ["a", "b", "c", "d", "e"]
#    print(list((zip(numbers, chars))))
    for number, char in zip(numbers, chars):  # поэлементно объединить numbers и chars
        print(f"{number}-{char}")


if __name__ == "__main__":
    task()
