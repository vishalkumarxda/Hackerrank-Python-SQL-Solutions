R, c = map(int,input().split(' '))

for i in range (1, R, 2):
    print((".|."*i).center(c,'-'))
print(("WELCOME").center(c,'-'))

for i in range (R-2, 0, -2):
    print((".|."*i).center(c,'-'))