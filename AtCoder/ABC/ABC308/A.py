def main():
    def isRule(idx):
        r1 = S[idx] % 25 == 0
        r2 = 100 <= S[idx] <= 675
        if idx == 0:
            return r1 and r2
        return r1 and r2 and S[idx - 1] <= S[idx]

    S = list(map(int, input().split()))
    for i in range(len(S)):
        if not isRule(i):
            print("No")
            break
    else:
        print("Yes")


if __name__ == "__main__":
    main()
