def SumDigit(n: int) -> int:
    ret = 0
    for s in str(n):
        ret += int(s)
    return ret


def main():
    N = int(input())
    print("Yes" if N % SumDigit(N) == 0 else "No")


if __name__ == "__main__":
    main()
