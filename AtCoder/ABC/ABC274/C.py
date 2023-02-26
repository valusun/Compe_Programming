def main():
    _ = int(input())
    A = list(map(int, input().split()))
    depths = [0]
    for a in A:
        depths.append(depths[a - 1] + 1)
        depths.append(depths[a - 1] + 1)
    print(depths)


if __name__ == "__main__":
    main()
