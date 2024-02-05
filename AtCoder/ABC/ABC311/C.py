import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    seen = [False] * (N + 1)

    def restore(v):
        ans = [v]
        nxt = A[v - 1]
        while nxt != v:
            ans.append(nxt)
            nxt = A[nxt - 1]
        print(len(ans))
        print(*ans)

    def check(v):
        seen[v] = True
        if seen[A[v] - 1]:
            restore(A[v])
            exit()
        check(A[v] - 1)

    for v in range(N):
        if seen[v]:
            continue
        check(v)


if __name__ == "__main__":
    main()
