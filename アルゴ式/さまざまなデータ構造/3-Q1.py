def main():
    H, _ = map(int, input().split())
    # print(sum([list(input()).count("o") for _ in range(H)]))
    ans = 0
    for _ in range(H):
        ans += list(input()).count("o")
    print(ans)


if __name__ == "__main__":
    main()
