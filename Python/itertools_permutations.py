from itertools import permutations

s,k = input().split(" ")

sorted_s = sorted(list(permutations(s,int(k))))

for i in sorted_s:
    print("".join(i))

