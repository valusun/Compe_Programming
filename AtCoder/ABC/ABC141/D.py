import heapq


def main():
    N, M = map(int, input().split())
    A = [-a for a in map(int, input().split())]
    heapq.heapify(A)
    for _ in range(M):
        x = heapq.heappop(A)
        heapq.heappush(A, -(-x // 2))
    print(-sum(A))


if __name__ == "__main__":
    main()
