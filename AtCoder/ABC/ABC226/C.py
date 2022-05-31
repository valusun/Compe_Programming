from collections import deque


def main():
    N = int(input())
    learning_times = []
    need_arts = []
    for _ in range(N):
        t, _, *a = map(int, input().split())
        learning_times.append(t)
        need_arts.append(a)
    learned_arts = [False] * N
    learned_arts[N - 1] = True
    time = 0
    q = deque()
    q.append((N - 1))
    while q:
        v = q.popleft()
        time += learning_times[v]
        for u in need_arts[v]:
            if learned_arts[u - 1]:
                continue
            learned_arts[u - 1] = True
            q.append((u - 1))
    print(time)


if __name__ == "__main__":
    main()
