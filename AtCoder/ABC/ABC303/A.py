def rplc(s: str):
    s = s.replace("1", "l")
    s = s.replace("0", "o")
    return s


def main():
    _ = int(input())
    S = rplc(input())
    T = rplc(input())
    print("Yes" if S == T else "No")


if __name__ == "__main__":
    main()
