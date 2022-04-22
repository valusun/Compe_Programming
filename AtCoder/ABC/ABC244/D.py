def main():
    S = input().split()
    T = input().split()
    diff = 0
    for i in range(3):
        if S[i] != T[i]:
            diff += 1
    print("Yes") if diff != 2 else print("No")


if __name__ == "__main__":
    main()
