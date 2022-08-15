n = int(input())
for c in range(n):
    k=0
    j=0
    z=0
    s = str(input())
    while s[z] != "m":
        k+=1
        z+=1
    while s[z+1] != "m":
        j+=1
        z+=1
    k = k-1
    j = j-2
    t = j*k
    a="a"*t
    print(f"k{a}")
