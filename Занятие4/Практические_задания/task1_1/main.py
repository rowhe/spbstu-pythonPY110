import re


def task():
    word_list = [
        ",./ sdfsdf",
        "Ddfsdf",
        "@@##,sdfsdf",
        "123_sdfsdf",
        "123sdfsdf",
        ", s,dfsdf",
        "123, fewfew",
    ]

    word_pattern = re.compile(r'\w+')  #  записать регулярное выражение для поиска слова любой длины

    # for word in word_list:
    print(word_pattern.search())
        # print(word_pattern.findall(word))  #  вызвать от регулярного выражения методы search и group
        # print(word_pattern.search(word).group())
        # print(word_pattern.search(word).group())

if __name__ == "__main__":
    task()
