from dataclasses import dataclass, field
from typing import List


@dataclass
class UnionFind:
    n: int
    parents: List = field(init=False, default_factory=list)

    def __post_init__(self):
        self.parents = [-1] * self.n

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
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        a, b = map(int, input().split())
        edges.append([a - 1, b - 1])
    ans = 0
    for i in range(M):
        UF = UnionFind(N)
        for j in range(M):
            if i == j:
                continue
            UF.Union(edges[j][0], edges[j][1])
        if UF.GetGroupCount() > 1:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
