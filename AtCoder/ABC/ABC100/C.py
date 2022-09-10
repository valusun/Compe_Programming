def main():
    _ = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        while not a % 2:
            a //= 2
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
