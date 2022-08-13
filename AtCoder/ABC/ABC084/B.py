import re


def main():
    A, B = map(int, input().split())
    S = input()
    pattern = f"[0-9]{{{A}}}-[0-9]{{{B}}}"
    if re.fullmatch(pattern, S) is None:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
