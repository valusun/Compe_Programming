def main():
    _ = int(input())
    A = list(map(int, input().split()))
    ans = 10**18
    for a in A:
        cnt = 0
        while a % 2 == 0:
            a //= 2
            cnt += 1
        ans = min(ans, cnt)
    print(ans)


if __name__ == "__main__":
    main()
