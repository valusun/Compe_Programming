from collections import deque


def main():
    Q = int(input())
    deq = deque([])
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            deq.appendleft(x)
        elif t == 2:
            deq.append(x)
        else:
            print(deq[x - 1])


if __name__ == "__main__":
    main()
