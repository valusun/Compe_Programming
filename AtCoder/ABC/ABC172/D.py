def main():
    N = int(input())
    divs = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(i, N + 1, i):
            divs[j] += 1
    ans = 0
    for i, d in enumerate(divs):
        ans += i * d
    print(ans)


if __name__ == "__main__":
    main()
