def main():
    _ = int(input())
    D = list(map(int, input().split()))
    ans = 0
    for i, d1 in enumerate(D):
        for d2 in D[i + 1 :]:
            ans += d1 * d2
    print(ans)


if __name__ == "__main__":
    main()
