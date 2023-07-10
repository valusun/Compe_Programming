def main():
    _ = int(input())
    A = list(map(int, input().split()))
    ans = [A[0]]
    for na in A[1:]:
        s = 1 if ans[-1] < na else -1
        ans += list(range(ans[-1] + s, na + s, s))
    print(*ans)


if __name__ == "__main__":
    main()
