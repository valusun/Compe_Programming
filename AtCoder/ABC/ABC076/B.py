def main():
    N = int(input())
    K = int(input())
    ans = 1
    for _ in range(N):
        ans = min(ans * 2, ans + K)
    print(ans)


if __name__ == "__main__":
    main()
