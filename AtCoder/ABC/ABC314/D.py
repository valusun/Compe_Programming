def main():
    _ = int(input())
    S = list(input())
    Q = int(input())
    queries = [list(input().split()) for _ in range(Q)]
    ri, f = "0", "0"
    for i, q in enumerate(queries):
        if q[0] in ["2", "3"]:
            ri = i
            f = q[0]
    for i, q in enumerate(queries):
        if q[0] == "1":
            S[int(q[1]) - 1] = q[2]
        else:
            if i == ri:
                if f == "2":
                    S = [s.lower() for s in S]
                if f == "3":
                    S = [s.upper() for s in S]
    print(*S, sep="")


if __name__ == "__main__":
    main()
