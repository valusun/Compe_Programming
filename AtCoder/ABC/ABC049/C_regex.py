import re


def main():
    s = input()
    if re.fullmatch("(erase|eraser|dream|dreamer)*", s):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
