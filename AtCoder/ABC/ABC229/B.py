def main():
    A, B = input().split()
    min_length = min(len(A), len(B))
    A, B = A[::-1], B[::-1]
    for i in range(min_length):
        if int(A[i]) + int(B[i]) > 9:
            print("Hard")
            break
    else:
        print("Easy")


if __name__ == "__main__":
    main()
