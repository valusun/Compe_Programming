def main():
    N, Q = map(int, input().split())
    player = [0] * N
    for _ in range(Q):
        e, x = map(int, input().split())
        if e == 1:
            player[x - 1] += 1
        elif e == 2:
            player[x - 1] += 2
        else:
            print("Yes" if player[x - 1] >= 2 else "No")


if __name__ == "__main__":
    main()
