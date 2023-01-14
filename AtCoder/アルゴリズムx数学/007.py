from math import gcd


def main():
    N, X, Y = map(int, input().split())
    print(N // X + N // Y - (N // (X // gcd(X, Y) * Y)))


if __name__ == "__main__":
    main()
