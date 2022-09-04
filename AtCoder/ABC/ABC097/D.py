# Union-Find
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.groups = [-1] * n

    # Returns the root of the tree to which x belongs
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            self.groups[x] = x
            return self.parents[x]

    # Union x-tree and y-tree
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.groups[y] = x

    # Returns x-tree number of elements in the tree
    def size(self, x):
        return -self.parents[self.find(x)]

    # Are x and y the same tree?
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # Returns the element of the tree to which x belongs
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    # Returns a list of all root elements
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    # Returns Group Count
    def group_count(self):
        return len(self.roots())


def main():
    N, M = map(int, input().split())
    p = list(map(int, input().split()))
    pair = [map(int, input().split()) for _ in range(M)]

    UF = UnionFind(N)
    for x, y in pair:
        UF.union(x - 1, y - 1)

    place = [0] * N
    for i, x in enumerate(p):
        place[x - 1] = i

    ans = 0
    for x in range(N):
        y = place[x]
        if p[x] - 1 == x or UF.same(x, y):
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
