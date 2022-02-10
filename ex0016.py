"""" crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira"""

# OPCAO 1
'''
from math import trunc
num = float(input('Escreva um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}: '.format(num, trunc(num)))'''

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
