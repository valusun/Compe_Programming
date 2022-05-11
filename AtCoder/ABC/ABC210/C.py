def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    candy_kinds = set()
    candy_counts = dict()
    ans = 0
    left = 0
    for right in range(N):
        if c[right] not in candy_kinds:
            candy_counts[c[right]] = 0
        candy_counts[c[right]] += 1
        candy_kinds.add(c[right])
        if right - left + 1 == K:
            ans = max(ans, len(candy_kinds))
            candy_counts[c[left]] -= 1
            if not candy_counts[c[left]]:
                candy_kinds.discard(c[left])
            left += 1
    print(ans)


if __name__ == "__main__":
    main()
