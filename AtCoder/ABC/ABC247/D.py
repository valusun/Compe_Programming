from collections import deque


def main():
    Q = int(input())
    queue = deque()
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x, c = query[1], query[2]
            queue.append([x, c])
        else:
            c = query[1]
            res = 0
            while c:
                ball, ball_num = queue.popleft()
                if ball_num < c:
                    res += ball * ball_num
                    c -= ball_num
                else:
                    res += ball * c
                    queue.appendleft([ball, ball_num - c])
                    c = 0
            print(res)


if __name__ == "__main__":
    main()
