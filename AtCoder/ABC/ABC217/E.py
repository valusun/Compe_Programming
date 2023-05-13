import heapq
from collections import deque


def main():
    Q = int(input())
    A = deque([])
    SA = []
    for _ in range(Q):
        c, *a = map(int, input().split())
        if c == 1:
            A.append(a[0])
        elif c == 2:
            print(heapq.heappop(SA) if SA else A.popleft())
        else:
            while A:
                heapq.heappush(SA, A.popleft())


if __name__ == "__main__":
    main()
