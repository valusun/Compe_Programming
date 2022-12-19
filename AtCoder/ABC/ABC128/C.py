def main():
    N, M = map(int, input().split())
    switches = [[] for _ in range(N)]
    for i in range(M):
        for j in list(map(int, input().split()))[1:]:
            switches[j - 1].append(i)
    patterns = list(map(int, input().split()))
    pattern_cnt = 0
    for bit in range(2**N):
        pushing_cnts = [0] * M
        for i in range(N):
            if bit & (1 << i):
                for s in switches[i]:
                    pushing_cnts[s] = (pushing_cnts[s] + 1) % 2
        if pushing_cnts == patterns:
            pattern_cnt += 1
    print(pattern_cnt)


if __name__ == "__main__":
    main()
