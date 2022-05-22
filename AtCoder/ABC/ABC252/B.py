def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    s = max(A)
    for i, v in enumerate(A):
        if v == s and (i + 1) in B:
            print("Yes")
            break
    else:
        print("No")


if __name__ == "__main__":
    main()
