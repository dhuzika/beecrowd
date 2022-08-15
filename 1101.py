while(True):
  linha = input().split()
  m = int(linha[0])
  n = int(linha[1])


  lista = []

  if m <= 0 or n <= 0:
    break
  else:
    if m > n:
      m, n = n, m
    for i in range(m, n + 1):
      lista.append(i)
    soma = sum(lista)
    a = (' '.join(map(str, lista)))
    print(f"{a} Sum={soma}")