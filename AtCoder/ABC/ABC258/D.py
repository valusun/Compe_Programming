def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    ans = float("inf")
    prev = 0
    for i in range(N):
        if i > X:
            break
        res = AB[i][0] + AB[i][1] + prev
        ans = min(ans, res + AB[i][1] * (X - i - 1))
        prev = res
    print(ans)


if __name__ == "__main__":
    main()
