def gen(start_, denom):

    for _ in range(10):
        print(start_)
        prev = start_
        cur = prev * denom
        start_ = cur



if __name__ == "__main__":
    # Write your solution here
    start = 1
    denominitor = 7
    gen(start, denominitor)
