def Check(a, b):
    if a == b:
        return "="
    elif a > b:
        return ">"
    else:
        return "<"


def main():
    A, B, C = map(int, input().split())
    if C % 2 or (A < 0 and B < 0 or A > 0 and B > 0):
        print(Check(A, B))
    else:
        print(Check(abs(A), abs(B)))


if __name__ == "__main__":
    main()
