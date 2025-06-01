M = int(input())
e = set(map(int,input().split()))

N = int(input())
f = set(map(int,input().split()))

x = e.symmetric_difference(f)
y = sorted(x)

for i in y:
    print(i)