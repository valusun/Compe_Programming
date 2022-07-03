def main():
    _ = int(input())
    S = input()
    ans, now = 0, 0
    for s in S:
        if s == "I":
            now += 1
        else:
            now -= 1
        ans = max(ans, now)
    print(ans)


if __name__ == "__main__":
    main()
