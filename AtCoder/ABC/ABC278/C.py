from collections import defaultdict


def main():
    N, Q = map(int, input().split())
    ff = defaultdict(set)
    for _ in range(Q):
        t, a, b = map(int, input().split())
        if t == 1:
            ff[a].add(b)
        if t == 2:
            if b in ff[a]:
                ff[a].remove(b)
        if t == 3:
            print("Yes" if (b in ff[a] and a in ff[b]) else "No")


if __name__ == "__main__":
    main()
