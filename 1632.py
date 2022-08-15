n = int(input())
for c in range(n):
    s = str(input()).lower()
    r=1
    for i in s:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "s":
            r*=3
        else:
            r*=2
    print(r)