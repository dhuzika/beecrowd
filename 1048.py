salario = float(input())
if 0 <= salario <= 400.00:
    reajuste = 15/100 * salario

if 400.01 <= salario <= 800.00:
    reajuste = 12/100 * salario

if 800.01 <= salario <= 1200.00:
    reajuste = 10/100 * salario

if 1200.01 <= salario <= 2000.00:
    reajuste = 7/100 * salario

if salario > 2000.00:
    reajuste = 4/100 * salario

novo_salario = salario + reajuste
percentual = novo_salario * 100 / salario - 100

print(f"Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {int(round(percentual,2))} %")

