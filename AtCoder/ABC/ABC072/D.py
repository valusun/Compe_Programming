def main():
    N = int(input())
    A = list(map(int, input().split()))
    i = 0
    ans = 0
    while i < N:
        if A[i] == i + 1:
            i += 1
            ans += 1
        i += 1
    print(ans)


if __name__ == "__main__":
    main()
