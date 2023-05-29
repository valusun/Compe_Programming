def main():
    X = int(input())
    now = 100
    ans = 0
    while X > now:
        now = now * 101 // 100
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
