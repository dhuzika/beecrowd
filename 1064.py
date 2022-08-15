positivo = 0

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

lista = [a,b,c,d,e,f]
positivo = 0
valor_positivo = 0
valores_positivos = 0
p = 0
for o in lista:
  if o > 0:
    valor_positivo += 1
    valores_positivos += o
print(f"{valor_positivo} valores positivos")
print(f"{valores_positivos/valor_positivo:.1f}")
    
        
