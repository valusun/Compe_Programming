def main():
    _ = int(input())
    S = list(input())
    Q = int(input())
    last_number = "1"
    no_tgt_indexes = set()
    for _ in range(Q):
        t, x, c = input().split()
        x = int(x) - 1
        if t == "1":
            S[x] = c
            no_tgt_indexes.add(x)
        else:
            no_tgt_indexes = set()
            last_number = t
    ans = ""
    if last_number == "1":
        ans = "".join(S)
    elif last_number == "2":
        for i, s in enumerate(S):
            ans += s if i in no_tgt_indexes else s.lower()
    else:
        for i, s in enumerate(S):
            ans += s if i in no_tgt_indexes else s.upper()
    print(ans)


if __name__ == "__main__":
    main()
