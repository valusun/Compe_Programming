# Union-Find
class UnionFind:
    def __init__(self, n, A, B):
        self.n = n
        self.parents = [-1] * n
        self.members_sum_a = A
        self.members_sum_b = B

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
        self.members_sum_a[x] += self.members_sum_a[y]
        self.members_sum_b[x] += self.members_sum_b[y]
        self.members_sum_a[y] = 0
        self.members_sum_b[y] = 0

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
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    UF = UnionFind(N, A, B)
    for _ in range(M):
        c, d = map(int, input().split())
        UF.union(c - 1, d - 1)
    for i in range(N):
        if UF.members_sum_a[i] != UF.members_sum_b[i]:
            print("No")
            break
    else:
        print("Yes")


if __name__ == "__main__":
    main()
