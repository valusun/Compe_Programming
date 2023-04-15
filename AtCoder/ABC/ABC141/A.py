def main():
    weathers = ["Sunny", "Cloudy", "Rainy"]
    w = input()
    print(weathers[(weathers.index(w) + 1) % 3])


if __name__ == "__main__":
    main()
