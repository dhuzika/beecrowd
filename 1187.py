op = str(input())
s = 0
for j in range(12):
    for i in range(12):
        n=float(input())
        if j < i < 11-j:
            s+=n

if op == "S":
    print(f"{s:.1f}")
else:
    print(f"{s/30:.1f}")


