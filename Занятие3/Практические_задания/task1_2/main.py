# -*- coding: cp1251 -*-
def task():
    list_words = ["����", "���", "���"]

    filename = "output.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for word in list_words:
            f.write(word + "\n")  # � ������� ������ write �������� ��������� ���������� ������

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            print(line)


if __name__ == "__main__":
    task()
