from math import sqrt


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def main():
    N = int(input())
    print("Yes" if is_prime(N) else "No")


if __name__ == "__main__":
    main()
