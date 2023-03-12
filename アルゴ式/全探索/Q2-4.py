def gcd(x, y):
    return y if x % y == 0 else gcd(y, x % y)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
