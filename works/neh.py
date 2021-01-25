def rotLeft(a, d):
    return a[d:]+a[:d]

nd = input().split()
n = int(nd[0])
d = int(nd[1])
a = list(map(int, input().rstrip().split()))

result = rotLeft(a, d)
print(result)
