yazi = "WELOME"
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
m = a[0]
n = a[1]

for x in range(m//2):
    mid = 3*(2*x+1)
    left = right = int((n-mid)/2)
    print('-'*left, '.|.'*(int(mid/3)), '-'*right, sep='')

print(((n-len(yazi))//2)*'-',yazi,((n-len(yazi))//2)*'-', sep='')

for y in range((m//2)-1, -1, -1):
    mid = 3*(2*y+1)
    left = right = int((n-mid)/2)
    print('-'*left, '.|.'*(int(mid/3)), '-'*right, sep='')
