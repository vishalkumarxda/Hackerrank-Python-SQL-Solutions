from itertools import combinations_with_replacement

s,k = input().split(" ")

m = int(k)
r = ''.join(sorted(s))

p = list(combinations_with_replacement(r,m))
for i in p:
    print("".join(i))