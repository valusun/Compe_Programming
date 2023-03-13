def main():
    _ = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for a in A:
        for b in B:
            if a > b:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
