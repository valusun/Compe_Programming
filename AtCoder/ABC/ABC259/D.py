import sys

sys.setrecursionlimit(10**9)


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

    Graph = [[] for _ in range(N)]
    start, goal = -1, -1
    for i in range(N):
        for j in range(i + 1, N):
            if IsIntersect(circle[i], circle[j]):
                Graph[i].append(j)
                Graph[j].append(i)
        if start == -1 and IsOnTheCircumference(circle[i], sx, sy):
            start = i
        if goal == -1 and IsOnTheCircumference(circle[i], tx, ty):
            goal = i

    def dfs(v, visited):
        visited[v] = True
        if v == goal:
            return True
        for u in Graph[v]:
            if visited[u]:
                continue
            dfs(u, visited)
        return False

    print("Yes" if dfs(start, [False] * N) else "No")


if __name__ == "__main__":
    main()
