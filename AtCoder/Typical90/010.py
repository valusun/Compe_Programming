import itertools


def main():
    N = int(input())
    c1, c2 = [0], [0]
    for _ in range(N):
        c, p = map(int, input().split())
        c1_p = c2_p = 0
        if c == 1:
            c1_p = p
        else:
            c2_p = p
        c1.append(c1_p)
        c2.append(c2_p)
    c1 = list(itertools.accumulate(c1))
    c2 = list(itertools.accumulate(c2))
    Q = int(input())
    for _ in range(Q):
        l, r = map(int, input().split())
        print(c1[r] - c1[l - 1], c2[r] - c2[l - 1])


if __name__ == "__main__":
    main()
