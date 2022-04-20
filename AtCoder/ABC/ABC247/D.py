from collections import deque


Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]
queue = deque()

for i in range(Q):
    t, *a = query[i]
    if t == 1:
        queue.append([a[0], a[1]])
    else:
        limit = a[0]
        now = 0
        while limit:
            x, c = queue.popleft()
            if limit > c:
                now += x * c
                limit -= c
            else:
                now += x * limit
                queue.appendleft([x, c - limit])
                limit = 0
        print(now)
