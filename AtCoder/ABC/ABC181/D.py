from collections import Counter


def main():
    S = input()
    if len(S) <= 2:
        if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
            print("Yes")
        else:
            print("No")
    else:
        c = Counter(S)
        for n in range(112, 1000, 8):
            if not Counter(str(n)) - c:
                print("Yes")
                break
        else:
            print("No")


if __name__ == "__main__":
    main()
