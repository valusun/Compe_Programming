def main():
    N = int(input())
    for _ in range(N):
        a, s = map(int, input().split())
        ans = "No"
        if a * 2 <= s:
            diff = s - 2 * a
            if diff & a == 0:
                ans = "Yes"
        print(ans)


if __name__ == "__main__":
    main()
