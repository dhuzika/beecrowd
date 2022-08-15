linha = input().split()
hi = int(linha[0])
mi = int(linha[1])
hf = int(linha[2])
mf = int(linha[3])
tm = 0
   #6   #7
if hi < hf:
    th = hf - hi

else: #16 < #4
    th = (24 - hi) + hf

if mi < mf:
    tm = mi - mf

elif mi == mf:
    tm == 0

else: # 50 20
    tm = (60-mi) + mf
    th -= 1

if hi == hf and mi < mf:
    th -= 24



print(f"O JOGO DUROU {abs(th)} HORA(S) E {abs(tm)} MINUTO(S)")