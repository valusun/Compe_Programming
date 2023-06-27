def main():
    N = int(input())
    DD = [list(map(int, input().split())) for _ in range(N)]
    cnt = [0] * (N + 1)
    for i in range(1, N + 1):
        if DD[i - 1][0] == DD[i - 1][1]:
            cnt[i] += cnt[i - 1] + 1
        else:
            cnt[i] = 0
    print("Yes" if max(cnt) >= 3 else "No")


if __name__ == "__main__":
    main()
