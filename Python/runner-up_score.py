if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    x = sorted(arr)
    print(x[-2])
        