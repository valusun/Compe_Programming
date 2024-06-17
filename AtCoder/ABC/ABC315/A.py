import re


def main():
    print(re.sub("a|i|u|e|o", "", input()))


if __name__ == "__main__":
    main()
