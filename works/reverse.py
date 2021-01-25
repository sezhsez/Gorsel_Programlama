ls = []
arr = []
N = int(input())
for i in range(N):
    arr = input().split()
    if arr[0] == 'insert':
        ls.insert(int(arr[1]), int(arr[2]))
    elif arr[0] == 'remove':
        ls.remove(arr[1])
    elif arr[0] == 'append':
        ls.append(arr[1])
    elif arr[0] == 'pop':
        ls.pop()
    elif arr[0] == 'print':
        print(ls)
    elif arr[0] == 'sort':
        ls.sort()
    elif arr[0] == 'reverse':
        ls.reverse()
print(ls)
