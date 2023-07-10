def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    rs = [sum(a) for a in A]
    cs = [sum(a) for a in zip(*A)]
    B = [[0] * W for _ in range(H)]
    for i, r in enumerate(rs):
        for j, c in enumerate(cs):
            B[i][j] = r + c - A[i][j]
    for b in B:
        print(*b)


if __name__ == "__main__":
    main()
