def main():
    x, y, z = map(int, input().split())

    if y < 0:
        x, y, z = -x, -y, -z
    if x < y:
        print(abs(x))
    else:
        if z < y:
            print(abs(z) + abs(x - z))
        else:
            print(-1)


if __name__ == "__main__":
    main()
