from typing import List
import sys

sys.setrecursionlimit(10**9)


class UnionFind:
    def __init__(self, n):
        self.n: int = n
        self.parents: List[int] = [-1] * self.n

    def Find(self, x) -> int:
        """xの属している木の親を返す"""
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.Find(self.parents[x])
            return self.parents[x]

    def Union(self, x, y) -> None:
        """xが属している木とyが属している木を結合する"""
        x = self.Find(x)
        y = self.Find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def GetSize(self, x) -> int:
        """xが属する木の要素数を返す"""
        return -self.parents[self.Find(x)]

    def IsSame(self, x, y) -> bool:
        """xとyが同じ木に属しているかを判定する"""
        return self.Find(x) == self.Find(y)

    def GetMembers(self, x) -> List[int]:
        """xの木に属している要素を返す"""
        root = self.Find(x)
        return [i for i in range(self.n) if self.Find(i) == root]

    def GetRoots(self) -> List[int]:
        """木の親を返す"""
        return [i for i, x in enumerate(self.parents) if x < 0]

    def GetGroupCount(self) -> int:
        """木の数を返す"""
        return len(self.GetRoots())


def main():
    def Connect(x, y):
        x, y = max(x, y), min(x, y)
        if y >= N:
            return
        if x > N:
            x = N
        UF.Union(x, y)

    N, M, E = map(int, input().split())
    X = []
    UF = UnionFind(N + 1)
    for _ in range(E):
        x, y = map(int, input().split())
        X.append([x - 1, y - 1])
    Q = int(input())
    Query = [int(input()) for _ in range(Q)]

    q = set(range(1, E + 1)) - set(Query)
    for v in q:
        Connect(*X[v - 1])

    ans = []
    for v in Query[::-1]:
        x, y = X[v - 1]
        ans.append(UF.GetSize(N) - 1)
        Connect(x, y)
    print(*ans[::-1], sep="\n")


if __name__ == "__main__":
    main()
