def main():
    _, M = map(int, input().split())
    gates = [list(map(int, input().split())) for _ in range(M)]
    max_l, min_r = gates[0]
    for left, right in gates[1:]:
        max_l = max(max_l, left)
        min_r = min(min_r, right)
    print(max(0, min_r - max_l + 1))


if __name__ == "__main__":
    main()
