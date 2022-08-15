s = str(input())
normal = ''
vogais = ['a', 'e', 'i', 'o', 'u']
for i in s:
    if i in vogais:
        normal += i
if normal == normal[::-1]:
    print("S")
else:
    print("N")