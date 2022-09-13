def main():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]
    ans = float("inf")

    for i in range(2**D):
        solved, point = 0, 0
        for j in range(D):
            if i & (1 << j):
                point += 100 * (j + 1) * pc[j][0] + pc[j][1]
                solved += pc[j][0]
        if point < G:
            for j in range(D - 1, -1, -1):
                if not i & (1 << j):
                    for _ in range(pc[j][0]):
                        point += 100 * (j + 1)
                        solved += 1
                        if point >= G:
                            break
                    else:
                        point += pc[j][1]
                    if point >= G:
                        break
        ans = min(ans, solved)
    print(ans)


if __name__ == "__main__":
    main()
