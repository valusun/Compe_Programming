from bisect import bisect_left


def main():
    N, M = map(int, input().split())
    H = sorted(list(map(int, input().split())))
    W = list(map(int, input().split()))
    left = [0]
    right = [0]
    for i in range(2, N, 2):
        left.append(left[-1] + H[i - 1] - H[i - 2])
        right.append(right[-1] + H[N - i + 1] - H[N - i])
    right = right[::-1]
    ans = 10**18
    for w in W:
        idx = bisect_left(H, w)
        if idx % 2:
            idx -= 1
        ans = min(ans, left[idx // 2] + right[idx // 2] + abs(w - H[idx]))
    print(ans)


if __name__ == "__main__":
    main()
