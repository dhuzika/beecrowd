a = int(input())
b = int(input())
c = int(input())
# a
tempo_a = c*2*2 + b*2*1
# b
tempo_b = c*2*1 + a*2*1
# c
tempo_c = b*2*1 + a*2*2

if tempo_a <= tempo_b and tempo_a <= tempo_c:
    print(tempo_a)
elif tempo_b <= tempo_a and tempo_b <= tempo_c:
    print(tempo_b)
elif tempo_c <= tempo_a and tempo_c <= tempo_b:
    print(tempo_c)
