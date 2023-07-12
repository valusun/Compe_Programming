def main():
    N = input()
    r_idx = max(0, len(N) - 3)
    print(N[: len(N) - r_idx] + "0" * r_idx)


if __name__ == "__main__":
    main()
