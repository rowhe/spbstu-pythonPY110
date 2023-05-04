INPUT_FILE = "input.txt"


def task() -> None:
    with open(INPUT_FILE, "rt") as file:  #  открыть указатель на файл
        for line in file:
            print(line.rstrip())#  файл является итератором, который работает с циклом for в построчном режиме


if __name__ == "__main__":
    task()
