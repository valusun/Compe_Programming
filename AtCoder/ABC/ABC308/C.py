from functools import cmp_to_key


def cmp(c1, c2):
    a1, b1, _ = c1
    a2, b2, _ = c2
    x1 = a1 * (a2 + b2)
    x2 = a2 * (a1 + b1)
    return 0 if x1 == x2 else 1 if x1 < x2 else -1


def main():
    N = int(input())
    ab = [list(map(int, input().split())) + [i + 1] for i in range(N)]
    tmp = sorted(ab, key=cmp_to_key(cmp))
    print(*[i for _, _, i in tmp])


if __name__ == "__main__":
    main()
