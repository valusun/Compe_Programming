def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()
    print(f"{A-1} {B}" if U == S else f"{A} {B-1}")


if __name__ == "__main__":
    main()
