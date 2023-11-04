def main():
    B = int(input())
    A = 1
    while A**A <= B:
        if A**A == B:
            print(A)
            return
        A += 1
    print(-1)


if __name__ == "__main__":
    main()
