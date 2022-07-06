def main():
    temp = list(map(int, input().split()))
    H, W = temp[:3], temp[3:]
    ans = 0
    # 左上からabc,def,ghiとみなす
    for a in range(1, 31):
        for b in range(1, 31):
            for d in range(1, 31):
                for e in range(1, 31):
                    c = H[0] - a - b
                    f = H[1] - d - e
                    g = W[0] - a - d
                    h = W[1] - b - e
                    i = W[2] - c - f
                    if min(c, f, g, h, i) > 0 and g + h + i == H[2]:
                        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
