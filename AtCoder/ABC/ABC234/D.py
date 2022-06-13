from heapq import heappop, heappush


def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    A = []
    for p in P[:K]:
        heappush(A, p)
    for i in range(K, N):
        ans = heappop(A)
        print(ans)
        heappush(A, max(ans, P[i]))
    print(heappop(A))


if __name__ == "__main__":
    main()
