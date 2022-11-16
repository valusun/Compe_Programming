from collections import deque


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    que = deque(A)
    Q = int(input())
    for _ in range(Q):
        n, v = map(int, input().split())
        if n == 0:
            que.appendleft(v)
        elif n == 1:
            que.append(v)
        else:
            if len(que) <= v:
                print("Error")
                continue
            print(que[v])


if __name__ == "__main__":
    main()
