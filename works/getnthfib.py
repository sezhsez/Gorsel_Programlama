# 0 1 1 2 3 5 8 13 21 34 ...
# 0 1 (0+1= 1)
def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        first = 0
        second = 1
        for i in range(2, n):
            new = first + second
            first = second
            second = new
        return new

arr = getNthFib(7)
print(arr)
