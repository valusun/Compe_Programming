def main():
    O = input()
    E = input()
    ans = [None] * (len(O) + len(E))
    ans[::2] = O
    ans[1::2] = E
    print("".join(ans))


if __name__ == "__main__":
    main()
