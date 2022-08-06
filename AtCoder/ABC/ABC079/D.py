def main():
    H, W = map(int, input().split())
    C = [list(map(int, input().split())) for _ in range(10)]
    A = [list(map(int, input().split())) for _ in range(H)]
    for k in range(10):
        for i in range(10):
            for j in range(10):
                C[i][j] = min(C[i][j], C[i][k] + C[k][j])
    ans = 0
    for h in range(H):
        for w in range(W):
            if A[h][w] >= 0:
                ans += C[A[h][w]][1]
    print(ans)


if __name__ == "__main__":
    main()
