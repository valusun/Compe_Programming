def main():
    A, op, B = input().split()
    print(int(A) + int(B) if op == "+" else int(A) - int(B))


if __name__ == "__main__":
    main()
