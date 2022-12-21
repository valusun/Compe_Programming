def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    d, ans = 0, 1
    for v in L:
        if (d := d + v) <= X:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
