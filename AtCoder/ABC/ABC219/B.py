def main():
    S = [input() for _ in range(3)]
    T = input()
    for t in T:
        print(S[int(t) - 1], end="")


if __name__ == "__main__":
    main()
