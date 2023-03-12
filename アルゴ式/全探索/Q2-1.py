def main():
    N = int(input())
    ans = 0
    for i in range(N + 1):
        if i % 2 and i % 3 and i % 5:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
