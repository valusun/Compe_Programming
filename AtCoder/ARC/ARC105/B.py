def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    x = A[0]
    for _, v in enumerate(A, 1):
        x = gcd(x, v)
    print(x)


if __name__ == "__main__":
    main()
