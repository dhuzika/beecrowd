n = int(input())
linha = input().split()
m2 = 0
m3 = 0
m4 = 0
m5 = 0
for c in range(n):
    a = int(linha[c])
    if a % 2 == 0:
        m2+=1
    if a % 3 == 0:
        m3+=1
    if a % 4 == 0:
        m4+=1
    if a % 5 == 0:
        m5+=1
print(f"{m2} Multiplo(s) de 2")
print(f"{m3} Multiplo(s) de 3")
print(f"{m4} Multiplo(s) de 4")
print(f"{m5} Multiplo(s) de 5")