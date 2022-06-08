def main():
    N = int(input())
    pascal = [[1]]
    for i in range(1, N):
        tmp = []
        for j in range(len(pascal[-1])):
            if not j:
                tmp.append(1)
            else:
                tmp.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
        tmp.append(1)
        pascal.append(tmp)
    for p in pascal:
        print(*p)


if __name__ == "__main__":
    main()
