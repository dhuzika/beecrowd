n = int(input())
for c in range(n):
  a = input().split()
  linha = input().split()
  b = int(linha[0])
  c = int(linha[1])
  if a [1] == "PAR" and (b + c) % 2 == 0:
    print(a[0])
  elif a [1] == "PAR" and (b+c) % 2 == 1:
    print(a[2])
  elif a[1] == "IMPAR" and (b+c) % 2 == 0:
    print(a[2])
  else:
    print(a[0])
  