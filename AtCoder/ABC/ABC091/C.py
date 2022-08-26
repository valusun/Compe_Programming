def main():
    N = int(input())
    Red, Blue = [], []
    for i in range(N * 2):
        x, y = map(int, input().split())
        if i < N:
            Red.append([x, y])
        else:
            Blue.append([x, y])

    Red = sorted(Red, key=lambda x: x[1], reverse=True)
    Blue = sorted(Blue)

    used_blue = [False] * N
    for rx, ry in Red:
        for i, (bx, by) in enumerate(Blue):
            if rx < bx and ry < by and not used_blue[i]:
                used_blue[i] = True
                break
    print(sum(used_blue))


if __name__ == "__main__":
    main()
