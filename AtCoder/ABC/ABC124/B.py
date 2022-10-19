def main():
    _ = int(input())
    H = list(map(int, input().split()))
    now_max = 0
    ans = 0
    for h in H:
        if now_max <= h:
            ans += 1
            now_max = h
    print(ans)


if __name__ == "__main__":
    main()
