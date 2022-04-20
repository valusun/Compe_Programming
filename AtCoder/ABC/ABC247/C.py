def GeneratorSequence(n):
    if n == 1:
        return [1]
    return GeneratorSequence(n - 1) + [n] + GeneratorSequence(n - 1)


print(*GeneratorSequence(int(input())))
