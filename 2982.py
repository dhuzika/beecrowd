n=  int(input())
gasto = 0
verba = 0
for c in range(n):
    a = input().split()
    if str(a[0]) == "G":
        gasto += int(a[1])
    if str(a[0]) == "V":
        verba += int(a[1])
if gasto > verba:
    print("NAO VAI TER CORTE, VAI TER LUTA!")
else:
    print("A greve vai parar.")