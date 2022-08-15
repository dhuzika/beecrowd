while True:
    k, l = map(int, input().split())
    if k == 0 and l == 0:
        break
    if k % 2 == 0:
        menor_fator_primo = 2
    else:
        for i in range(3, l, 2):
            if k % i == 0:
                menor_fator_primo = i
                break
        else:
            menor_fator_primo = l
    if menor_fator_primo < l:
        print(f"BAD {menor_fator_primo}")
    else:
        print("GOOD")