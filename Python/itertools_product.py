from itertools import product  #for cartesian product need to import itertools.product()

a = list(map(int, input().split())) 
b = list(map(int, input().split()))

result = list(product(a,b))

print(*result) # '*' it is used for seperate the result with space