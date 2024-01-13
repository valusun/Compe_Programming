def main():
    N = int(input())
    w = set()
    ans = 0
    for _ in range(N):
        s = input()
        s1 = s[::-1]
        if s in w or s1 in w:
            continue
        w.add(s)
        w.add(s1)
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
