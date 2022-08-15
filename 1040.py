linha = input().split()
N1 = float(linha[0])
N2 = float(linha[1])
N3 = float(linha[2])
N4 = float(linha[3])

media = (N1 * 2 + N2 * 3 + N3 * 4 + N4)/10
if media >= 7.0:
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")
elif media < 5.0:
    print(f"Media: {media:.1f}")
    print("Aluno reprovado.")
elif 5.0 <= media <= 6.9:
    print(f"Media: {media:.1f}")
    print("Aluno em exame.")
    exame = float(input())
    media = (exame + media)/2
    if media >= 5.0:
        print(f"Nota do exame: {exame:.1f}")
        print("Aluno aprovado.")
        print(f"Media final: {media:.1f}")
    elif media <= 4.9:
        print(f"Nota do exame: {exame:.1f}")
        print("Aluno reprovado.")
        print(f"Media final: {media:.1f}")