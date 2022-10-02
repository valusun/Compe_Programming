def main():
    N = int(input())
    H = [0] + list(map(int, input().split()))

    ans = 0
    for i in range(1, N + 1):
        if H[i - 1] < H[i]:
            ans += H[i] - H[i - 1]
    print(ans)


if __name__ == "__main__":
    main()
