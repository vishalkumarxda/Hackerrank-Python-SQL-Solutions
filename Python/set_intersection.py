n = int(input())
e = set(map(int,input().split()))

m = int(input())
f = set(map(int,input().split()))

print(len(e.intersection(f)))
