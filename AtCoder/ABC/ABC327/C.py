def main():
    def CheckRow():
        for a in A:
            if len(set(a)) != 9:
                return False
        return True

    def CheckCol():
        for a in zip(*A):
            if len(set(a)) != 9:
                return False
        return True

    def CheckRange():
        for i in range(3):
            r_start = i * 3
            for j in range(3):
                c_start = j * 3
                tmp = set()
                for k in range(3):
                    for l in range(3):
                        tmp.add(A[r_start + k][c_start + l])
                if len(tmp) != 9:
                    return False
        return True

    A = [list(map(int, input().split())) for _ in range(9)]
    if CheckRow() and CheckCol() and CheckRange():
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
