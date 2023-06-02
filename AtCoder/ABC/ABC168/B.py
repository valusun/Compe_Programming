def main():
    K = int(input())
    S = input()
    if len(S) > K:
        S = f"{S[:K]}..."
    print(S)


if __name__ == "__main__":
    main()
