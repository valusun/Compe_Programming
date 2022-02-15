from bisect import bisect_left

# 等差数列の全列挙
Number = []
for i in range(1, 10):
    for j in range(-9, 10):
        tmp = ""
        digit = i
        for k in range(18):
            tmp += str(digit)
            Number.append(int(tmp))
            digit += j
            if digit < 0 or digit > 9:
                break

Number.sort()

N = int(input())
print(Number[bisect_left(Number, N)])