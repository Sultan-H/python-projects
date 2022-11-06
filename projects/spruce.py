
def spruce(size):
    print("a spruce!")
    new = size - 1
    times = 1
    while new >= 0:
        print(" " * new + "*" * times)
        new -= 1
        times += 2
    print(" " * (size - 1) + "*")


if __name__ == "__main__":
    spruce(int(input("size: ")))