def gcd(x, y):
    return y if x % y == 0 else gcd(y, x % y)


def main():
    A, B = map(int, input().split())
    print(A // gcd(A, B) * B)


if __name__ == "__main__":
    main()
