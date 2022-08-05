from bisect import bisect_left, bisect_right


def main():
    N = int(input())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    C = sorted(list(map(int, input().split())))
    ans = 0
    for b in B:
        a_pattern = bisect_left(A, b)
        c_pattern = N - bisect_right(C, b)
        ans += a_pattern * c_pattern
    print(ans)


if __name__ == "__main__":
    main()
