positivo = 0

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

lista = [a,b,c,d,e]
valor_par = 0
valor_impar = 0
valor_positivo = 0
valor_negativo = 0

for c in lista:
  if c % 2 == 0:
    valor_par += 1
  if c % 2 == 1:
    valor_impar += 1
  if c > 0:
    valor_positivo += 1
  if c < 0:
    valor_negativo += 1
print(f"{valor_par} valor(es) par(es)")
print(f"{valor_impar} valor(es) impar(es)")
print(f"{valor_positivo} valor(es) positivo(s)")
print(f"{valor_negativo} valor(es) negativo(s)")

    
        
