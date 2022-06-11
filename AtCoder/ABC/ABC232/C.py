from itertools import permutations


def main():
    N, M = map(int, input().split())
    AB = [[False] * N for _ in range(N)]
    CD = [[False] * N for _ in range(N)]
    for c in range(M * 2):
        a, b = map(int, input().split())
        if c < M:
            AB[a - 1][b - 1] = True
            AB[b - 1][a - 1] = True
        else:
            CD[a - 1][b - 1] = True
            CD[b - 1][a - 1] = True

    def IsSame(p):
        for i in range(N):
            for j in range(N):
                if AB[i][j] != CD[p[i]][p[j]]:
                    return False
        return True

    for p in permutations(range(N)):
        if IsSame(p):
            print("Yes")
            break
    else:
        print("No")


if __name__ == "__main__":
    main()
