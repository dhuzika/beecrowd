n = int(input())
i=0
for c in range(1000):
    print(f"N[{c}] = {i}")
    i+=1
    if i == n:
        i = 0