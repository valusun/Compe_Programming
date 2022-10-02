def main():
    s = int(input())
    seen = set([s])

    ans = 2
    while True:
        s = s * 3 + 1 if s % 2 else s // 2
        if s in seen:
            print(ans)
            break
        seen.add(s)
        ans += 1


if __name__ == "__main__":
    main()
