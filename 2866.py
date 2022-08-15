n = int(input())
for c in range(n):
    s = str(input())
    x = ""
    for i in s:
        if i.islower():
            x += i
    print(x[::-1])
