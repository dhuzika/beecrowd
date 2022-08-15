k = 0
while True:
    k+=1
    n = int(input())
    if n == 0:
        break
    else:
        a = input()
        a = a.replace('+0+','A').replace('+0-','B').replace('-0+','C').replace('-0-','D').replace('-0','-').replace('+0','+').replace('A','+0+').replace('B','+0-').replace('C','-0+').replace('D','-0-')
        if a[-1]=='-' or a[-1]=='+':
          a = a[:-1]
        r = eval(a)
        print(f"Teste {k}\n{r}\n")