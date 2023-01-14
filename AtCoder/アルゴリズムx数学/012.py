from math import sqrt


def main():
    n = int(input())
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            print("No")
            break
    else:
        print("Yes")


if __name__ == "__main__":
    main()
