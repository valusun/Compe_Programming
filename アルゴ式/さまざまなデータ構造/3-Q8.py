def main():
    N, T = input().split()
    ans = 0
    for _ in range(int(N)):
        _, *c = input().split()
        ans += T in c
    print(ans)


if __name__ == "__main__":
    main()
