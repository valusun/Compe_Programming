def main():
    N = int(input())
    B = list(map(int, input().split()))
    ans = B[0]
    for i in range(N - 2):
        ans += B[i] if B[i] < B[i + 1] else B[i + 1]
    print(ans + B[-1])


if __name__ == "__main__":
    main()
