def main():
    _ = int(input())
    A = list(map(int, input().split()))
    all_A = sum(A)
    now = 0
    ans = float("inf")
    for a in A[:-1]:
        now += a
        raccoon = all_A - now
        ans = min(ans, abs(now - raccoon))
    print(ans)


if __name__ == "__main__":
    main()
