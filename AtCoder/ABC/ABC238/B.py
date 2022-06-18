def main():
    _ = int(input())
    A = list(map(int, input().split()))
    cutting_point = [0, 360]
    now_point = 0
    for a in A:
        now_point = (now_point + a) % 360
        cutting_point.append(now_point)
    cutting_point.sort()
    ans = 0
    for i, v in enumerate(cutting_point[1:]):
        ans = max(ans, v - cutting_point[i])
    print(ans)


if __name__ == "__main__":
    main()
