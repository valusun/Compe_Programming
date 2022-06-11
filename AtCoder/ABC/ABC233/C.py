def main():
    N, X = map(int, input().split())
    A = []
    for _ in range(N):
        _, *a = map(int, input().split())
        A.append(sorted(a))

    def dfs(cnt, res):
        if cnt == N:
            if res == X:
                return 1
            return 0
        ans = 0
        for a in A[cnt]:
            if res * a <= X:
                ans += dfs(cnt + 1, res * a)
        return ans

    print(dfs(0, 1))


if __name__ == "__main__":
    main()
