from itertools import groupby


def main():
    S = input()
    print(len([s for s, _ in groupby(S)]) - 1)


if __name__ == "__main__":
    main()
