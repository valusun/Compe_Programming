def main():
    N = int(input())
    xy = tuple(tuple(map(int, input().split())) for _ in range(N))
    xy_set = set(xy)
    rect_count = 0
    for upper_left_x, upper_left_y in xy:
        for lower_right_x, lower_right_y in xy:
            if lower_right_x > upper_left_x and upper_left_y > lower_right_y:
                upper_right = (lower_right_x, upper_left_y)
                lower_left = (upper_left_x, lower_right_y)
                if upper_right in xy_set and lower_left in xy_set:
                    rect_count += 1
    print(rect_count)


if __name__ == "__main__":
    main()
