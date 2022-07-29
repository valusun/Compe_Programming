def main():
    H, W = map(int, input().split())
    _ = int(input())
    A = list(map(int, input().split()))
    ans = [[0] * W for _ in range(H)]
    idx = 0
    cnt = 0
    for h in range(H):
        for w in range(W):
            if h % 2:
                ans[h][-w - 1] = idx + 1
            else:
                ans[h][w] = idx + 1
            cnt += 1
            if cnt == A[idx]:
                idx += 1
                cnt = 0
    for i in range(H):
        print(*ans[i])


if __name__ == "__main__":
    main()
