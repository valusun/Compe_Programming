def gcd(x, y):
    return y if x % y == 0 else gcd(y, x % y)


def main():
    A, B, C = map(int, input().split())
    x = gcd(gcd(A, B), C)
    print((A // x - 1) + (B // x - 1) + (C // x - 1))


if __name__ == "__main__":
    main()
