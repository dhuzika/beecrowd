alcool = 0
gasolina = 0
diesel = 0
n=0
j = True
while j == True:
      n=int(input())
      while n > 4 or n < 1:
            n = int(input())
      if n == 1:
            alcool += 1
      if n == 2:
            gasolina += 1
      if n == 3:
            diesel += 1
      if n == 4:
            j=False

print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")