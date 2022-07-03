from collections import defaultdict


def main():
    N = int(input())
    datas = defaultdict(list)
    for i in range(N):
        s, p = input().split()
        datas[s].append([int(p), i + 1])
    point, time = -1, float("inf")
    for s in datas.keys():
        sp, st = datas[s][0]
        if point < sp or (point == sp and st < time):
            point = sp
            time = st
    print(time)


if __name__ == "__main__":
    main()
