def main():
    K = int(input())
    print(f"{21+K//60}:{str(K%60).zfill(2)}")


if __name__ == "__main__":
    main()
