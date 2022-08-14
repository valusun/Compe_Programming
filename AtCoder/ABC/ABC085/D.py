def main():
    N, H = map(int, input().split())
    k = [list(map(int, input().split())) for _ in range(N)]
    max_a = sorted(k)[-1][0]
    used = sorted([b for _, b in k if b > max_a], reverse=True)
    ans = 0
    for b in used:
        H -= b
        ans += 1
        if H <= 0:
            print(ans)
            exit()
    print(ans + (H + max_a - 1) // max_a)


if __name__ == "__main__":
    main()
