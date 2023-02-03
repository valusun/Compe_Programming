from math import sqrt


def solve(n):
    for x in range(2, int(sqrt(n) + 1)):
        if n % x**2 == 0:
            return x, n // x**2
        elif n % x == 0:
            return int(sqrt(n // x)), x


def main():
    T = int(input())
    for _ in range(T):
        print(*solve(int(input())))


if __name__ == "__main__":
    main()
