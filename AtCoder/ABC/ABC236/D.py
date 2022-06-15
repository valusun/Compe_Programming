import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N * 2 - 1)]

    def dfs(pair, used):
        if len(pair) == N:
            score = 0
            for i in range(N):
                x, y = pair[i][0], pair[i][1]
                score ^= A[x][y - x - 1]
            return score
        ans = 0
        for i in range(N * 2):
            if used[i]:
                continue
            used[i] = True
            first = i
            break
        for j in range(first + 1, N * 2):
            if used[j]:
                continue
            pair.append((first, j))
            used[j] = True
            ans = max(ans, dfs(pair, used))
            used[j] = False
            pair.pop()
        used[first] = False
        return ans

    print(dfs([], [False] * (N * 2)))


if __name__ == "__main__":
    main()
