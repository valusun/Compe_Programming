def main():
    H, _ = map(int, input().split())
    c = [list(input()) for _ in range(H)]
    ans = []
    for cc in zip(*c):
        ans.append(cc.count("#"))
    print(*ans)


if __name__ == "__main__":
    main()
