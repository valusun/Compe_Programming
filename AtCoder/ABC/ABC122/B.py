import re


def main():
    S = input()
    print(max(map(len, re.findall("[ATGC]*", S))))


if __name__ == "__main__":
    main()
