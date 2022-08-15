X = int(input())
Y = int(input())

if X < Y:
      for c in range(X+1, Y):
            if c % 5 == 2 or c % 5 == 3:
                  print(c)
else:
      for c in range(Y+1, X):
            if c % 5 == 2 or c % 5 == 3:
                  print(c)
