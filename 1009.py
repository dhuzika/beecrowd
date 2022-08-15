nome = str(input())
salario = float(input())
vendas = float(input())
comissao = 15/100 * vendas
total = salario + comissao
print(f"TOTAL = R$ {total:.2f}")
