def main():
    N = int(input())
    reels = [input() for _ in range(N)]
    ans = 10**9
    for i in range(10):
        appearance_place = [0] * 10
        t = 0
        for reel in reels:
            idx = reel.index(str(i))
            t = max(t, idx + appearance_place[idx])
            appearance_place[idx] += 10
        ans = min(ans, t)
    print(ans)


if __name__ == "__main__":
    main()
