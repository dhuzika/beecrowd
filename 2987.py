import string
a = string.ascii_lowercase
b = str(input()).lower()
for c in range(len(a)+1):
    if b in a[c]:
        print(c+1)
        break
