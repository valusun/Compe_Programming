def main():
    A, B, C, D = map(int, input().split())
    L = A + B
    R = C + D
    print("Balanced" if L == R else "Left" if L > R else "Right")


if __name__ == "__main__":
    main()
