from math import sqrt


def main():
    X = int(input())
    while True:
        for i in range(2, int(sqrt(X)) + 1):
            if X % i == 0:
                X += 1
                break
        else:
            print(X)
            break


if __name__ == "__main__":
    main()
