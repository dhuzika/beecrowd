while True:
    s=0
    i=0
    j=0
    x = int(input())
    if x == 0:
        break
    else:
        while j != 5:
            if (x+i) % 2 == 0:
                s+=(x+i)
                j+=1
            i+=1
    print(s)