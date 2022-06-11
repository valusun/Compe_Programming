def main():
    X = input()[::-1]
    Cusum = [0]
    for i in X:
        Cusum.append(Cusum[-1] + int(i))
    Ans = []
    res = 0
    for i in range(len(X)):
        res += Cusum[-1] - Cusum[i]
        Ans.append(res % 10)
        res = res // 10
    if res != 0:
        Ans.append(res % 10)
    print(*Ans[::-1], sep="")


if __name__ == "__main__":
    main()
