def main():
    S = input()
    T = input()
    for i in range(26):
        for j, s in enumerate(S):
            if chr((ord(s) - 97 + i) % 26 + 97) != T[j]:
                break
        else:
            print("Yes")
            break
    else:
        print("No")


if __name__ == "__main__":
    main()
