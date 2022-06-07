def main():
    N = int(input())
    if N >= 42:
        N += 1
    print(f"AGC{str(N).zfill(3)}")


if __name__ == "__main__":
    main()
