def main():
    N = int(input())
    W = list(map(int, input().split()))
    a = 0
    b = sum(W)
    ans = b - a
    for i in range(N):
        a += W[i]
        b -= W[i]
        ans = min(ans, abs(a - b))
    print(ans)


if __name__ == "__main__":
    main()
