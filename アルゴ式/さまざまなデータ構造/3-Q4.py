def main():
    H, _ = map(int, input().split())
    fields = [list(input()) for _ in range(H)]
    r, c = map(int, input().split())
    ans = fields[r].count("#")
    for i in range(H):
        ans += 1 if fields[i][c] == "#" else 0
    print(ans - 1 if fields[r][c] == "#" else ans)


if __name__ == "__main__":
    main()
