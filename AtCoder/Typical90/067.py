def FromOctToDec(n: int) -> int:
    n_ = str(n)[::-1]
    ans = 0
    for i, d in enumerate(n_):
        ans += int(d) * 8**i
    return ans


def Conversion(n: int) -> int:
    ans = ""
    while n:
        tmp = n % 9
        if tmp == 8:
            ans += "5"
        else:
            ans += str(tmp)
        n //= 9
    return int(ans[::-1]) if ans else 0


def main():
    N, K = map(int, input().split())
    ans = N
    for _ in range(K):
        ans = Conversion(FromOctToDec(ans))
    print(ans)


if __name__ == "__main__":
    main()
