def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    for j in range(W):
        ans = []
        for i in range(H):
            ans.append(A[i][j])
        print(*ans)


if __name__ == "__main__":
    main()
