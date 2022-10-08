def main():
    def dfs(cost, n, a, b, c):
        nonlocal ans
        if n == N:
            if a == 0 or b == 0 or c == 0:
                return
            cost += abs(A - a) + abs(B - b) + abs(C - c) - 30  # 伸縮魔法
            ans = min(ans, cost)
            return
        dfs(cost + 10, n + 1, a + L[n], b, c)
        dfs(cost + 10, n + 1, a, b + L[n], c)
        dfs(cost + 10, n + 1, a, b, c + L[n])
        dfs(cost, n + 1, a, b, c)

    N, A, B, C = map(int, input().split())
    L = [int(input()) for _ in range(N)]
    ans = float("inf")
    dfs(0, 0, 0, 0, 0)
    print(ans)


if __name__ == "__main__":
    main()
