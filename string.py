from itertools import combinations

s = input("Enter string : ")
n = len(s)

for i in range(1, n + 1):
    for combo in combinations(s, i):
        print(''.join(combo))
