string = "ThIsisCoNfUsInG"
substring = 'is'
count = 0
for i in range (0, len(string)):
    temp = string[i:i+len(substring)]
    if temp == substring:
        count += 1
print(count)
