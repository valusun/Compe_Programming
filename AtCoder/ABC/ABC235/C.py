from collections import defaultdict


def main():
    _, Q = map(int, input().split())
    A = list(map(int, input().split()))
    dic = defaultdict(list)
    for i, a in enumerate(A):
        dic[a].append(i + 1)
    for _ in range(Q):
        x, k = map(int, input().split())
        if x in dic and len(dic[x]) >= k:
            print(dic[x][k - 1])
        else:
            print(-1)


if __name__ == "__main__":
    main()
