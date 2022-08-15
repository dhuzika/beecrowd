n = int(input())
fibonacci = [0, 1, 1]
n1 = 0
n2 = 1
n3 = n1 + n2
for j in range(60):
    n1 = n2
    n2 = n3
    n3 = n2 + n1
    fibonacci.append(n3)

for c in range(n):
    i = int(input())
    print(f"Fib({i}) = {fibonacci[i]}")