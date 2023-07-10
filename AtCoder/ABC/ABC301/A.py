def main():
    N = int(input())
    S = input()
    if S.count("T") > S.count("A"):
        print("T")
    elif S.count("T") < S.count("A"):
        print("A")
    else:
        tgt = N // 2
        t, a = 0, 0
        for s in S:
            if s == "T":
                t += 1
            else:
                a += 1
            if t == tgt:
                print("T")
                break
            if a == tgt:
                print("A")
                break


if __name__ == "__main__":
    main()
