n = float(input())
i=1
for c in range(100):
    print(f"N[{c}] = {(n/i):.4f}")
    n=n/i
    i=2
