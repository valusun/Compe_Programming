def main():
    A, B = map(int, input().split())
    print("IMPOSSIBLE" if (K := A + B) % 2 else K // 2)


if __name__ == "__main__":
    main()
