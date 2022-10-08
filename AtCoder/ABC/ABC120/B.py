from math import sqrt


def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)


def main():

    A, B, K = map(int, input().split())
    Z = gcd(A, B)
    divisor = []
    for i in range(1, int(sqrt(Z)) + 1):
        if Z % i == 0:
            divisor.append(i)
            if i * i != Z:
                divisor.append(Z // i)
    print(sorted(divisor, reverse=True)[K - 1])


if __name__ == "__main__":
    main()
