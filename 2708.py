salida = 0
vuelta = 0
a=0
b=0
while True:
    s = str(input()).split()
    if s[0] == "SALIDA":
        salida += int(s[1])
        a+=1
    if s[0] == "VUELTA":
        vuelta += int(s[1])
        b+=1
    if s[0] == "ABEND":
      break
print(salida-vuelta)
print(a-b)
    