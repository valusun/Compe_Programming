from bisect import bisect_right, bisect_left


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    A_value_place = dict()
    for i, v in enumerate(A):
        if v not in A_value_place:
            A_value_place[v] = []
        A_value_place[v].append(i + 1)
    for i in range(Q):
        l, r, x = map(int, input().split())
        if x not in A_value_place:
            print(0)
        else:
            print(bisect_right(A_value_place[x], r) - bisect_left(A_value_place[x], l))


if __name__ == "__main__":
    main()
