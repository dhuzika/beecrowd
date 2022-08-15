X = int(input())
Y = int(input())

soma = 0

if X > Y:
    for c in range(Y, X):
        if c == Y:
            continue
        if c % 2 == 1:
            soma += c

if Y > X:
    for c in range(X, Y):
        if c == X:
            continue
        if c % 2 == 1:
            soma += c

if Y == X:
    soma = 0

print(soma)