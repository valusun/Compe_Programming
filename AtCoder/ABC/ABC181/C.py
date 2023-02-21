def main():
    N = int(input())
    coords = list(tuple(map(int, input().split())) for _ in range(N))
    for i, (x1, y1) in enumerate(coords):
        for j, (x2, y2) in enumerate(coords[i + 1 :], i + 1):
            for (x3, y3) in coords[j + 1 :]:
                vec1 = (x2 - x1, y2 - y1)
                vec2 = (x3 - x1, y3 - y1)
                if vec1[0] * vec2[1] == vec1[1] * vec2[0]:
                    print("Yes")
                    exit()
    print("No")


if __name__ == "__main__":
    main()
