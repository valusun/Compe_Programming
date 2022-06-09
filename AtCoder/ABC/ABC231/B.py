def main():
    N = int(input())
    S = [input() for _ in range(N)]
    dic = dict.fromkeys(S, 0)
    for s in S:
        dic[s] += 1
    print(sorted(dic.items(), key=lambda x: x[1], reverse=True)[0][0])


if __name__ == "__main__":
    main()
