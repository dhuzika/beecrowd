n = int(input())
for c in range(n):
    i=0
    a = int(input())
    for v in range(1, a+1):
        if a % v == 0:
            i+=1
    if i == 2:
        print(f"{a} eh primo")
    else:
        print(f"{a} nao eh primo")