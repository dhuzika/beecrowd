linha = input().split()
a = int(linha[0])
b = int(linha[1])
c = int(linha[2])
p = a-b
s = b-c
if a > b:
  if c > b:
    print(":)")
  else:
    if s < p:
      print(":)")
    else:
      print(":(")
elif a < b:
  if c < b:
    print(":(")
  else:
    if s > p:
      print(":(")
    else:
      print(":)")
else:
  if c > a:
    print(":)")
  else:
    print(":(")