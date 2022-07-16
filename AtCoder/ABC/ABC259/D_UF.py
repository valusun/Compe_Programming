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


def IsIntersect(c1, c2):
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
    if dist > (r1 + r2) ** 2 or dist < (r1 - r2) ** 2:
        return False
    return True


def IsOnTheCircumference(c, x, y):
    cx, cy, cr = c
    if (cx - x) ** 2 + (cy - y) ** 2 == cr**2:
        return True
    return False


def main():
    N = int(input())
    sx, sy, tx, ty = map(int, input().split())
    circle = []
    for _ in range(N):
        circle.append(list(map(int, input().split())))
    UF = UnionFind(N)
    start, goal = -1, -1
    for i in range(N):
        for j in range(i + 1, N):
            if IsIntersect(circle[i], circle[j]):
                UF.union(i, j)
        if start == -1 and IsOnTheCircumference(circle[i], sx, sy):
            start = i
        if goal == -1 and IsOnTheCircumference(circle[i], tx, ty):
            goal = i
    print("Yes" if UF.same(start, goal) else "No")


if __name__ == "__main__":
    main()
