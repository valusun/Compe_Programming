def main():
    N, D = map(int, input().split())
    S = [list(input()) for _ in range(N)]
    ans = tmp = 0
    for s in list(zip(*S)):
        tmp = 0 if "x" in s else tmp + 1
        ans = max(ans, tmp)
    print(ans)


if __name__ == "__main__":
    main()
