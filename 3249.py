n = int(input())
i=0
lista = []
for c in range(n):
     a = input()
     lista.append(a)
     if "CD" in a:
         i+=1
print(n - i)