def main():
    N, Q = map(int, input().split())
    went = [False] * N
    now = 0
    for _ in range(Q):
        event = list(map(int, input().split()))
        if event[0] == 2:
            x = event[1]
            went[x - 1] = True
        elif event[0] == 3:
            while went[now]:
                now += 1
            print(now + 1)


if __name__ == "__main__":
    main()
