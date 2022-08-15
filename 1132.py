X = int(input())
Y = int(input())
lista = []
lista2= []
if X < Y:
      for c in range(X, Y+1):
            lista.append(c)
else:
      for c in range(Y, X+1):
            lista.append(c)
for numero in lista:
      if numero % 13 != 0:
            lista2.append(numero)

print(sum(lista2))
