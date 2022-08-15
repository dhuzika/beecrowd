t_dias = int(input())
anos = t_dias//365
t_dias = t_dias - anos * 365
meses = t_dias//30
t_dias = t_dias - 30 * meses
dias = t_dias

print(f"{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)")