# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
n = int(input())
a=""
for c in range(n):
    if c == n-1:
        a+= "Ho!"
    else:
        a += "Ho "

print(a)