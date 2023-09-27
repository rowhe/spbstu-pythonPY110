if __name__ == "__main__":
    with open("input1.txt") as f1:  # Write your solution here
        lines1 = f1.read()
    with open("input2.txt") as f2:
        lines2 = f2.read()
    with open("output.txt", "w") as f3:
        f3.write(lines1 + "\n" + lines2)
