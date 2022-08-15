mae = int(input())
filho1 = int(input())
filho2 = int(input())
filho3 = mae - (filho1 + filho2)
if filho1 > filho2 and filho1 > filho3:
    maior = filho1
if filho2 > filho1 and filho2 > filho3:
    maior = filho2
if filho3 > filho1 and filho3 > filho2:
    maior = filho3
print(maior)