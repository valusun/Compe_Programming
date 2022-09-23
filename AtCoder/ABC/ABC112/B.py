def main():
    N, T = map(int, input().split())
    cost_time = [list(map(int, input().split())) for _ in range(N)]
    cost_time.sort()
    for c, t in cost_time:
        if t <= T:
            print(c)
            break
    else:
        print("TLE")


if __name__ == "__main__":
    main()
