linha = input().split()
A = int(linha[0])
B = int(linha[1])

if A > B:
    if A % B == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

if A < B:
    if B % A == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

if A == B:
    print('Sao Multiplos')
