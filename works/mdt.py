def merge_the_tools(string, k):
    while string:
        s = string[0:k]
        seen = ''
        for c in s:
            if c not in seen:
                seen += c
        print(seen)
        string = string[k:]

a = 'AAABBAACAASSAAA'
k = 5
merge_the_tools(a,k)
