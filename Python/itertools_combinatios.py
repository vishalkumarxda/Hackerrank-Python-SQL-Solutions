from itertools import combinations

s,k = input().split(" ")
m = int(k)
u = s.upper()

for i in range(1, m+1):
    for j in list(combinations(sorted(u),i)):
        print("".join(j))
