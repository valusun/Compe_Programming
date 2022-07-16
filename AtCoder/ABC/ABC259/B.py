from math import sin, cos, radians


def main():
    x, y, d = map(int, input().split())
    d = radians(d)
    rotation_x = x * cos(d) - y * sin(d)
    rotation_y = x * sin(d) + y * cos(d)
    print(rotation_x, rotation_y)


if __name__ == "__main__":
    main()
