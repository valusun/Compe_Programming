import heapq
from collections import deque


def main():
    Q = int(input())
    A = deque()
    sorted_A = []
    for _ in range(Q):
        c, *x = map(int, input().split())
        if c == 1:
            A.append(x[0])
        elif c == 2:
            if len(sorted_A):
                print(heapq.heappop(sorted_A))
            else:
                print(A.popleft())
        else:
            while len(A):
                heapq.heappush(sorted_A, A.popleft())


if __name__ == "__main__":
    main()
