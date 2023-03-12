from math import sqrt


def get_divisor(n):
    ret = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            ret.append(i)
            if i * i != n:
                ret.append(n // i)
    return ret


def main():
    N = int(input())
    print(len(get_divisor(N)))


if __name__ == "__main__":
    main()
