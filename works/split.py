n = int(input())
for _ in range (n):
    s = input()
    e = ''
    o = ''
    for i in range(len(s)):
        if i%2 == 0:
            e += s[i]
        else:
            o += s[i]
    print(e, o)
