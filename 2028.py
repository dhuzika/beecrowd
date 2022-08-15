k=0
while True:
  try:
    k+=1
    lista = [0]
    n = int(input())
    for c in range(n+1):
      for i in range(1, c+1):
        lista.append(c)
    if n == 0:
      print(f"Caso {k}: {len(lista)} numero")
    else:
      print(f"Caso {k}: {len(lista)} numeros")
    lista = str(lista)
    r = lista.replace('[','').replace(']','').replace(',','')
    print(r)
    print()
  except:
    break