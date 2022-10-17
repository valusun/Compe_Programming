def main():
    A = [int(input()) for _ in range(5)]
    k = int(input())
    print("Yay!" if max(A) - min(A) <= k else ":(")


if __name__ == "__main__":
    main()
