def main():
    _ = int(input())
    rates = list(map(int, input().split()))
    colors = [0] * 9
    for r in rates:
        if r >= 3200:
            colors[-1] += 1
        else:
            colors[r // 400] += 1
    min_color = 8 - colors[:-1].count(0)
    if not min_color:
        print(1, colors[-1])
    else:
        print(min_color, min_color + colors[-1])


if __name__ == "__main__":
    main()
