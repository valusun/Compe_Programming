from bisect import bisect_left


def main():
    H, W, N = map(int, input().split())
    h_idx, w_idx, hw = [], [], []
    for _ in range(N):
        h, w = map(int, input().split())
        h_idx.append(h)
        w_idx.append(w)
        hw.append([h, w])
    h_idx = sorted(list(set(h_idx)))
    w_idx = sorted(list(set(w_idx)))
    for h, w in hw:
        print(bisect_left(h_idx, h) + 1, bisect_left(w_idx, w) + 1)


if __name__ == "__main__":
    main()
