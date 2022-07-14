def main():
    N, M = map(int, input().split())
    humans = [list(map(int, input().split())) for _ in range(N)]
    check_points = [list(map(int, input().split())) for _ in range(M)]
    for x1, y1 in humans:
        near_check_point, near_dist = -1, 10**18
        for idx, (x2, y2) in enumerate(check_points, 1):
            if (dist := abs(x1 - x2) + (abs(y1 - y2))) < near_dist:
                near_dist = dist
                near_check_point = idx
        print(near_check_point)


if __name__ == "__main__":
    main()
