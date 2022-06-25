def main():
    _ = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    same_position = 0
    diff_position = 0
    for i, a in enumerate(A):
        if a in B:
            if a == B[i]:
                same_position += 1
            else:
                diff_position += 1
    print(same_position, diff_position, sep="\n")


if __name__ == "__main__":
    main()
