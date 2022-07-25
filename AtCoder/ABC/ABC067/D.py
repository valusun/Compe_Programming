from collections import deque
from typing import List, Deque


def GetFastestPath(Q: Deque[int], Graph: List[List[int]]) -> List[int]:
    """各地点への最短到達距離を求める"""
    INF = 10**18
    dist = [INF] * len(Graph)
    dist[Q[0]] = 0
    while Q:
        v = Q.popleft()
        for u in Graph[v]:
            if dist[u] == INF:
                dist[u] = dist[v] + 1
                Q.append(u)
    return dist


def main():
    N = int(input())
    Graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        Graph[a - 1].append(b - 1)
        Graph[b - 1].append(a - 1)
    black_dist = GetFastestPath(deque([0]), Graph)
    white_dist = GetFastestPath(deque([N - 1]), Graph)
    getting_black = 0
    getting_while = 0
    for i in range(N):
        if black_dist[i] <= white_dist[i]:
            getting_black += 1
        else:
            getting_while += 1
    print("Fennec" if getting_black > getting_while else "Snuke")


if __name__ == "__main__":
    main()
