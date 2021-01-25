i = 17
for a in range(1, i+1):
    print(a, oct(a).replace('0o', ''), hex(a).replace('0x', '').capitalize(), bin(a).replace('0b', ''))
