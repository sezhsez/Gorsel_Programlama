arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split()))) #Enter 6x6 natrix
maxsum = -64

for i in range(4):
    for j in range(4):
        hgsum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        if hgsum > maxsum:
            maxsum = hgsum
print(maxsum)
