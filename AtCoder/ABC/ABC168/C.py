import math


def main():
    A, B, H, M = map(int, input().split())
    a = H * 30 + M / 12 * 6 - M * 6
    b = A**2 + B**2 - 2 * A * B * math.cos(math.radians(a))
    print(math.sqrt(b))


if __name__ == "__main__":
    main()
