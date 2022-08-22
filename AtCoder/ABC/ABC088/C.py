def main():
    C = [list(map(int, input().split())) for _ in range(3)]
    a1_min = min(C[0])
    for a1 in range(a1_min + 1):
        B = [C[0][0] - a1, C[0][1] - a1, C[0][2] - a1]
        A = [a1, C[1][0] - B[0], C[2][0] - B[0]]
        ab = [[a + b for b in B] for a in A]
        if ab == C:
            print("Yes")
            exit()
    print("No")


if __name__ == "__main__":
    main()
