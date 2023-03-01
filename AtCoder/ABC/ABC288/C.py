from typing import List


class UnionFind:
    def __init__(self, n):
        self.n = n
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
    UF = UnionFind(N)
    ans = 0
    for _ in range(M):
        s, t = map(int, input().split())
        if UF.IsSame(s - 1, t - 1):
            ans += 1
            continue
        UF.Union(s - 1, t - 1)
    print(ans)


if __name__ == "__main__":
    main()
