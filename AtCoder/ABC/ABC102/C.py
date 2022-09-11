def main():
    N = int(input())
    A = list(map(int, input().split()))
    diffs = sorted([a - i for i, a in enumerate(A, 1)])
    mid = diffs[N // 2] if N % 2 else (diffs[N // 2 - 1] + diffs[N // 2]) // 2
    ans = sum([abs(a - mid - i) for i, a in enumerate(A, 1)])
    print(ans)


if __name__ == "__main__":
    main()
