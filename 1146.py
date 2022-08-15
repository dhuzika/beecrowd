n=1
while n != 0:
    n = int(input())
    for c in range(1, n+1):
        if c != n:
            print(c, end=' ')
        else:
            print(c)