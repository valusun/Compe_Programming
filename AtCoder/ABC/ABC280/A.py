def main():
    H, _ = map(int, input().split())
    ans = 0
    for _ in range(H):
        ans += list(input()).count("#")
    print(ans)


if __name__ == "__main__":
    main()
