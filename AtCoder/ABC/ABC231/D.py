# Union-Find
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
            return False

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return True

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
    A = [list(map(int, input().split())) for _ in range(M)]
    UF = UnionFind(N)
    neighbors_cnt = [0] * N
    for a, b in A:
        if not UF.union(a - 1, b - 1):
            print("No")
            exit()
        neighbors_cnt[a - 1] += 1
        neighbors_cnt[b - 1] += 1
    for n in neighbors_cnt:
        if n > 2:
            print("No")
            break
    else:
        print("Yes")


if __name__ == "__main__":
    main()
