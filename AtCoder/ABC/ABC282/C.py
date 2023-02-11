def main():
    _ = int(input())
    S = list(input())
    dq_cnt = 0
    for i, s in enumerate(S):
        if s == '"':
            dq_cnt += 1
        if s == ",":
            if dq_cnt % 2 == 0:
                S[i] = "."
    print("".join(S))


if __name__ == "__main__":
    main()
