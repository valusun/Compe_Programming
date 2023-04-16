def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i, a in enumerate(A, start=1):
        ans[a - 1] = i
    print(*ans)


if __name__ == "__main__":
    main()
