from collections import defaultdict, deque


def main():
    _ = map(int, input().split())
    S = input()
    A = list(map(int, input().split()))
    d = defaultdict(deque)
    for i, a in enumerate(A):
        d[a].append(i)
    for k in d.keys():
        d[k].rotate()
    ans = ""
    for a in A:
        ans += S[d[a].popleft()]
    print(ans)


if __name__ == "__main__":
    main()
