from math import sqrt


def divisor(n: int):
    """約数を返す

    Args:
        n (int): 約数を求める数
    """

    ret = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            ret.append(i)
            if n // i != i:
                ret.append(n // i)
    return sorted(ret)


def main():
    S, P = map(int, input().split())
    divisor_P = divisor(P)
    for n in divisor_P:
        m = P // n
        if n + m == S:
            print("Yes")
            exit()
    print("No")


if __name__ == "__main__":
    main()
