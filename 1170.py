n = int(input())
for c in range(n):
    m = float(input())
    d=0
    while m > 1:
        m = m / 2
        d += 1
    print(f'{d} dias')