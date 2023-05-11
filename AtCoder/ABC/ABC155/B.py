def main():
    _ = int(input())
    A = list(map(int, input().split()))
    for a in A:
        if a % 2:
            continue
        if a % 3 and a % 5:
            print("DENIED")
            break
    else:
        print("APPROVED")


if __name__ == "__main__":
    main()
