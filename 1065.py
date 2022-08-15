positivo = 0

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

lista = [a,b,c,d,e]
valor_par = 0

for c in lista:
  if c % 2 == 0:
    valor_par += 1
print(f"{valor_par} valores pares")

    
        
