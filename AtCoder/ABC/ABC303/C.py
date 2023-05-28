def main():
    _, M, H, K = map(int, input().split())
    S = input()
    items = set(tuple(map(int, input().split())) for _ in range(M))
    dic = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    x, y = 0, 0
    used = set()
    for s in S:
        H -= 1
        if H < 0:
            print("No")
            break
        mx, my = dic[s]
        x, y = x + mx, y + my
        if (x, y) not in items or (x, y) in used or H >= K:
            continue
        H = K
        used.add((x, y))
    else:
        print("Yes")


if __name__ == "__main__":
    main()
