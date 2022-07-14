from math import sqrt


def GetDigit(num: int) -> int:
    """桁数を返す"""

    return len(str(num))


def main():
    N = int(input())
    ans = 10**10
    for i in range(1, int(sqrt(N) + 1)):
        if N % i == 0:
            ans = min(ans, max(GetDigit(i), GetDigit(N // i)))
    print(ans)


if __name__ == "__main__":
    main()
