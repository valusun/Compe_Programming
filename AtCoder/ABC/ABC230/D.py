def main():
    N, D = map(int, input().split())
    Walls = [list(map(int, input().split())) for _ in range(N)]
    Walls.sort(key=lambda x: x[1])
    punch_cnt = 1
    punch_point = Walls[0][1]
    for i in range(1, N):
        if Walls[i][0] > punch_point + D - 1:
            punch_cnt += 1
            punch_point = Walls[i][1]
    print(punch_cnt)


if __name__ == "__main__":
    main()
