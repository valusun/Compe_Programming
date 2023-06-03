def main():
    A, B = input().split()
    print(int(A) * int(B.replace(".", "")) // 100)


if __name__ == "__main__":
    main()
