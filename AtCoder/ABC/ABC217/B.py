S = set(["ABC", "ARC", "AGC", "AHC"])
for i in range(3):
    S -= set(input().split())

print(list(S)[0])