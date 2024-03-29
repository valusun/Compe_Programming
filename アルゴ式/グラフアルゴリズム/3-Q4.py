from collections import deque


def main():
    N, M = map(int, input().split())
    works = [[] for _ in range(N)]
    dependence_cnts = [0] * N
    for _ in range(M):
        a, b = map(int, input().split())
        works[a].append(b)
        dependence_cnts[b] += 1

    Q = deque()
    for i, d in enumerate(dependence_cnts):
        if d == 0:
            Q.append(i)

    while Q:
        v = Q.popleft()
        for nv in works[v]:
            dependence_cnts[nv] -= 1
            if dependence_cnts[nv] == 0:
                Q.append(nv)
    print("Yes" if max(dependence_cnts) == 0 else "No")


if __name__ == "__main__":
    main()
