from collections import Counter


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    ans = sum(A)
    elm_memo = Counter()
    for a in A:
        elm_memo[a] += 1
    Q = int(input())
    for _ in range(Q):
        B, C = map(int, input().split())
        ans = ans - B * elm_memo[B] + elm_memo[B] * C
        elm_memo[C] += elm_memo[B]
        elm_memo[B] = 0
        print(ans)


if __name__ == "__main__":
    main()
