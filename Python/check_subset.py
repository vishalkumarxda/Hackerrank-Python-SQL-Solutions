T_case = int(input())

for _ in range(T_case):
    N = int(input())
    A = set(map(int,input().split()))
    M = int(input())
    B = set(map(int,input().split()))
    print(A.issubset(B))
