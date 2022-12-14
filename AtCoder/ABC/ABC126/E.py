class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def Union(self, x, y):
        x_tree = self.Find(x)
        y_tree = self.Find(y)
        if x_tree == y_tree:
            return
        if self.parents[x_tree] > self.parents[y_tree]:
            x_tree, y_tree = y_tree, x_tree
        self.parents[x_tree] += self.parents[y_tree]
        self.parents[y_tree] = x_tree

    def Find(self, x):
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.Find(self.parents[x])
        return self.parents[x]

    def GetTreeCnt(self):
        return len([i for i, x in enumerate(self.parents) if x < 0])


def main():
    N, M = map(int, input().split())
    UF = UnionFind(N)
    for _ in range(M):
        X, Y, _ = map(int, input().split())
        UF.Union(X - 1, Y - 1)
    print(UF.GetTreeCnt())


if __name__ == "__main__":
    main()
