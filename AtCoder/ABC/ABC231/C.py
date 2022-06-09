from bisect import bisect_left


def main():
    N, Q = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    for _ in range(Q):
        print(N - bisect_left(A, int(input())))


if __name__ == "__main__":
    main()
