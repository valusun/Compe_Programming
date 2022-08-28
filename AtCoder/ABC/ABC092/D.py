def main():
    a, b = map(int, input().split())
    h, w = 100, 100
    black_field = [["#"] * w for _ in range(h // 2)]
    white_field = [["."] * w for _ in range(h // 2)]

    for i in range(a - 1):
        black_field[1 + ((i * 2) // w) * 2][(i * 2) % w] = "."
    for i in range(b - 1):
        white_field[1 + ((i * 2) // w) * 2][(i * 2) % w] = "#"

    print(h, w)
    for bw in black_field + white_field:
        print("".join(bw))


if __name__ == "__main__":
    main()
