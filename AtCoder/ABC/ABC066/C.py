from collections import deque


def main():
    N = int(input())
    A = list(map(int, input().split()))

    B = deque()
    for i, a in enumerate(A):
        if i % 2:
            B.appendleft(a)
        else:
            B.append(a)

    if N % 2:
        print(*list(B)[::-1])
    else:
        print(*B)


if __name__ == "__main__":
    main()
