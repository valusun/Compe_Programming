def main():
    A, B, C, D, E, F = map(int, input().split())
    ans_water, ans_sugar = 0, 0
    ans_concentration = 0
    for a in range(F // A + 1):
        for b in range(F // B + 1):
            water = 100 * (a * A) + 100 * (b * B)
            if water > F:
                break
            for c in range(F // C + 1):
                for d in range(F // D + 1):
                    sugar = c * C + d * D
                    if water + sugar == 0:
                        break
                    if water + sugar > F or sugar > water // 100 * E:
                        break
                    concentration = (100 * sugar) / (sugar + water)
                    if concentration >= ans_concentration:
                        ans_water = water
                        ans_sugar = sugar
                        ans_concentration = concentration
    print(ans_water + ans_sugar, ans_sugar)


if __name__ == "__main__":
    main()
