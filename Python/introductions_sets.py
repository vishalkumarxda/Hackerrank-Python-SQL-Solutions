def average(array):
    # your code goes here
    a = set(array)
    total = sum(a)
    number = len(set(array))
    
    result = total/number
    return result

if __name__ == '__main__':...