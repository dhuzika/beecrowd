n = int(input())
lista = ['one', 'two', 'three']
for c in range(n):
    j = 0
    s = str(input())
    if len(s) > 3:
        print('3')
    else:
        if s[0] == 'o':
            j+=1
        if s[1] == 'n':
            j+=1
        if s[2] == 'e':
            j+=1
        if j >= 2:
            print('1')
        else:
            print('2')

        