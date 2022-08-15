while(True):
  linha = input().split()
  m = int(linha[0])
  n = int(linha[1])


  lista = []

  if m == n:
    break
  else:
    if m > n:
        print("Decrescente")
    if n > m:
        print("Crescente")