def main():
    _ = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        n, *m = map(int, input().split())
        if n == 0:
            A.append(m[0])
        else:
            print(A.pop() if A else "Error")


if __name__ == "__main__":
    main()
