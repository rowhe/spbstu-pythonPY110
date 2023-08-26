def pow_gen(base: int):
    pows = 0
    while True:
        yield base ** pows
        pows += 1
    return None #  записать функцию-генератор


if __name__ == "__main__":
    pow_numbers = pow_gen(10)

    for _ in range(5):
        print(next(pow_numbers))
