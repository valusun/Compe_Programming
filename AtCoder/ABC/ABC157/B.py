def main():
    A = [list(map(int, input().split())) for _ in range(3)]
    c = [[False] * 3 for _ in range(3)]
    N = int(input())
    for _ in range(N):
        b = int(input())
        for i in range(3):
            if b in A[i]:
                c[i][A[i].index(b)] = True
    for i in range(3):
        y = c[i][0] is True and c[i][0] == c[i][1] == c[i][2]
        t = c[0][i] is True and c[0][i] == c[1][i] == c[2][i]
        n1 = c[0][0] is True and c[0][0] == c[1][1] == c[2][2]
        n2 = c[0][2] is True and c[0][2] == c[1][1] == c[2][0]
        if y or t or n1 or n2:
            print("Yes")
            break
    else:
        print("No")


if __name__ == "__main__":
    main()
