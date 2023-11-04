import sys

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    pos = [[] for _ in range(N)]
    Color = [-1] * N
    for i in range(M):
        if A[i] == B[i]:
            print("No")
            return
        pos[A[i] - 1].append(B[i] - 1)
        pos[B[i] - 1].append(A[i] - 1)

    def dfs(n):
        for u in pos[n]:
            nxt = (Color[n] + 1) % 2
            if Color[u] == -1:
                Color[u] = nxt
                dfs(u)
            if Color[u] != nxt:
                print("No")
                exit()

    for i in range(N):
        if Color[i] == -1:
            Color[i] = 0
            dfs(i)
    print("Yes")


if __name__ == "__main__":
    main()
