s=1
i=2
for c in range(3, 39, 2):
    s = s + c/i
    i*=2
print(f"{s:.2f}")