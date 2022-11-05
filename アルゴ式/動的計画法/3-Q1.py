def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    can_moved = [[False] * M for _ in range(N)]
    can_moved[0][0] = True
    for i in range(N - 1):
        for j in range(M):
            can_moved[i + 1][j] |= can_moved[i][j]
            if j + A[i] < M:
                can_moved[i + 1][j + A[i]] |= can_moved[i][j]
    print(can_moved[N - 1].count(True))


if __name__ == "__main__":
    main()
