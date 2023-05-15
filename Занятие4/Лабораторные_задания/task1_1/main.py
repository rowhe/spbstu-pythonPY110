import json
import re

BOOKS_FILE = "books.md"
BOOK_REGEX = re.compile(r'^#+\s(?P<position>.+?).\s\[(?P<book>.+?)]\((?P<url>.+?)\)\sby\s(?P<author>.+?)\((?P<recommended>.+?)\srecommended\)\n{1,2}^!\[]\((?P<cover_url>.+?)\)\n{1,2}\"(?P<description>.+?)\"')  # записать ругулярное выражения для поиска книги

def task():
    book_pattern = BOOK_REGEX
#    book_pattern = re.compile(BOOK_REGEX, re.DOTALL) # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки

    with open(BOOKS_FILE) as f:
        for book in book_pattern.finditer(f.read()):
            print(json.dumps(book.groupdict(), indent=4))


if __name__ == '__main__':
    task()
