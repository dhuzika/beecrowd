op = str(input())
s = 0
k=1
for j in range(12):
    for i in range(12):
        n=float(input())
        if i >= j+1:
            s+=n

if op == "S":
    print(f"{s:.1f}")
else:
    print(f"{s/66:.1f}")


