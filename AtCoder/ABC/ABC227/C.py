def main():
    N = int(input())

    ans = 0
    for a in range(1, N + 1):
        if a**3 > N:
            break
        for b in range(a, N + 1):
            c = N // (a * b)
            if b > c:
                break
            ans += c - b + 1
    print(ans)


if __name__ == "__main__":
    main()
