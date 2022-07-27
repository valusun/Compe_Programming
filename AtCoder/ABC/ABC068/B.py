def main():
    N = int(input())
    ans = 0
    div_cnt = 0
    for i in range(1, N + 1):
        x = i
        res = 0
        while x % 2 == 0:
            res += 1
            x //= 2
        if div_cnt <= res:
            div_cnt = res
            ans = i
    print(ans)


if __name__ == "__main__":
    main()
