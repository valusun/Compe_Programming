# TODO:綺麗にする
def main():
    S = input()
    for s in S:
        if s != "A" and s != "C" and s.isupper():
            print("WA")
            exit()
    if S[0] == "A" and S[2:-1].count("C") == 1:
        print("AC")
    else:
        print("WA")


if __name__ == "__main__":
    main()
