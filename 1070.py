X = int(input())
if X % 2 == 0:
  for c in range(X,X+13):
    if c % 2 == 1:
      print(c)
if X % 2 == 1:
  for c in range(X,X+12):
    if c % 2 == 1:
      print(c)
    