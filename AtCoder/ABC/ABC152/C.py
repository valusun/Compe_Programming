def main():
    _ = int(input())
    P = list(map(int, input().split()))
    ans = 1
    mn = P[0]
    for p in P[1:]:
        if p <= mn:
            ans += 1
            mn = p
    print(ans)


if __name__ == "__main__":
    main()
