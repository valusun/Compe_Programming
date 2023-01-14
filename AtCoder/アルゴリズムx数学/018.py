def main():
    _ = int(input())
    A = list(map(int, input().split()))
    products = [0, 0, 0, 0]
    for a in A:
        products[a // 100 - 1] += 1
    print(products[0] * products[3] + products[1] * products[2])


if __name__ == "__main__":
    main()
