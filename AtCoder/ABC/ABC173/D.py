def main():
    N = int(input())
    A = sorted(list(map(int, input().split())), reverse=True)
    ans = A[0]
    for i in range(N - 2):
        ans += A[i // 2 + 1]
    print(ans)


if __name__ == "__main__":
    main()
