n = int(input())
a = 1
for c in range(n):
    print(f"{a**1} {a**2} {a**3}")
    print(f"{a**1} {a**2 + 1} {a**3+1}")
    a += 1
