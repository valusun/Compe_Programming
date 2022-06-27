from math import sqrt


def main():
    A, B = map(int, input().split())
    d = sqrt(A**2 + B**2)
    print(A / d, B / d)


if __name__ == "__main__":
    main()
