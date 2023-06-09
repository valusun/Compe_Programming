from collections import Counter


def main():
    _ = int(input())
    A = sorted(list(map(int, input().split())))
    mx = max(A) + 1

    mul_memo = [0] * mx
    seen = set()
    dic = Counter()
    for a in A:
        dic[a] += 1
        if a in seen:
            continue
        for p in range(a * 2, mx, a):
            mul_memo[p] = 1

    ans = 0
    for a in A:
        if not mul_memo[a] and dic[a] == 1:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
