def main():
    _ = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))

    opt_temp, near_point = float("inf"), 0
    for i, h in enumerate(H, 1):
        temp = T - h * 0.006
        if abs(A - temp) < opt_temp:
            opt_temp = abs(A - temp)
            near_point = i
    print(near_point)


if __name__ == "__main__":
    main()
