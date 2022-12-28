from itertools import combinations

numbers = [1, 2, 3, 4, 5]

list(combinations([1, 2, 3, 4], 2))


for i in range(1, len(numbers)+1):
    for comb in combinations(numbers, i):
        if sum(comb) == 9:
            print(comb)
