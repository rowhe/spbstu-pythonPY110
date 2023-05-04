OUTPUT_FILE = "output.txt"


def task():
    with open(OUTPUT_FILE, "w") as file:
        counter = 10
        for i in range(1, 11):
            counter -= 1
            file.write(" " * counter + "*" * i + "\n")



if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
