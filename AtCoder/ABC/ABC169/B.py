def main():
    _ = int(input())
    A = sorted(list(map(int, input().split())))
    now = A[0]
    for a in A[1:]:
        now *= a
        if now > 10**18:
            print(-1)
            break
    else:
        print(now)


if __name__ == "__main__":
    main()
