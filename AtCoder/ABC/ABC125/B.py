def main():
    _ = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    x, y = 0, 0
    for v, c in zip(V, C):
        if v > c:
            x += v
            y += c
    print(x - y)


if __name__ == "__main__":
    main()
