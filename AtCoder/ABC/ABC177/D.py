from typing import List


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * self.n

    def get_root(self, x) -> int:
        """xの属している木の親を返す"""
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.get_root(self.parents[x])
            return self.parents[x]

    def union(self, x, y) -> None:
        """xが属している木とyが属している木を結合する"""
        x = self.get_root(x)
        y = self.get_root(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def get_size(self, x) -> int:
        """xが属する木の要素数を返す"""
        return -self.parents[self.get_root(x)]

    def is_same(self, x, y) -> bool:
        """xとyが同じ木に属しているかを判定する"""
        return self.get_root(x) == self.get_root(y)

    def get_members(self, x) -> List[int]:
        """xの木に属している要素を返す"""
        root = self.get_root(x)
        return [i for i in range(self.n) if self.get_root(i) == root]

    def get_roots(self) -> List[int]:
        """木の親を返す"""
        return [i for i, x in enumerate(self.parents) if x < 0]

    def get_group_count(self) -> int:
        """木の数を返す"""
        return len(self.get_roots())


def main():
    N, M = map(int, input().split())
    UF = UnionFind(N)
    for _ in range(M):
        a, b = map(int, input().split())
        UF.union(a - 1, b - 1)
    ans = 0
    for p in UF.parents:
        if p < 0:
            ans = max(ans, -p)
    print(ans)


if __name__ == "__main__":
    main()
