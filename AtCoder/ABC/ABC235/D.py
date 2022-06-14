from collections import deque


def main():
    a, N = map(int, input().split())
    seem_numbers = set([1])
    que = deque()
    que.append((1, 0))
    while que:
        now, cnt = que.popleft()
        if now == N:
            print(cnt)
            exit()
        if now >= 10 and now % 10 != 0:
            next_number = int(str(now)[-1] + str(now)[:-1])
            if next_number not in seem_numbers:
                seem_numbers.add(next_number)
                que.append((next_number, cnt + 1))
        if len(str(now * a)) <= len(str(N)) and (now * a) not in seem_numbers:
            seem_numbers.add(now * a)
            que.append((now * a, cnt + 1))
    print(-1)


if __name__ == "__main__":
    main()
