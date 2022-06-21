from math import sqrt


def IsPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def CanPrime(c, d, n):
    for i in range(c, d + 1):
        if IsPrime(n + i):
            return True
    return False


def main():
    A, B, C, D = map(int, input().split())
    for i in range(A, B + 1):
        if not CanPrime(C, D, i):
            print("Takahashi")
            break
    else:
        print("Aoki")


if __name__ == "__main__":
    main()
