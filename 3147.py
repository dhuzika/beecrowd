linha = input().split()
h = int(linha[0])
e = int(linha[1])
a = int(linha[2])
o = int(linha[3])
w = int(linha[4])
x = int(linha[5])
bem = h+e+a+x
mal = o+w
if bem>=mal:
    print("Middle-earth is safe.")
else:
    print("Sauron has returned.")