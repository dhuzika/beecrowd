while True:
  try:
    linha = input().split()
    # 5
    a = int(linha[0])
    # 3
    b = int(linha[1])
    # ZENIT
    c = input().lower()
    # POLAR
    d = input().lower()
    cu =c.upper()
    du =d.upper()
    resposta = ''
    for i in range(b):
        palavras = input()
        palavras = list(palavras)
        for j in range(len(palavras)):
            for i in range(a):
                if palavras[j] == c[i]:
                    palavras[j] = d[i]
                elif palavras[j] == d[i]:
                    palavras[j] = c[i]
                elif palavras[j] == cu[i]:
                    palavras[j] = du[i]
                elif palavras[j] == du[i]:
                    palavras[j] = cu[i]
            resposta += palavras[j]
        print(resposta)
        resposta = ''
    print()
  except:
    break