def main():
    _, X = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    ans = 0
    while X != 0:
        ans += 1
        X = A[X]
    print(ans)


if __name__ == "__main__":
    main()
