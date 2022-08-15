ponto = 0
d = int(input())

if d <= 800:
    ponto+=1
elif 1400 >= d > 800:
    ponto+=2
elif 1400 < d <= 2000:
    ponto+=3

print(ponto)