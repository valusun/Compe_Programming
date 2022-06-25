from collections import defaultdict


def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    S = input()
    L, R = defaultdict(int), defaultdict(int)
    for i in range(N):
        if S[i] == "L":
            if XY[i][1] in L:
                L[XY[i][1]] = max(L[XY[i][1]], XY[i][0])
            else:
                L[XY[i][1]] = XY[i][0]
        else:
            if XY[i][1] in R:
                R[XY[i][1]] = min(R[XY[i][1]], XY[i][0])
            else:
                R[XY[i][1]] = XY[i][0]

    for k, v in L.items():
        if k not in R:
            continue
        if R[k] <= v:
            print("Yes")
            break
    else:
        print("No")


if __name__ == "__main__":
    main()
