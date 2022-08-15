linha = input().split()
x = int(linha[0])
y = int(linha[1])
z=1
if y % x == 0:
      for c in range(1, y//x + 1):
            for i in range(x):
                  if (i+1) % x == 0:
                        print(z+i, end='')
                  else:
                        print(z+i, end=' ')
            print('', end='\n')
            z+=x
else:
      for c in range(1, y//x + 2):
            for i in range(x):
                  if z+i == y+1:
                        break
                  print(z+i, end=' ')

            print('', end='\n')
            z+=x

