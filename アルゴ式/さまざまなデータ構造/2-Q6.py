from collections import deque


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    que = deque(A)
    Q = int(input())
    is_reverse = False
    for _ in range(Q):
        n, *v = map(int, input().split())
        if n == 0:
            is_reverse = False if is_reverse else True
        elif n == 1:
            if is_reverse:
                que.appendleft(v[0])
            else:
                que.append(v[0])
        else:
            if not que:
                print("Error")
                continue
            num = que.popleft() if is_reverse else que.pop()
            print(num)


if __name__ == "__main__":
    main()
