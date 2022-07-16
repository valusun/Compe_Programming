from bisect import bisect_left


def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    a_sorted = sorted(list(set(A)))
    for a in A:
        print(bisect_left(a_sorted, a))


if __name__ == "__main__":
    main()
