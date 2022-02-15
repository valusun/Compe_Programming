# Union-Find
class UnionFind():
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

# ----- Main ----- #

N = 2**20
A = [-1]*N

Q = int(input())
UF = UnionFind(N)
for i in range(Q):
    t,x = map(int,input().split())
    if t==1:
        h = x%N
        if A[h] != -1:
            h = UF.find(h)
        if h == N-1:
            UF.union(0, h)
        else:
            UF.union(h+1, h)
        A[h] = x
    else:
        print(A[x%N])