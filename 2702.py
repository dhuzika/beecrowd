# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
s=0
linha1 = input().split()
a=int(linha1[0])
b=int(linha1[1])
c=int(linha1[2])
linha2 = input().split()
d=int(linha2[0])
e=int(linha2[1])
f=int(linha2[2])
if d-a > 0:
    s+=d-a
if e-b > 0:
    s+=e-b
if f-c > 0:
    s+=f-c
print(s)