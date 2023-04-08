def main():
    _ = int(input())
    vals = sorted(list(map(int, input().split())))
    now = vals[0]
    for v in vals[1:]:
        now = (now + v) / 2
    print(now)


if __name__ == "__main__":
    main()
