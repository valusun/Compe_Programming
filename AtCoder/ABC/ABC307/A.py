def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = []
    for i in range(N):
        ans.append(sum(A[i * 7 : i * 7 + 7]))
    print(*ans)


if __name__ == "__main__":
    main()
