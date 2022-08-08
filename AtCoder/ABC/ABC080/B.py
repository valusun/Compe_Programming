def SumDigit(n: str):
    ret = 0
    for i in n:
        ret += int(i)
    return ret


def main():
    N = input()
    if int(N) % SumDigit(N):
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
