class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    # Returns the root of the tree to which x belongs
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
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
    Graph = [[] for _ in range(N)]
    for _ in range(M):
        v, u = map(int, input().split())
        Graph[v - 1].append(u - 1)
    ans = [0]
    link_cnt = 0
    UF = UnionFind(N)
    for v in range(N - 1, 0, -1):
        link_cnt += 1
        for u in Graph[v]:
            if not UF.same(v, u):
                UF.union(v, u)
                link_cnt -= 1
        ans.append(link_cnt)
    print(*ans[::-1], sep="\n")


if __name__ == "__main__":
    main()
