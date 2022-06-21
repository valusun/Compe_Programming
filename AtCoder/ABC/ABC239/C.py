def main():
    x1, y1, x2, y2 = map(int, input().split())
    offset_x = [-2, -1, 1, 2, 2, 1, -1, -2]
    offset_y = [1, 2, 2, 3, -1, -2, -2, -1]
    for i in range(8):
        point_x, point_y = offset_x[i] + x1, offset_y[i] + y1
        if (x2 - point_x) ** 2 + (y2 - point_y) ** 2 == 5:
            print("Yes")
            break
    else:
        print("No")


if __name__ == "__main__":
    main()
