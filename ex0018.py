""" faça um programa que leia um angulo qualquer e mostre na tela o valor de seno cosseno e tangente desse angulo"""
from math import radians, sin, cos, tan

an: float = float(input('Digite o angulo desejado: '))
s = sin(radians(an))
c = cos(radians(an))
t = tan(radians(an))
print('O seno de {} é {:.2f} o Cosseno é {:.2f} e a tangente é {:.2f}'.format(an, s, c, t))
