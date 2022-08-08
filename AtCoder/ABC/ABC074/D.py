def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    INF = 10**18
    for i in range(N):
        A[i][i] = INF

    ans = 0
    for u in range(N):
        for v in range(u + 1, N):
            min_dist = INF
            for w in range(N):
                min_dist = min(min_dist, A[u][w] + A[w][v])
            if min_dist < A[u][v]:
                print(-1)
                exit()
            if A[u][v] < min_dist:
                ans += A[u][v]
    print(ans)


if __name__ == "__main__":
    main()
