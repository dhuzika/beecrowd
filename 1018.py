a1 = int(input())

nota100 = int(a1/100)
a = a1 - int((nota100 * 100))

nota50 = int(a/50)
a = a - (nota50 * 50)

nota20 = int(a/20)
a = a - (nota20 * 20)

nota10 = int(a/10)
a = a - (nota10 * 10)

nota5 = int(a/5)
a = a - (nota5 * 5)

nota2 = int(a/2)
a = a - (nota2 * 2)

nota1 = int(a/1)

print(f"{a1}\n{nota100} nota(s) de R$ 100,00\n{nota50} nota(s) de R$ 50,00\n{nota20} nota(s) de R$ 20,00\n{nota10} nota(s) de R$ 10,00\n{nota5} nota(s) de R$ 5,00\n{nota2} nota(s) de R$ 2,00\n{nota1} nota(s) de R$ 1,00")


